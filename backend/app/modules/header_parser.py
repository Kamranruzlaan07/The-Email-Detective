import re
from email.header import decode_header

from app.modules.ip_validator import filter_public_ips


def decode_mime(value: str) -> str:
    """
    Decode RFC 2047 MIME-encoded email headers.
    Example:
    =?UTF-8?Q?Hello_=F0=9F=91=8B?=
    ->
    Hello 👋
    """

    if not value:
        return value

    try:
        decoded_parts = decode_header(value)
        decoded = ""

        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                decoded += part.decode(
                    encoding or "utf-8",
                    errors="replace"
                )
            else:
                decoded += part

        return decoded

    except Exception:
        return value


def parse_header(header: str):
    result = {
        "received": [],
        "sender_ips": []
    }

    current_key = None

    for raw_line in header.splitlines():

        # Handle folded (continued) headers
        if raw_line.startswith((" ", "\t")) and current_key:

            if current_key == "received":
                if result["received"]:
                    result["received"][-1] += " " + raw_line.strip()

                    ips = re.findall(
                        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                        result["received"][-1]
                    )

                    result["sender_ips"].extend(ips)

            else:
                result[current_key] += " " + raw_line.strip()

            continue

        line = raw_line.strip()

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip().lower()
        value = value.strip()

        # Decode MIME-encoded subjects
        if key == "subject":
            value = decode_mime(value)

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

    # Keep only valid public IPv4 addresses
    result["sender_ips"] = filter_public_ips(
        result["sender_ips"]
    )

    return result