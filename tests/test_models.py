from src.models import Asset, Vulnerability, Finding


def test_finding_starts_open():
    asset = Asset(
        1,
        "Web Server",
        "192.168.1.10",
        "Ubuntu",
        "High"
    )

    vulnerability = Vulnerability(
        1,
        "CVE-2026-0001",
        "Test Vulnerability",
        "Used for testing",
        7.5,
        "High"
    )

    finding = Finding(
        1,
        asset,
        vulnerability
    )

    assert finding.status == "Open"

def test_close_finding_changes_status_to_closed():
    asset = Asset(
        1,
        "Web Server",
        "192.168.1.10",
        "Ubuntu",
        "High"
    )

    vulnerability = Vulnerability(
        1,
        "CVE-2026-0001",
        "Test Vulnerability",
        "Used for testing",
        7.5,
        "High"
    )

    finding = Finding(
        1,
        asset,
        vulnerability
    )

    finding.close_finding()

    assert finding.status == "Closed"