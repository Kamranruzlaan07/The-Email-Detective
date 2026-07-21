import re


def parse_header(header: str):
    result = {
        "received": [],
        "sender_ips": []
    }

    current_key = None

    for raw_line in header.splitlines():

        # Folded (continued) header
        if raw_line.startswith((" ", "\t")) and current_key:

            if current_key == "received":
                # Append to the last Received header
                if result["received"]:
                    result["received"][-1] += " " + raw_line.strip()

                    # Re-extract IPs from the completed header
                    ips = re.findall(
                        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                        result["received"][-1]
                    )

                    result["sender_ips"] = list(dict.fromkeys(ips + result["sender_ips"]))
            else:
                result[current_key] += " " + raw_line.strip()

            continue

        line = raw_line.strip()

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip().lower()
        value = value.strip()

        current_key = key

        if key == "received":
            result["received"].append(value)

            ips = re.findall(
                r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                value
            )

            result["sender_ips"].extend(ips)

        else:
            result[key] = value

    # Remove duplicate IPs while preserving order
    result["sender_ips"] = list(dict.fromkeys(result["sender_ips"]))

    return result