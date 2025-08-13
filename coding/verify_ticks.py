# filename: verify_ticks.py
import yfinance as yf

# Define the stock symbols
stocks = ['NVDA', 'TSLA']

# Fetch stock info and print
for stock in stocks:
    ticker = yf.Ticker(stock)
    info = ticker.info
    print(f"Information for {stock}:")
    print(info)
    print("\n")