# import yfinance as yf
# import pandas as pd 
# import numpy as np 
# from datetime import datetime 
# import time
# TICKERS=["AAPL","MSFT","GOOGL"]
# def fetch_stock_data(ticker):
#   """Fetch latest stock data from Yahoo Finance."""
#   data=yf.Ticker(ticker).history(period="1d")
#   if data.empty:
#     return None
#   close_price=data['Close'].iloc[-1]
#   volume=data['Volume'].iloc[-1]
#   return{
#     "ticker":ticker,
#     "price":float(close_price),
#     "volume":int(volume),
#     "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#   }
# def print_summary():
#   """Fetch & print stock summary for each ticker."""
#   print("="*60)
#   print(f"Run at: {datetime.now()}")
#   print("="*60)
#   for ticker in TICKERS:
#     info=fetch_stock_data(ticker)
#     if info:
#       print(
#         f"{info['timestamp']}|{info['ticker']}|"
#         f"Price:{info['price']}|Volume:{info['volume']}"
#       )
#     else:
#       print(f"Failed to fetch data for {ticker}")
#   print("="*60)
# def run_loop(interval_seconds=60):
#   """Run the data fetch repeatedly at a given interval."""
#   while True:
#     print_summary()
#     time.sleep(interval_seconds)
# if __name__=="__main__":
#   run_loop(interval_seconds=60)

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import time

# List of stocks to fetch
TICKERS = ["AAPL", "MSFT", "GOOGL"]


# -----------------------------
# Indicator Calculations
# -----------------------------
def calculate_sma(series, window):
    if len(series) < window:
        return None
    return series.rolling(window=window).mean().iloc[-1]


def calculate_rsi(series, period=14):
    delta = series.diff()

    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]


# -----------------------------
# Generate Buy / Sell / Hold Signal
# -----------------------------
def generate_signal(close_prices):
    sma20 = calculate_sma(close_prices, 20)
    sma50 = calculate_sma(close_prices, 50)
    rsi = calculate_rsi(close_prices, 14)

    if sma20 is None or sma50 is None or rsi is None:
        return "Not enough data", sma20, sma50, rsi

    # Buy signals
    if sma20 > sma50 and rsi < 60:
        return "BUY", sma20, sma50, rsi

    # Sell signals
    if sma20 < sma50 or rsi > 70:
        return "SELL", sma20, sma50, rsi

    # Otherwise hold
    return "HOLD", sma20, sma50, rsi


# -----------------------------
# Fetch Stock Data
# -----------------------------
def fetch_stock_data(ticker):
    data = yf.Ticker(ticker).history(period="90d")  # get enough history for SMA50
    if data.empty:
        return None

    close_prices = data["Close"]

    latest_close = close_prices.iloc[-1]
    volume = data["Volume"].iloc[-1]

    signal, sma20, sma50, rsi = generate_signal(close_prices)

    return {
        "ticker": ticker,
        "price": float(latest_close),
        "volume": int(volume),
        "sma20": sma20,
        "sma50": sma50,
        "rsi": rsi,
        "signal": signal,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# -----------------------------
# Print Summary
# -----------------------------
def print_summary():
    print("=" * 80)
    print(f"Run at: {datetime.now()}")
    print("=" * 80)

    for ticker in TICKERS:
        info = fetch_stock_data(ticker)

        if info:
            print(
                f"{info['timestamp']} | {info['ticker']} | "
                f"Price: {info['price']:.2f} | "
                f"SMA20: {info['sma20']:.2f} | SMA50: {info['sma50']:.2f} | "
                f"RSI: {info['rsi']:.1f} | "
                f"Signal → {info['signal']}"
            )
        else:
            print(f"Failed to fetch data for {ticker}")

    print("=" * 80)


# -----------------------------
# Looping Function
# -----------------------------
def run_loop(interval_seconds=60):
    while True:
        print_summary()
        time.sleep(interval_seconds)


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    run_loop(interval_seconds=60)

