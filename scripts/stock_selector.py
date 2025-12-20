import yfinance as yf
import pandas as pd

def auto_select_stocks(stock_list, top_n=10):
    selected = []

    for symbol in stock_list:
        try:
            data = yf.download(
                symbol,
                period="3mo",
                interval="1d",
                progress=False
            )

            if data.empty or len(data) < 30:
                continue

            avg_volume = float(data["Volume"].mean())
            volatility = float(data["Close"].pct_change().std())
            momentum = float(
                (data["Close"].iloc[-1] / data["Close"].iloc[0]) - 1
            )

            selected.append({
                "symbol": symbol,
                "volume": avg_volume,
                "volatility": volatility,
                "momentum": momentum
            })

        except Exception:
            continue

    df = pd.DataFrame(selected)

    print(f"\n📊 Total stocks analyzed: {len(df)}")
    print("📈 Sample analyzed stocks:", df["symbol"].head(10).tolist())

    # 🔥 FORCE NUMERIC TYPES (CRITICAL FIX)
    df["volume"] = pd.to_numeric(df["volume"], errors="coerce")
    df["momentum"] = pd.to_numeric(df["momentum"], errors="coerce")
    df["volatility"] = pd.to_numeric(df["volatility"], errors="coerce")

    # Remove invalid rows
    df.dropna(inplace=True)

    # 🔥 SAFE FILTER
    df = df[df["volume"] > 300_000]

    # Rank stocks instead of eliminating all
    df = df.sort_values(
        by=["momentum", "volatility"],
        ascending=False
    )

    return df.head(top_n)["symbol"].tolist()
