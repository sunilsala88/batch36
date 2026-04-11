import yfinance as yf
import datetime as dt

e=dt.datetime.now()
s=e-dt.timedelta(days=2000)
print(s,e)
data=yf.download('TSLA',start=s,end=e,multi_level_index=False,interval='1d',ignore_tz=True )
print(data)

data['sma']=data['Close'].rolling(window=20).mean()

import mplfinance as mpf
mpf.plot(data,type='candle',volume=True,style='yahoo',addplot=mpf.make_addplot(data['sma'],color='blue'))


#talib
#pandasta
#ta