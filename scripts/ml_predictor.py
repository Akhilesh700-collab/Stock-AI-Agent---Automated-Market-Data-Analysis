import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import os

def run_ml_prediction(symbol="AAPL"):
    data = yf.download(symbol, period="1y")

    data["Return"] = data["Close"].pct_change()
    data["SMA_5"] = data["Close"].rolling(5).mean()
    data["SMA_20"] = data["Close"].rolling(20).mean()

    data.dropna(inplace=True)

    X = data[["Return", "SMA_5", "SMA_20"]]
    y = data["Close"]

  
    split = int(len(data) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

  
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    latest_features = X.iloc[-1].values.reshape(1, -1)
    next_day_price = model.predict(latest_features)[0]

    return {
        "symbol": symbol,
        "mse": round(mse, 2),
        "predicted_price": round(next_day_price, 2)
    }


if __name__ == "__main__":
    result = run_ml_prediction("AAPL")
    print(" ML Prediction Result")
    print(result)
