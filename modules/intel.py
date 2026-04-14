import re

def get_threat_intel(service_banner):
    if not service_banner: return []
    intel_hits = []
    banner_low = service_banner.lower()

    critical_sigs = {
        'vsftpd 2.3.4': 'CRITICAL:CVE-2011-2523 (Backdoor Found!)',
        'unrealircd': 'CRITICAL:CVE-2010-2075 (Trojan Detected)',
        'openssh_4.7': 'CRITICAL:CVE-2008-5161 (Encryption Weakness)',
        'root@': 'CRITICAL:ROOT SHELL ACCESS DETECTED',
        'ingreslock': 'CRITICAL:PORT 1524: ROOT BACKDOOR'
    }

    for key, val in critical_sigs.items():
        if key in banner_low:
            intel_hits.append(val)

    match = re.search(r'([a-zA-Z0-9\-\_]{3,})\/?\s?v?([\d\.]+)', service_banner)
    if match:
        service, version = match.group(1), match.group(2)
        if service.upper() not in ['HTTP', 'DATE', 'DEBIAN', 'UBUNTU']:
            try:
                major = int(version.split('.')[0])
                if major < 5 and not any("CRITICAL" in h for h in intel_hits):
                    intel_hits.append(f"MID-RANGE:{service} {version} likely Legacy/EOL")
            except: pass
    return intel_hits
