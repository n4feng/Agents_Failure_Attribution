# filename: fetch_stock_alpha_vantage.py
import requests
import matplotlib.pyplot as plt
import pandas as pd

# Alpha Vantage configuration
API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'  # Replace with your actual API key
stocks = ['NVDA', 'TSLA']
start_date = '2023-01-01'
year = 2023

# Function to fetch stock data
def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=full'
    response = requests.get(url)
    data = response.json()
    return data

# Fetch data and process it
ytd_change = {}
for stock in stocks:
    data = fetch_stock_data(stock)
    time_series = data.get('Time Series (Daily)', {})
    
    # Filter data for the specified year and save closing prices
    closing_prices = {}
    for date, values in time_series.items():
        if date.startswith(str(year)):
            closing_prices[date] = float(values['4. close'])

    # Calculate YTD change
    if closing_prices:
        first_price = closing_prices[list(closing_prices.keys())[-1]]
        last_price = closing_prices[list(closing_prices.keys())[0]]
        ytd_change[stock] = ((last_price - first_price) / first_price) * 100

# Plotting results
plt.figure(figsize=(10, 5))
pd.Series(ytd_change).plot(kind='bar', color=['blue', 'orange'])
plt.title("YTD Price Change for NVDA and TSLA")
plt.ylabel("Percentage Change (%)")
plt.xticks(ticks=range(len(ytd_change)), labels=ytd_change.keys(), rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()