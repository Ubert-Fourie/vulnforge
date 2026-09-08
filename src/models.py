from datetime import datetime


class Asset:
    #Represents a device or system being monitored.

    def __init__(
        self,
        asset_id: int,
        name: str,
        ip_address: str,
        operating_system: str,
        criticality: str
    ):
        self.asset_id = asset_id
        self.name = name
        self.ip_address = ip_address
        self.operating_system = operating_system
        self.criticality = criticality

    def __str__(self):
        return (
            f"{self.name} ({self.ip_address}) - "
            f"{self.operating_system} - Criticality: {self.criticality}"
        )


class Vulnerability:
    #Represents a vulnerability that may affect an asset.

    def __init__(
        self,
        vulnerability_id: int,
        cve_id: str,
        name: str,
        description: str,
        cvss_score: float,
        severity: str
    ):
        self.vulnerability_id = vulnerability_id
        self.cve_id = cve_id
        self.name = name
        self.description = description
        self.cvss_score = cvss_score
        self.severity = severity

    def __str__(self):
        return (
            f"{self.cve_id} - {self.name} "
            f"(CVSS: {self.cvss_score}, Severity: {self.severity})"
        )


class Finding:
    #Represents a vulnerability discovered on a specific asset.

    def __init__(
        self,
        finding_id: int,
        asset: Asset,
        vulnerability: Vulnerability,
        status: str = "Open"
    ):
        self.finding_id = finding_id
        self.asset = asset
        self.vulnerability = vulnerability
        self.status = status
        self.discovered_at = datetime.now()

    def close_finding(self):
        self.status = "Closed"

    def __str__(self):
        return (
            f"Finding {self.finding_id}: "
            f"{self.vulnerability.cve_id} on {self.asset.name} "
            f"- Status: {self.status}"
        )
