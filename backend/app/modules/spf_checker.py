def check_spf(headers):
    auth = headers.get("authentication-results", "").lower()

    if "spf=pass" in auth:
        return "pass"

    if "spf=fail" in auth:
        return "fail"

    return "unknown"