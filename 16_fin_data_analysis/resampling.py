
#yfinance
import yfinance as yf
import datetime as dt

e=dt.datetime.now()
s=e-dt.timedelta(days=5)
print(s,e)
data=yf.download('TSLA',start=s.date(),end=e.date(),multi_level_index=False,interval='1m',ignore_tz=True)

print(data)
df_5min = data.resample('15min').agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last',
    'Volume': 'sum'
}).dropna()
print(df_5min.tail(50))


import mplfinance as mpf
mpf.plot(df_5min,type='candle',style='yahoo')