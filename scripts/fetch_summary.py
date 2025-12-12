import yfinance as yf
import pandas as pd 
import numpy as np 
from datetime import datetime 
import time
TICKERS=["AAPL","MSFT","GOOGL"]
def fetch_stock_data(ticker):
  """Fetch latest stock data from Yahoo Finance."""
  data=yf.Ticker(ticker).history(period="1d")
  if data.empty:
    return None
  close_price=data['Close'].iloc[-1]
  volume=data['Volume'].iloc[-1]
  return{
    "ticker":ticker,
    "price":float(close_price),
    "volume":int(volume),
    "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
def print_summary():
  """Fetch & print stock summary for each ticker."""
  print("="*60)
  print(f"Run at: {datetime.now()}")
  print("="*60)
  for ticker in TICKERS:
    info=fetch_stock_data(ticker)
    if info:
      print(
        f"{info['timestamp']}|{info['ticker']}|"
        f"Price:{info['price']}|Volume:{info['volume']}"
      )
    else:
      print(f"Failed to fetch data for {ticker}")
  print("="*60)
def run_loop(interval_seconds=60):
  """Run the data fetch repeatedly at a given interval."""
  while True:
    print_summary()
    time.sleep(interval_seconds)
if __name__=="__main__":
  run_loop(interval_seconds=60)
  
