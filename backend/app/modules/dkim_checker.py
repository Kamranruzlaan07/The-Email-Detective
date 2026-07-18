def check_dkim(headers):
    auth = headers.get("authentication-results", "").lower()

    if "dkim=pass" in auth:
        return "pass"

    if "dkim=fail" in auth:
        return "fail"

    return "unknown"