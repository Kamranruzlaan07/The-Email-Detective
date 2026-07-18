def calculate_risk(report):
    score = 0
    reasons = []

    auth = report.get("authentication", {})

    if auth.get("spf") == "fail":
        score += 30
        reasons.append("SPF failed")

    if auth.get("dkim") == "fail":
        score += 30
        reasons.append("DKIM failed")

    if auth.get("dmarc") == "fail":
        score += 40
        reasons.append("DMARC failed")

    if score == 0:
        level = "Low"
    elif score <= 30:
        level = "Medium"
    elif score <= 60:
        level = "High"
    else:
        level = "Critical"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }