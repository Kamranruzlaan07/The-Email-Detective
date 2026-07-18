def check_dmarc(headers):
    auth = headers.get("authentication-results", "").lower()

    if "dmarc=pass" in auth:
        return "pass"

    if "dmarc=fail" in auth:
        return "fail"

    return "unknown"