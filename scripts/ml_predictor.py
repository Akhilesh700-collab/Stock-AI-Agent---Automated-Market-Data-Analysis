import yfinance as yf
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def run_ml_prediction(symbol):
    print(f"\n🔍 Fetching data for {symbol}")

    data = yf.download(symbol, period="1y", progress=False)

    if data.empty or len(data) < 50:
        print(f"⚠️ Not enough data for {symbol}")
        return None

    data["Return"] = data["Close"].pct_change()
    data.dropna(inplace=True)

    X = np.arange(len(data)).reshape(-1, 1)
    y = data["Close"].values.ravel() 
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    predicted_price = model.predict([[len(data)]])[0]
    current_price = data["Close"].iloc[-1]

    return {
        "symbol": symbol,
        "current_price": round(float(current_price), 2),
        "predicted_price": round(float(predicted_price), 2)
    }

 
