def generate_signal(current_price, predicted_price):
    diff_pct = (predicted_price - current_price) / current_price

    if diff_pct >= 0.03:
        signal = "BUY"
    elif diff_pct <= -0.03:
        signal = "SELL"
    else:
        signal = "HOLD"

    confidence = round(abs(diff_pct) * 100, 2)

    return {
        "signal": signal,
        "confidence": confidence
    }
