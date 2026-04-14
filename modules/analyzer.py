def analyze_vulnerabilities(found_ports):
    """
    Checks found banners against a database of known vulnerable versions.
    """
    # Simple 'Signature' Database
    # In a real tool, this would connect to an API like CVE Details or NIST
    VULN_DB = {
        "vsFTPd 2.3.4": "CRITICAL - Backdoor Command Execution (CVE-2011-2523)",
        "OpenSSH 4.7p1": "HIGH - Outdated version, potential for user enumeration",
        "Apache/2.2.8": "MEDIUM - Outdated version, multiple known vulnerabilities",
        "Samba": "HIGH - Possible remote code execution (depending on version)"
    }

    alerts = []

    for port, banner in found_ports:
        for signature, risk in VULN_DB.items():
            if signature.lower() in banner.lower():
                alerts.append({
                    "port": port,
                    "service": signature,
                    "risk": risk
                })
    
    return alerts
