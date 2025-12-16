
import time
from data_fetcher import fetch_stock_data
from analytics import calculate_metrics
from agent import predict_trend
from report import print_report
from scripts.ml_predictor import run_ml_prediction

STOCK_SYMBOL = "AAPL"
REFRESH_SECONDS = 60
ml_result = run_ml_prediction("AAPL")

print("Stock AI Agent started...")
print("\n MACHINE LEARNING PREDICTION")
print("Predicted Next Day Price:", ml_result["predicted_price"])
print("Model MSE:", ml_result["mse"])

while True:
    data = fetch_stock_data(STOCK_SYMBOL)
    metrics = calculate_metrics(data)
    prediction = predict_trend(metrics)
    print_report(STOCK_SYMBOL, metrics, prediction)

    time.sleep(REFRESH_SECONDS) 
    

    