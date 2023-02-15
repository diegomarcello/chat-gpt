import yfinance as yf
import pandas as pd

# Define the list of stocks you want to monitor
stock_list = ['AAPL', 'GOOG', 'AMZN']

# Define the time period for which you want to retrieve the stock data (in this case, 1 year)
start_date = '2022-02-14'
end_date = '2023-02-14'

# Retrieve the stock data using the yfinance library
data = yf.download(stock_list, start=start_date, end=end_date)

# Calculate the daily returns of the stocks
returns = data['Adj Close'].pct_change()

# Calculate the daily volatility of the stocks (standard deviation of the returns)
volatility = returns.std()

# Calculate the annualized volatility of the stocks (multiply daily volatility by sqrt(252))
annual_volatility = volatility * (252 ** 0.5)

# Calculate the portfolio volatility for an equal-weighted portfolio
portfolio_volatility = annual_volatility.mean()

# Define the risk limit for the portfolio (in this case, 15%)
risk_limit = 0.15

# Calculate the maximum allowed portfolio value to stay within the risk limit
portfolio_value_limit = portfolio_volatility * risk_limit

# Retrieve the latest stock prices to calculate the portfolio value
latest_data = yf.download(stock_list, period='1d')
latest_prices = latest_data['Adj Close']
portfolio_value = latest_prices.sum()

# Check if the portfolio value is within the risk limit
if portfolio_value > portfolio_value_limit:
    print('WARNING: Portfolio value exceeds risk limit. Current value: ${:.2f}, Maximum allowed value: ${:.2f}'.format(portfolio_value, portfolio_value_limit))
else:
    print('Portfolio value within risk limit. Current value: ${:.2f}, Maximum allowed value: ${:.2f}'.format(portfolio_value, portfolio_value_limit))
