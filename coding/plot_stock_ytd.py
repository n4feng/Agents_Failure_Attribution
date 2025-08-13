# filename: plot_stock_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the stock symbols and the start date for YTD
stocks = ['NVDA', 'TSLA']
start_date = '2023-01-01'

# Fetch stock data
data = yf.download(stocks, start=start_date)

# Check if data is fetched correctly
if data.isnull().values.all():
    print("Failed to get data. Please check the ticker symbols or data source.")
else:
    data = data['Close']  # We are only interested in the closing prices

    # Calculate YTD price change
    ytd_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100

    # Plotting the results
    plt.figure(figsize=(10, 5))
    ytd_change.plot(kind='bar', color=['blue', 'orange'])
    plt.title("YTD Price Change for NVDA and TSLA")
    plt.ylabel("Percentage Change (%)")
    plt.xticks(ticks=range(len(stocks)), labels=stocks, rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()