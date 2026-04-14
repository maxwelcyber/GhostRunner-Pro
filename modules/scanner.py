import socket
import threading
import time
import sys
import json
import os
from modules import intel

shutdown_flag = False

def progress_spinner(stop_event):
    chars = ['|', '/', '-', '\\']
    while not stop_event.is_set() and not shutdown_flag:
        for char in chars:
            # RESTORED: The Loading Spinner
            sys.stdout.write(f'\r\033[90m[*] 65k Audit in progress... {char}\033[0m')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 45 + '\r')

def save_results(target, scan_data, output_base, format_choice):
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"reports/{output_base}_{timestamp}" if output_base else f"reports/audit_{target}_{timestamp}"

    # JSON Export (For Wazuh/Automation)
    if format_choice in ['json', 'both']:
        with open(f"{filename}.json", 'w') as f:
            json.dump({"target": target, "timestamp": timestamp, "results": scan_data}, f, indent=4)
        print(f"\033[92m[+] JSON saved: {filename}.json\033[0m")

    # TXT Export (For Portfolio Documentation)
    if format_choice in ['txt', 'both']:
        with open(f"{filename}.txt", 'w') as f:
            f.write(f"GhostRunner Audit Report - {target}\n" + "="*55 + "\n")
            for entry in scan_data:
                f.write(f"Port: {entry['port']} | Service: {entry['banner']}\n")
                for threat in entry['threats']:
                    f.write(f"  [!] {threat}\n")
        print(f"\033[92m[+] TXT saved: {filename}.txt\033[0m")

def scan_port(target, port, scan_results, timeout):
    global shutdown_flag
    if shutdown_flag: return
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        if s.connect_ex((target, port)) == 0:
            try:
                s.send(b"\r\n")
                banner = s.recv(1024).decode(errors='ignore').strip()
                banner = " ".join(banner.split())
            except: banner = "Unknown Service"
            
            threats = intel.get_threat_intel(banner)
            sys.stdout.write('\r' + ' ' * 80 + '\r') 
            
            # UI: BOLD WHITE FOR SCANNABILITY
            print(f"\033[1;97m{port}/tcp\topen\t{banner[:65]}\033[0m")
            
            scan_results.append({"port": port, "banner": banner, "threats": threats})

            for t in threats:
                color = "\033[91m" if "CRITICAL" in t else "\033[93m"
                print(f"{color}{t}\033[0m")
        s.close()
    except: pass

def scan_target(target, ports, timing=2, output=None, fmt='both'):
    global shutdown_flag
    shutdown_flag = False
    
    # Timing logic
    timeouts = {1: 0.4, 2: 0.8, 3: 1.5}
    timeout = timeouts.get(timing, 0.8)

    print(f"\n\033[97m[*] FULL AUDIT START | Target: {target} | Timing: {timing}\033[0m")
    print("-" * 75)
    
    stop_event = threading.Event()
    spinner = threading.Thread(target=progress_spinner, args=(stop_event,))
    spinner.start()

    scan_results = []
    threads = []
    
    try:
        for port in ports:
            if shutdown_flag: break
            t = threading.Thread(target=scan_port, args=(target, port, scan_results, timeout))
            t.setDaemon(True)
            t.start()
            threads.append(t)
            
            if len(threads) >= 500: # High-concurrency batching
                for t in threads: t.join()
                threads = []
        for t in threads: t.join()
    except KeyboardInterrupt:
        shutdown_flag = True
        print("\n\033[91m[!] Aborting... cleaning up and saving results.\033[0m")
    
    stop_event.set()
    spinner.join()
    
    if scan_results:
        print("-" * 75)
        save_results(target, scan_results, output, fmt)
