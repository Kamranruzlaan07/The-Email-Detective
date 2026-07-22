import re


def parse_route(received_headers):
    """
    Parse all Received headers into an ordered mail route.
    """

    if isinstance(received_headers, str):
        received_headers = [received_headers]

    route = []

    for index, header in enumerate(received_headers, start=1):

        ip_match = re.search(r"\[([\d\.]+)\]", header)

        host_match = re.search(
            r"from\s+([^\s\(]+)",
            header,
            re.IGNORECASE,
        )

        route.append(
            {
                "hop": index,
                "host": host_match.group(1) if host_match else "Unknown",
                "ip": ip_match.group(1) if ip_match else None,
            }
        )

    return route