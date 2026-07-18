import re


def parse_header(header: str):
    result = {
        "received": [],
        "sender_ips": []
    }

    lines = header.split("\n")

    for line in lines:
        line = line.strip()

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip().lower()
        value = value.strip()

        if key == "received":
            result["received"].append(value)

            ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", value)
            result["sender_ips"].extend(ips)

        else:
            result[key] = value

    return result