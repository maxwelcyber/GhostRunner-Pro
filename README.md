# GhostRunner v2.2-PRO 👻
**High-Concurrency Vulnerability Auditor & SIEM Integration Engine**

GhostRunner is a professional-grade reconnaissance and vulnerability assessment tool built for rapid network auditing and automated Security Operations Center (SOC) workflows. Developed with a high-concurrency 500-thread engine, it bridges the gap between raw data collection and real-time threat detection in cloud and on-prem environments.

---

## 🚀 Core Capabilities

* **High-Performance Threading:** Leverages a batch-processing engine (500 threads) to sweep all 65,535 TCP ports with extreme efficiency.
* **Vulnerability Signature Mapping:** Built-in intelligence module for identifying critical services and known backdoors (e.g., vsFTPd 2.3.4, UnrealIRCd, OpenSSH legacy exploits).
* **SOC-Ready Data Export:** Dual-format reporting (JSON & TXT). JSON outputs are structured specifically for automated ingestion by SIEM platforms like **Wazuh**, **ELK**, or **Splunk**.
* **Dynamic Timing Control:** Configurable scan intensity (T1-T3) to balance audit speed against network stability and IDS detection thresholds.

---

## 🛠️ SOC Lab Pipeline
GhostRunner is engineered to function as a core data provider for modern security monitoring.

Reconnaissance: Execute a full-scale audit of target infrastructure.

Structured Output: GhostRunner generates a timestamped JSON report in the reports/ directory.

SIEM Ingestion: A Wazuh Agent monitors the reports/ folder via syscheck or localfile configurations.

Real-Time Alerting: Findings are parsed by the Wazuh Manager, triggering high-severity alerts on the dashboard when critical vulnerabilities are identified.

---

## 💻 Technical Usage
* **Flags**
-t, --timing: 1 (Aggressive), 2 (Standard), 3 (Polite)

-o, --output: Custom filename for the generated reports.

-f, --format: Choose between json, txt, or both (default).

---

## 🔒 Security Policy
This tool is intended for Authorized Educational and Professional Auditing only. As a Cybersecurity student and aspiring Cloud Security Engineer, I developed this tool to demonstrate the critical role of structured logging and automation in modern vulnerability management.

---

Developed by: maxwelcyber

Status: v2.2-PRO | Production Build

---

## ⚙️ Quick Installation (One-Liner)

To install GhostRunner v2.2-PRO globally on your Linux system, copy and paste the following command:

```bash
git clone [https://github.com/maxwelcyber/GhostRunner-Pro.git](https://github.com/maxwelcyber/GhostRunner-Pro.git) && cd GhostRunner-Pro && chmod +x setup.sh && ./setup.sh
