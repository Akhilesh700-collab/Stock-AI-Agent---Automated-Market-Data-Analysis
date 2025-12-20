import pandas as pd
import requests

def get_stock_universe(limit=50):
    """
    Fetch S&P 500 stock symbols dynamically.
    Falls back to a static universe if online fetch fails.
    """

    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        tables = pd.read_html(response.text)
        sp500 = tables[0]
        symbols = sp500["Symbol"].tolist()

        print("Universe fetched dynamically from Wikipedia")
        return symbols[:limit]

    except Exception as e:
        print(" Dynamic fetch failed, using fallback universe")
        print("Reason:", e)

        
        fallback = [
            "AAPL", "MSFT", "AMZN", "GOOGL", "NVDA",
            "META", "TSLA", "JPM", "BAC", "WMT",
            "V", "MA", "DIS", "ADBE", "NFLX",
            "INTC", "CSCO", "ORCL", "IBM", "AMD",
            "QCOM", "PYPL", "COST", "PEP", "KO",
            "T", "VZ", "CRM", "ABNB", "UBER",
            "NKE", "MCD", "SBUX", "LOW", "HD",
            "GE", "CAT", "MMM", "BA", "CVX",
            "XOM", "PFE", "JNJ", "MRK", "ABBV",
            "UNH", "LLY", "TMO", "AVGO"
        ]

        return fallback[:limit]

if __name__ == "__main__":
    stocks = get_stock_universe()
    print("\nTotal stocks:", len(stocks))
    print("Sample stocks:", stocks[:10])

