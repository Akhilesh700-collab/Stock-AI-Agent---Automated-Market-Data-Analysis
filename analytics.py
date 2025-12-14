import pandas as pd

def calculate_rsi(data, window=14):
    delta = data["Close"].diff()

    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return round(rsi.iloc[-1], 2)


def calculate_metrics(data):
    latest = data.iloc[-1]
    previous = data.iloc[-2]

    price = latest["Close"]
    change = price - previous["Close"]
    percent = (change / previous["Close"]) * 100
    volume = latest["Volume"]

    sma_5 = data["Close"].rolling(window=5).mean().iloc[-1]
    rsi = calculate_rsi(data)

    return {
        "price": round(price, 2),
        "change": round(change, 2),
        "percent": round(percent, 2),
        "volume": int(volume),
        "sma_5": round(sma_5, 2),
        "rsi": rsi
    }
    