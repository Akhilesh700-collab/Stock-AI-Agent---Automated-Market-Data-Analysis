from datetime import datetime

def print_report(symbol, metrics, prediction):
    print("\n==============================")
    print("DAILY STOCK REPORT")
    print("==============================")
    print("Time:", datetime.now())
    print("Stock:", symbol)
    print("Current Price:", metrics["price"])
    print("Change:", metrics["change"], f"({metrics['percent']}%)")
    print("Volume:", metrics["volume"])
    print("5-Day SMA:", metrics["sma_5"])
    print("RSI:", metrics["rsi"])
    print("Prediction:", prediction)
    print("==============================\n")
    