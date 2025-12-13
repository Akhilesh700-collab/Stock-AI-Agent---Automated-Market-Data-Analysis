# def predict_trend(metrics):
#     if metrics["price"] > metrics["sma_5"]:
#         return "Bullish (price above 5-day SMA)"
#     else:
#         return "Bearish (price below 5-day SMA)"
def predict_trend(metrics):
    price = metrics["price"]
    sma = metrics["sma_5"]
    rsi = metrics["rsi"]

    if rsi > 70:
        return "Overbought (RSI > 70) → Possible price correction"
    elif rsi < 30:
        return "Oversold (RSI < 30) → Possible upward movement"
    elif price > sma:
        return "Bullish (Price above 5-day SMA)"
    else:
        return "Bearish (Price below 5-day SMA)"
        