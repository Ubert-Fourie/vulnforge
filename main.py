from src.models import Asset, Vulnerability, Finding


# Create an asset
asset = Asset(
    1,
    "Web Server",
    "192.168.1.10",
    "Ubuntu Linux",
    "High"
)

# Create a vulnerability
vulnerability = Vulnerability(
    1,
    "CVE-2026-0001",
    "Example Vulnerability",
    "Example vulnerability used for testing VulnForge.",
    8.5,
    "High"
)

# Create a finding that connects the vulnerability to the asset
finding = Finding(
    1,
    asset,
    vulnerability
)


# Display the objects
print("---VulnForge---")
print()

print("Asset:")
print(asset)
print()

print("Vulnerability:")
print(vulnerability)
print()

print("Finding:")
print(finding)
print()


# Close the finding
print("Closing finding...")
finding.close_finding()

print()
print("Updated Finding:")
print(finding)

#placeholder code for future implementation of the CLI