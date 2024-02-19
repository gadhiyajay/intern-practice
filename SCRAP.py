import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period="1d")
    return todays_data['Close'][0]

ticker = "AAPL" # Apple stock
price = get_stock_price(ticker)
print(f"The current price of {ticker} is ${price:.2f}")