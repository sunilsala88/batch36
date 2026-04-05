from finvizfinance.screener.overview import Overview

foverview = Overview()
filters_dict = {'Exchange':"NASDAQ",'Index':'NASDAQ 100','Sector':'Energy'}
foverview.set_filter(filters_dict=filters_dict)
df = foverview.screener_view()
print(df.head())
print(df['Ticker'].tolist())