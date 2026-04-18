
# --- Download data ---
import yfinance as yf
import datetime as dt
import numpy as np
from pandas import Series, DataFrame
import mplfinance as mpf


def bbands(
    close: Series,
    length: int = None,
    lower_std: float = None,
    upper_std: float = None,
    ddof: int = None,
    mamode: str = None,
    offset: int = None,
    **kwargs
) -> DataFrame:
    """Bollinger Bands (no pandas_ta dependency)"""
    # Defaults / validation
    length = int(length) if isinstance(length, int) and length > 0 else 5
    lower_std = float(lower_std) if lower_std is not None and float(lower_std) > 0 else 2.0
    upper_std = float(upper_std) if upper_std is not None and float(upper_std) > 0 else 2.0
    ddof = int(ddof) if isinstance(ddof, int) and 0 <= ddof < length else 1
    mamode = mamode.lower() if isinstance(mamode, str) else "sma"
    offset = int(offset) if isinstance(offset, int) else 0

    if close is None or len(close) < length:
        return None

    # Moving average
    if mamode == "ema":
        mid = close.ewm(span=length, adjust=False).mean()
    elif mamode == "wma":
        weights = np.arange(1, length + 1, dtype=float)
        mid = close.rolling(length).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
    else:  # sma (default)
        mid = close.rolling(window=length).mean()

    # Standard deviation & bands
    std_dev = close.rolling(window=length).std(ddof=ddof)
    lower = mid - lower_std * std_dev
    upper = mid + upper_std * std_dev

    # Bandwidth & percent-b  (avoid division by zero)
    ulr = upper - lower
    ulr_safe = ulr.where(ulr != 0, np.nan)
    mid_safe = mid.where(mid != 0, np.nan)
    bandwidth = 100 * ulr / mid_safe
    percent = (close - lower) / ulr_safe

    # Offset
    if offset != 0:
        lower = lower.shift(offset)
        mid = mid.shift(offset)
        upper = upper.shift(offset)
        bandwidth = bandwidth.shift(offset)
        percent = percent.shift(offset)

    # Fill
    if "fillna" in kwargs:
        lower = lower.fillna(kwargs["fillna"])
        mid = mid.fillna(kwargs["fillna"])
        upper = upper.fillna(kwargs["fillna"])
        bandwidth = bandwidth.fillna(kwargs["fillna"])
        percent = percent.fillna(kwargs["fillna"])

    # Column names
    _props = f"_{length}_{lower_std}_{upper_std}"
    lower.name = f"BBL{_props}"
    mid.name = f"BBM{_props}"
    upper.name = f"BBU{_props}"
    bandwidth.name = f"BBB{_props}"
    percent.name = f"BBP{_props}"

    df = DataFrame(
        {lower.name: lower, mid.name: mid, upper.name: upper,
         bandwidth.name: bandwidth, percent.name: percent},
        index=close.index
    )
    df.name = f"BBANDS{_props}"
    return df


e = dt.datetime.now()
s = e - dt.timedelta(days=5)
print(s, e)
data = yf.download('TSLA', start=s.date(), end=e.date(),
                   multi_level_index=False, interval='5m', ignore_tz=True)
print(data)

# b1 = bbands(data['Close'], length=20)
# print(b1)


# mpf.plot(data, type='candle', style='yahoo',
#          title='TSLA 5m', ylabel='Price ($)',
#          addplot=[
#              mpf.make_addplot(b1['BBL_20_2.0_2.0'], color='blue'),
#              mpf.make_addplot(b1['BBM_20_2.0_2.0'], color='orange'),
#              mpf.make_addplot(b1['BBU_20_2.0_2.0'], color='red')
#          ])

# rsi

def rsi(
    close: Series,
    length: int = None,
    scalar: float = None,
    mamode: str = None,
    drift: int = None,
    offset: int = None,
    **kwargs
) -> Series:
    """Relative Strength Index (no pandas_ta dependency)"""
    # Defaults / validation
    length = int(length) if isinstance(length, int) and length > 0 else 14
    scalar = float(scalar) if scalar is not None and float(scalar) > 0 else 100.0
    mamode = mamode.lower() if isinstance(mamode, str) else "rma"
    drift = int(drift) if isinstance(drift, int) and drift > 0 else 1
    offset = int(offset) if isinstance(offset, int) else 0

    if close is None or len(close) < length + 1:
        return None

    # Price changes
    delta = close.diff(drift)
    positive = delta.clip(lower=0)
    negative = delta.clip(upper=0)

    # Smoothed averages
    def _smooth(series):
        if mamode == "ema":
            return series.ewm(span=length, adjust=False).mean()
        elif mamode == "sma":
            return series.rolling(window=length).mean()
        else:  # rma — Wilder's smoothing (default)
            alpha = 1.0 / length
            return series.ewm(alpha=alpha, adjust=False).mean()

    positive_avg = _smooth(positive)
    negative_avg = _smooth(negative.abs())

    denom = positive_avg + negative_avg
    denom_safe = denom.where(denom != 0, np.nan)
    result = scalar * positive_avg / denom_safe

    # Offset
    if offset != 0:
        result = result.shift(offset)

    # Fill
    if "fillna" in kwargs:
        result = result.fillna(kwargs["fillna"])

    result.name = f"RSI_{length}"
    return result


# r = rsi(data['Close'], length=14)
# print(r)




# mpf.plot(data, type='candle', style='yahoo',
#          title='TSLA 5m', ylabel='Price ($)',
#             addplot=[mpf.make_addplot(r, panel=1, color='purple', ylabel='RSI')])

# atr

def atr(
    high: Series,
    low: Series,
    close: Series,
    length: int = None,
    mamode: str = None,
    drift: int = None,
    offset: int = None,
    **kwargs
) -> Series:
    """Average True Range (no pandas_ta dependency)"""
    # Defaults / validation
    length = int(length) if isinstance(length, int) and length > 0 else 14
    mamode = mamode.lower() if isinstance(mamode, str) else "rma"
    drift = int(drift) if isinstance(drift, int) and drift > 0 else 1
    offset = int(offset) if isinstance(offset, int) else 0

    if high is None or low is None or close is None:
        return None
    if len(close) < length + 1:
        return None

    # True Range: max of three measures
    prev_close = close.shift(drift)
    tr = (
        (high - low).abs()
        .combine((high - prev_close).abs(), max)
        .combine((low - prev_close).abs(), max)
    )

    # Seed with SMA of first `length` TRs, then apply Wilder's smoothing (rma)
    percent = kwargs.pop("percent", False)

    def _smooth(series):
        if mamode == "ema":
            return series.ewm(span=length, adjust=False).mean()
        elif mamode == "sma":
            return series.rolling(window=length).mean()
        else:  # rma — Wilder's smoothing (default)
            alpha = 1.0 / length
            # Seed first value with SMA
            result = series.copy().astype(float)
            first_valid = series.first_valid_index()
            if first_valid is None:
                return series
            iloc_start = series.index.get_loc(first_valid)
            seed_end = iloc_start + length
            if seed_end > len(series):
                return series.rolling(window=length).mean()
            seed = series.iloc[iloc_start:seed_end].mean()
            values = series.to_numpy(dtype=float)
            out = np.full(len(values), np.nan)
            out[seed_end - 1] = seed
            for i in range(seed_end, len(values)):
                out[i] = alpha * values[i] + (1 - alpha) * out[i - 1]
            result[:] = out
            return result

    result = _smooth(tr)

    if np.all(np.isnan(result)):
        return None

    if percent:
        result = result * 100 / close

    # Offset
    if offset != 0:
        result = result.shift(offset)

    # Fill
    if "fillna" in kwargs:
        result = result.fillna(kwargs["fillna"])

    result.name = f"ATR{mamode[0]}{'p' if percent else ''}_{length}"
    return result


# at1 = atr(data['High'], data['Low'], data['Close'], length=14)
# print(at1)



# mpf.plot(data, type='candle', style='yahoo',
#          title='TSLA 5m', ylabel='Price ($)',
#             addplot=[mpf.make_addplot(at1, panel=1, color='green', ylabel='ATR')])



# supertrend

def supertrend(
    high: Series,
    low: Series,
    close: Series,
    length: int = None,
    atr_length: int = None,
    multiplier: float = None,
    atr_mamode: str = None,
    offset: int = None,
    **kwargs
) -> DataFrame:
    """Supertrend (no pandas_ta dependency)"""
    # Defaults / validation
    length = int(length) if isinstance(length, int) and length > 0 else 7
    atr_length = int(atr_length) if isinstance(atr_length, int) and atr_length > 0 else length
    multiplier = float(multiplier) if multiplier is not None and float(multiplier) > 0 else 3.0
    atr_mamode = atr_mamode.lower() if isinstance(atr_mamode, str) else "rma"
    offset = int(offset) if isinstance(offset, int) else 0

    if high is None or low is None or close is None:
        return None
    if len(close) < length + 1:
        return None

    # HL2 midpoint and ATR bands
    hl2_ = (high + low) / 2
    matr = multiplier * atr(high, low, close, length=atr_length, mamode=atr_mamode)
    lb = hl2_ - matr   # lower band (support in uptrend)
    ub = hl2_ + matr   # upper band (resistance in downtrend)

    m = len(close)
    dir_ = [1] * m
    trend = [np.nan] * m
    long = [np.nan] * m
    short = [np.nan] * m

    lb_arr = lb.to_numpy(dtype=float).copy()
    ub_arr = ub.to_numpy(dtype=float).copy()
    close_arr = close.to_numpy(dtype=float)

    for i in range(1, m):
        if close_arr[i] > ub_arr[i - 1]:
            dir_[i] = 1
        elif close_arr[i] < lb_arr[i - 1]:
            dir_[i] = -1
        else:
            dir_[i] = dir_[i - 1]
            if dir_[i] > 0 and lb_arr[i] < lb_arr[i - 1]:
                lb_arr[i] = lb_arr[i - 1]
            if dir_[i] < 0 and ub_arr[i] > ub_arr[i - 1]:
                ub_arr[i] = ub_arr[i - 1]

        if dir_[i] > 0:
            trend[i] = long[i] = lb_arr[i]
        else:
            trend[i] = short[i] = ub_arr[i]

    # Mask warm-up period
    dir_[:length] = [np.nan] * length

    _props = f"_{length}_{multiplier}"
    df = DataFrame(
        {
            f"SUPERT{_props}": trend,
            f"SUPERTd{_props}": dir_,
            f"SUPERTl{_props}": long,
            f"SUPERTs{_props}": short,
        },
        index=close.index,
    )
    df.name = f"SUPERT{_props}"

    # Offset
    if offset != 0:
        df = df.shift(offset)

    # Fill
    if "fillna" in kwargs:
        df = df.fillna(kwargs["fillna"])

    return df


sup1 = supertrend(data['High'], data['Low'], data['Close'], length=7, multiplier=3)
print(sup1)



# mpf.plot(data, type='candle', style='yahoo',
#          title='TSLA 5m', ylabel='Price ($)',
#          addplot=[
#              mpf.make_addplot(sup1['SUPERTl_7_3.0'], color='blue'),
#              mpf.make_addplot(sup1['SUPERTs_7_3.0'], color='black'),
        
#          ])


# macd

def macd(
    close: Series,
    fast: int = None,
    slow: int = None,
    signal: int = None,
    offset: int = None,
    **kwargs
) -> DataFrame:
    """Moving Average Convergence Divergence (no pandas_ta dependency)"""
    # Defaults / validation
    fast = int(fast) if isinstance(fast, int) and fast > 0 else 12
    slow = int(slow) if isinstance(slow, int) and slow > 0 else 26
    signal = int(signal) if isinstance(signal, int) and signal > 0 else 9
    if slow < fast:
        fast, slow = slow, fast
    offset = int(offset) if isinstance(offset, int) else 0
    as_mode = kwargs.get("asmode", False)

    if close is None or len(close) < slow + signal - 1:
        return None

    def _ema(series, length):
        return series.ewm(span=length, adjust=False).mean()

    # Fast and slow EMAs
    fastma = _ema(close, fast)
    slowma = _ema(close, slow)

    macd_line = fastma - slowma

    # Signal EMA computed from first valid MACD value onward
    fvi = macd_line.first_valid_index()
    macd_fvi = macd_line.loc[fvi:]
    signalma = _ema(macd_fvi, signal).reindex(macd_line.index)
    histogram = macd_line - signalma

    # AS mode: re-smooth the adjusted MACD
    if as_mode:
        macd_line = macd_line - signalma
        fvi = macd_line.first_valid_index()
        macd_fvi = macd_line.loc[fvi:]
        signalma = _ema(macd_fvi, signal).reindex(macd_line.index)
        histogram = macd_line - signalma

    # Offset
    if offset != 0:
        macd_line = macd_line.shift(offset)
        histogram = histogram.shift(offset)
        signalma = signalma.shift(offset)

    # Fill
    if "fillna" in kwargs:
        macd_line = macd_line.fillna(kwargs["fillna"])
        histogram = histogram.fillna(kwargs["fillna"])
        signalma = signalma.fillna(kwargs["fillna"])

    _asmode = "AS" if as_mode else ""
    _props = f"_{fast}_{slow}_{signal}"
    macd_line.name = f"MACD{_asmode}{_props}"
    histogram.name = f"MACD{_asmode}h{_props}"
    signalma.name = f"MACD{_asmode}s{_props}"

    df = DataFrame(
        {macd_line.name: macd_line, histogram.name: histogram, signalma.name: signalma},
        index=close.index,
    )
    df.name = f"MACD{_asmode}{_props}"
    return df


m1 = macd(data['Close'], fast=12, slow=26, signal=9)
print(m1)

mpf.plot(data, type='candle', style='yahoo',
            title='TSLA 5m', ylabel='Price ($)',
            addplot=[
                mpf.make_addplot(m1['MACD_12_26_9'], panel=1, color='blue', ylabel='MACD'),
                mpf.make_addplot(m1['MACDh_12_26_9'], panel=1, color='red', type='bar', ylabel='Histogram'),
                mpf.make_addplot(m1['MACDs_12_26_9'], panel=1, color='black', ylabel='Signal')
            ])
