import yfinance as yf

def fetch_stock_data(symbol, period="5d"):
    stock = yf.Ticker(symbol)
    return stock.history(period=period)
    