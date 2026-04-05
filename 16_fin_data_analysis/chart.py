
# yfinance + mplfinance example
import datetime as dt
import sys

try:
	import yfinance as yf
	import pandas as pd
	import matplotlib.pyplot as plt
	import matplotlib.dates as mdates
	import matplotlib.patches as patches
except Exception as e:
	print("Missing dependencies:", e)
	print("Install requirements with: python -m pip install -r requirements.txt")
	sys.exit(1)


def fetch_data(ticker='TSLA', days=3, interval='1m'):
	e = dt.datetime.now()
	s = e - dt.timedelta(days=days)
	df = yf.download(ticker, start=s, end=e, interval=interval, progress=False, ignore_tz=True, multi_level_index=False)
	if df.empty:
		print('No data downloaded for', ticker)
		return df
	df.index = pd.to_datetime(df.index)
	return df


def plot_candles(df, title='TSLA'):
	if df.empty:
		return

	df = df.copy()
	df.index = pd.to_datetime(df.index)

	# Prepare figure with volume subplot
	fig, (ax, ax_vol) = plt.subplots(
		2, sharex=True, gridspec_kw={'height_ratios': [3, 1]}, figsize=(12, 6)
	)

	# compute bar width in days for date axis
	if len(df.index) > 1:
		delta = (df.index[1] - df.index[0]).total_seconds() / (24 * 3600)
		width = delta * 0.8
	else:
		width = 0.0008

	xs = mdates.date2num(df.index.to_pydatetime())

	for x, row in zip(xs, df.itertuples(index=False, name='Row')):
		o, h, l, c = row.Open, row.High, row.Low, row.Close
		color = 'green' if c >= o else 'red'
		# vertical line
		ax.vlines(x, l, h, color='k', linewidth=0.5)
		# rectangle for open-close
		bottom = o if c >= o else c
		rect = patches.Rectangle((x - width / 2, bottom), width, float(abs(c - o)), facecolor=color, edgecolor='k')
		ax.add_patch(rect)

	# volume bars
	volumes = df['Volume'].values
	vol_colors = ['green' if c >= o else 'red' for o, c in zip(df['Open'].values, df['Close'].values)]
	ax_vol.bar(xs, volumes, width=width, color=vol_colors, align='center')

	# formatting
	ax.set_title(title)
	ax.grid(True, linewidth=0.3)
	ax_vol.set_ylabel('Volume')

	ax.xaxis_date()
	ax.xaxis.set_major_locator(mdates.AutoDateLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
	plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

	plt.tight_layout()
	plt.show()


def main():
	df = fetch_data()
	print(df.tail())
	plot_candles(df)


if __name__ == '__main__':
	main()
