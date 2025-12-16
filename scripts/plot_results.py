import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)


symbol = "AAPL"
data = yf.download(symbol, period="3mo")

data["SMA_5"] = data["Close"].rolling(5).mean()
data["SMA_20"] = data["Close"].rolling(20).mean()

plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close Price")
plt.plot(data["SMA_5"], label="SMA 5")
plt.plot(data["SMA_20"], label="SMA 20")

plt.title(f"{symbol} Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

file_path = os.path.join(RESULTS_DIR, "price_trend.png")

plt.savefig(file_path, dpi=150, bbox_inches="tight")
plt.close()

print(f" Image successfully saved at: {file_path}")
