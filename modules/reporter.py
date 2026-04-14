import json
from datetime import datetime

def save_report(target, found_ports):
    """
    Saves the scan results to a JSON file for later analysis.
    """
    report_data = {
        "target": target,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "open_ports": []
    }

    for port, banner in found_ports:
        report_data["open_ports"].append({
            "port": port,
            "service": banner
        })

    # Create a filename based on the target and date
    filename = f"report_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    try:
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=4)
        print(f"\n[!] Report saved successfully: {filename}")
    except Exception as e:
        print(f"\n[!] Error saving report: {e}")
