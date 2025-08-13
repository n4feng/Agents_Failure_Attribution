# filename: check_stock_data.py
import yfinance as yf

# Define the stock symbols and the start date for YTD
stocks = ['NVDA', 'TSLA']
start_date = '2023-01-01'

# Fetch stock data and print the results for each stock
for stock in stocks:
    data = yf.download(stock, start=start_date)
    print(f"Data for {stock}:")
    print(data)
    print("\n")