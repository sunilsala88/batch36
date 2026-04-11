#talib C++->python #fast #difficult to install
#pandasta #pure python #easy to install #slower than talib #update
#ta #less indicator

#problem when you install old library


#yfinance
import yfinance as yf
import datetime as dt

e=dt.datetime.now()
s=e-dt.timedelta(days=5)
print(s,e)
data=yf.download('TSLA',start=s.date(),end=e.date(),multi_level_index=False,interval='5m',ignore_tz=True)

print(data)

import pandas_ta as ta

sma=ta.sma(data['Close'], length=20)
data['sma']=sma
print(data)

ema=ta.ema(data['Close'], length=20)
data['ema']=ema
print(data)

import mplfinance as mpf
s=mpf.make_addplot(data['sma'],color='blue')
e=mpf.make_addplot(data['ema'],color='red')
mpf.plot(data,type='candle',volume=True,style='yahoo',addplot=[s,e])