import ipaddress


def filter_public_ips(ip_list):
    """
    Return only valid public IPv4 addresses.
    Removes duplicates while preserving order.
    """

    valid_ips = []
    seen = set()

    for ip in ip_list:
        try:
            addr = ipaddress.ip_address(ip)

            if (
                addr.version == 4
                and not addr.is_private
                and not addr.is_loopback
                and not addr.is_link_local
                and not addr.is_multicast
                and not addr.is_reserved
                and ip not in seen
            ):
                valid_ips.append(ip)
                seen.add(ip)

        except ValueError:
            # Ignore invalid IPs
            continue

    return valid_ips