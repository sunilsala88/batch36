#talib C++->python #fast #difficult to install
#pandasta #pure python #easy to install #slower than talib #update
#ta #less indicator

#problem when you install old library

import numpy as np
from pandas import Series

# --- SMA implementation (no pandas_ta required) ---
def sma(close: Series, length: int = 10, offset: int = 0, **kwargs) -> Series:
    """Simple Moving Average using numpy convolution."""
    length = max(int(length), 1)
    min_periods = int(kwargs.get("min_periods", length))
    if len(close) < max(length, min_periods):
        return None

    weights = np.ones(length) / length
    # 'valid' gives only fully-overlapping windows (len = N - length + 1)
    conv = np.convolve(close.to_numpy(), weights, mode='valid')
    result = np.concatenate([np.full(length - 1, np.nan), conv])  # restore to N

    result = Series(result, index=close.index)

    if offset != 0:
        result = result.shift(offset)

    if "fillna" in kwargs:
        result.fillna(kwargs["fillna"], inplace=True)

    result.name = f"SMA_{length}"
    return result


# --- EMA implementation (no pandas_ta required) ---
def ema(close: Series, length: int = 10, offset: int = 0, **kwargs) -> Series:
    """Exponential Moving Average using pandas ewm."""
    length = max(int(length), 1)
    adjust = kwargs.get("adjust", False)

    result = close.ewm(span=length, adjust=adjust, min_periods=length).mean()

    if offset != 0:
        result = result.shift(offset)

    if "fillna" in kwargs:
        result.fillna(kwargs["fillna"], inplace=True)

    result.name = f"EMA_{length}"
    return result


# --- Download data ---
import yfinance as yf
import datetime as dt

e = dt.datetime.now()
s = e - dt.timedelta(days=5)
print(s, e)
data = yf.download('TSLA', start=s.date(), end=e.date(),
                   multi_level_index=False, interval='5m', ignore_tz=True)
print(data)

data['sma'] = sma(data['Close'], length=20)
print(data)

data['ema'] = ema(data['Close'], length=20)
print(data)

import mplfinance as mpf
s_plot = mpf.make_addplot(data['sma'], color='blue')
e_plot = mpf.make_addplot(data['ema'], color='red')
mpf.plot(data, type='candle', volume=True, style='yahoo', addplot=[s_plot, e_plot])