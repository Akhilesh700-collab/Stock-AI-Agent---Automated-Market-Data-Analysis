from scripts.universe import get_stock_universe
from scripts.stock_selector import auto_select_stocks
from scripts.ml_predictor import run_ml_prediction
from scripts.signal_engine import generate_signal
from scripts.report_writer import save_report

def run_agent():
    universe = get_stock_universe(limit=50)
    trade_candidates = auto_select_stocks(universe, top_n=10)

    print("\n✅ Selected stocks for analysis:", trade_candidates)

    for symbol in trade_candidates:
        ml_result = run_ml_prediction(symbol)

        if ml_result is None:
            continue

        signal_data = generate_signal(
            ml_result["current_price"],
            ml_result["predicted_price"]
        )

        save_report(
            symbol=ml_result["symbol"],
            current_price=ml_result["current_price"],
            predicted_price=ml_result["predicted_price"],
            signal=signal_data["signal"],
            confidence=signal_data["confidence"]
        )

        print(
            f"📌 {symbol} → {signal_data['signal']} "
            f"(Confidence: {signal_data['confidence']}%)"
        )

if __name__ == "__main__":
    run_agent()
