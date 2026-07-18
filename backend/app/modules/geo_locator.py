import requests


def lookup_ip(ip):
    url = f"http://ip-api.com/json/{ip}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") != "success":
            return {
                "ip": ip,
                "country": "Unknown",
                "city": "Unknown",
                "isp": "Unknown"
            }

        return {
            "ip": ip,
            "country": data.get("country"),
            "city": data.get("city"),
            "isp": data.get("isp")
        }

    except Exception:
        return {
            "ip": ip,
            "country": "Unknown",
            "city": "Unknown",
            "isp": "Unknown"
        }