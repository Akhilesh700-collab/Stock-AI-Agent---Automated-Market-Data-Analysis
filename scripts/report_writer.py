import csv
from datetime import datetime
import os

REPORT_FILE = "reports/daily_report.csv"

def save_report(symbol, current_price, predicted_price, signal, confidence):
    os.makedirs("reports", exist_ok=True)

    file_exists = os.path.isfile(REPORT_FILE)

    with open(REPORT_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "symbol",
                "current_price",
                "predicted_price",
                "signal",
                "confidence"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            symbol,
            current_price,
            predicted_price,
            signal,
            confidence
        ])
