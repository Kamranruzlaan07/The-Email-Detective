from app.modules.header_parser import parse_header
from app.modules.spf_checker import check_spf
from app.modules.dkim_checker import check_dkim
from app.modules.dmarc_checker import check_dmarc
from app.modules.risk_engine import calculate_risk
from app.modules.geo_locator import locate_ips
from app.modules.route_parser import parse_route
from app.modules.provider_detector import detect_provider
from app.modules.trust_engine import calculate_trust


def build_report(raw_headers: str):
    parsed = parse_header(raw_headers)

    authentication = {
        "spf": check_spf(parsed),
        "dkim": check_dkim(parsed),
        "dmarc": check_dmarc(parsed),
    }

    risk = calculate_risk(authentication)

    provider = detect_provider(parsed.get("received", []))

    report = {
        "headers": parsed,
        "sender_ips": parsed.get("sender_ips", []),
        "authentication": authentication,
        "risk": risk,
        "geo": locate_ips(parsed.get("sender_ips", [])),
        "route": parse_route(parsed.get("received", [])),
        "provider": provider,
    }

    # Calculate overall trust score
    report["trust"] = calculate_trust(report)

    return report