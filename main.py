# print("main.py has started")
# import pandas as pd 
# import yfinance as yf
# import time
# from datetime import datetime
# STOCK_SYMBOL="TCS"
# def fetch_stock_data(symbol):
#   print("Fetching stock data...")
#   stock=yf.Ticker(symbol)
#   data=stock.history(period="7d",interval="1d")
#   print("stock data fetched")
#   return data
# def calculate_metrics(data):
#   print("Calculating metrics...")
#   latest=data.iloc[-1]
#   previous=data.iloc[-2]
#   current_price=latest["Close"]
#   price_change=current_price-previous["Close"]
#   percent_change=(price_change/previous["Close"])*100
#   volume=latest["Volume"]
#   return{
#     "current_price":round(current_price, 2),
#     "price_change":round(price_change, 2),
#     "percent_change":round(percent_change, 2),
#     "volume": int(volume)
#  }
# # def predict_trend(metrics):
# #   if metrics["current_price"]>metrics["sma_5"]:
# #     return "Bullish(Price above 5-day moving average)"
# #   else:
# #      return "Bearish(Price below 5-day moving average)"
# def generate_report():
#   print("\n==============")
#   print("DAILY STOCK REPORT")
#   print("================")
#   print(f"Time: {datetime.now()}")
#   print(f"Stock: {STOCK_SYMBOL}")
#   data=fetch_stock_data(STOCK_SYMBOL)
#   metrics=calculate_metrics(data)
#   print(f"Current Price: ${metrics['current_price']}")
#   print(f"Price Change: {metrics['price_change']} ({metrics['percent_change']}%)")
#   print(f"Volume: {metrics['volume']}")
#   print("===================\n")
#   # d
#   print("Starting report generation...")
#   generate_report()
#   print("Program finished successfully")
      
# print("STEP1: Program started")
# import yfinance as yf
# print("STEP2: yfinance imported successfully")
# print("STEP1: Program started")
# import yfinance as yf
# print("STEP2: Fetching stock info")
# ticker=yf.Ticker("AAPL")
# info=ticker.history(period="id")
# print("STEP3: Data received")
# print(info)
# import yfinance as yf
# from datetime import datetime

# print("Program started")

# data = yf.Ticker("AAPL").history(period="5d")

# latest = data.iloc[-1]
# previous = data.iloc[-2]

# price = latest["Close"]
# change = price - previous["Close"]

# print("Time:", datetime.now())
# print("Price:", round(price, 2))
# # print("Change:", round(change, 2))
# import yfinance as yf
# from datetime import datetime
# import time

# STOCK_SYMBOL = "AAPL"
# REFRESH_SECONDS = 60   # runs every 1 minute


# def fetch_stock_data(symbol):
#     stock = yf.Ticker(symbol)
#     return stock.history(period="5d")


# def calculate_metrics(data):
#     latest = data.iloc[-1]
#     previous = data.iloc[-2]

#     price = latest["Close"]
#     change = price - previous["Close"]
#     percent = (change / previous["Close"]) * 100
#     volume = latest["Volume"]

#     sma_5 = data["Close"].rolling(window=5).mean().iloc[-1]

#     return price, change, percent, volume, sma_5


# def predict_trend(price, sma):
#     if price > sma:
#         return "Bullish (price above 5-day moving average)"
#     else:
#         return "Bearish (price below 5-day moving average)"


# def generate_report():
#     print("\n==============================")
#     print("DAILY STOCK REPORT")
#     print("==============================")
#     print("Time:", datetime.now())
#     print("Stock:", STOCK_SYMBOL)

#     data = fetch_stock_data(STOCK_SYMBOL)
#     price, change, percent, volume, sma = calculate_metrics(data)
#     trend = predict_trend(price, sma)

#     print("Current Price:", round(price, 2))
#     print("Change:", round(change, 2), f"({round(percent,2)}%)")
#     print("Volume:", int(volume))
#     print("5-Day SMA:", round(sma, 2))
#     print("Prediction:", trend)
#     print("==============================\n")


# print("Stock AI Agent started...")
# generate_report()

# while True:
#     time.sleep(REFRESH_SECONDS)
#     generate_report()
    
import time
from data_fetcher import fetch_stock_data
from analytics import calculate_metrics
from agent import predict_trend
from report import print_report

STOCK_SYMBOL = "AAPL"
REFRESH_SECONDS = 60

print("Stock AI Agent started...")

while True:
    data = fetch_stock_data(STOCK_SYMBOL)
    metrics = calculate_metrics(data)
    prediction = predict_trend(metrics)
    print_report(STOCK_SYMBOL, metrics, prediction)

    time.sleep(REFRESH_SECONDS) 
    