PROVIDERS = {
    "klaviyomail.com": "Klaviyo",
    "sendgrid.net": "SendGrid",
    "amazonses.com": "Amazon SES",
    "mailgun.org": "Mailgun",
    "mailgun.net": "Mailgun",
    "outlook.com": "Microsoft 365",
    "protection.outlook.com": "Microsoft 365",
    "office365.com": "Microsoft 365",
    "google.com": "Google Workspace",
    "googlemail.com": "Google Workspace",
    "gmail.com": "Gmail",
    "proofpoint.com": "Proofpoint",
    "mimecast.com": "Mimecast",
    "barracuda.com": "Barracuda",
    "messagelabs.com": "Symantec Email Security",
    "icloud.com": "Apple iCloud Mail",
    "yahoodns.net": "Yahoo Mail",
    "yahoo.com": "Yahoo Mail",
    "zoho.com": "Zoho Mail",
}


def detect_provider(received_headers):
    """
    Detect the email service provider from Received headers.
    """

    if not received_headers:
        return {
            "name": "Unknown",
            "confidence": "Low",
            "matched_domain": None,
        }

    headers = " ".join(received_headers).lower()

    for domain, provider in PROVIDERS.items():
        if domain in headers:
            return {
                "name": provider,
                "confidence": "High",
                "matched_domain": domain,
            }

    return {
        "name": "Unknown",
        "confidence": "Low",
        "matched_domain": None,
    }