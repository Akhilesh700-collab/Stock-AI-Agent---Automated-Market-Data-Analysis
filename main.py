
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
    

    