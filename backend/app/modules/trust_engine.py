def calculate_trust(report):
    """
    Calculate an overall trust score (0-100)
    based on authentication, provider recognition,
    routing, and risk assessment.
    """

    score = 0
    reasons = []

    # SPF
    if report["authentication"]["spf"] == "pass":
        score += 20
        reasons.append("SPF passed")

    # DKIM
    if report["authentication"]["dkim"] == "pass":
        score += 20
        reasons.append("DKIM passed")

    # DMARC
    if report["authentication"]["dmarc"] == "pass":
        score += 20
        reasons.append("DMARC passed")

    # Provider Detection
    if report["provider"]["name"] != "Unknown":
        score += 10
        reasons.append(f"Recognized provider ({report['provider']['name']})")

    # Public Route
    if len(report.get("sender_ips", [])) > 0:
        score += 10
        reasons.append("Public sender route detected")

    # Risk Level
    risk = report["risk"]["level"].lower()

    if risk == "low":
        score += 20
        reasons.append("Low risk assessment")
    elif risk == "medium":
        score += 10
        reasons.append("Medium risk assessment")

    # Rating
    if score >= 90:
        rating = "Excellent"
        stars = 5
    elif score >= 75:
        rating = "Good"
        stars = 4
    elif score >= 60:
        rating = "Fair"
        stars = 3
    elif score >= 40:
        rating = "Poor"
        stars = 2
    else:
        rating = "Very Poor"
        stars = 1

    return {
        "score": score,
        "rating": rating,
        "stars": stars,
        "reasons": reasons,
    }