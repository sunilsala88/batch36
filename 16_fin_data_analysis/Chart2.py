

# yfinance -> fetch data and plot interactive candlestick with Plotly
import yfinance as yf
import datetime as dt
import plotly.graph_objects as go

def fetch_and_plot(ticker='TSLA', days=5, interval='1m', out_html=None):
	e = dt.datetime.now()
	s = e - dt.timedelta(days=1000)
	print('Downloading', ticker, 'from', s, 'to', e)
	data = yf.download(ticker, start=s, end=e, multi_level_index=False, interval='1d', ignore_tz=True)
	data=data.dropna()
	
	if data is None or data.empty:
		print('No data downloaded for', ticker)
		return

	fig = go.Figure(data=[
		go.Candlestick(
			x=data.index,
			open=data['Open'],
			high=data['High'],
			low=data['Low'],
			close=data['Close'],
			increasing_line_color='green',
			decreasing_line_color='red',
		)
	])

	fig.update_layout(
		title=f"{ticker} {interval} Candlestick",
		xaxis_title='Time',
		yaxis_title='Price',
		xaxis_rangeslider_visible=False,
	)

	if out_html is None:
		out_html = f"{ticker}_candlestick.html"

	fig.write_html(out_html, include_plotlyjs='cdn')
	print('Saved interactive chart to', out_html)

	try:
		fig.show()
	except Exception as e:
		print('Could not open browser preview:', e)


if __name__ == '__main__':
	fetch_and_plot()