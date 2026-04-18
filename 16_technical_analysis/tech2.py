
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


r = rsi(data['Close'], length=14)
print(r)




mpf.plot(data, type='candle', style='yahoo',
         title='TSLA 5m', ylabel='Price ($)',
            addplot=[mpf.make_addplot(r, panel=1, color='purple', ylabel='RSI')])

#atr
#adx