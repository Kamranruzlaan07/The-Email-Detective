from app.modules.header_parser import parse_header
from app.modules.spf_checker import check_spf
from app.modules.dkim_checker import check_dkim
from app.modules.dmarc_checker import check_dmarc
from app.modules.risk_engine import calculate_risk
from app.modules.geo_locator import lookup_ip


def build_report(header: str):
    parsed = parse_header(header)

    report = {
        "headers": {
            "from": parsed.get("from"),
            "to": parsed.get("to"),
            "subject": parsed.get("subject"),
            "date": parsed.get("date"),
            "received": parsed.get("received", [])
        },
        "sender_ips": parsed.get("sender_ips", []),
        "authentication": {
            "spf": check_spf(parsed),
            "dkim": check_dkim(parsed),
            "dmarc": check_dmarc(parsed)
        }
    }

    report["risk"] = calculate_risk(report)

    report["geo"] = [
        lookup_ip(ip)
        for ip in report["sender_ips"]
    ]

    return report