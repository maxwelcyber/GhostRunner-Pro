#!/usr/bin/env python3
import sys
import os
import readline 
import argparse
from modules import scanner

def print_banner():
    # RESTORED: The Ghost Icon
    banner = r"""
       .---.
      /     \    GhostRunner v2.2-PRO
     |( ) ( )|   [Status: Data-Export Active]
      \  ^  /    Developed by: maxwelcyber
       |||||
       '|||'
    """
    print(f"\033[96m{banner}\033[0m")
    print("\033[90m" + "="*75 + "\033[0m")

def print_help():
    print("""
    \033[93mGhostRunner v2.2-PRO Flags & Usage:\033[0m
    -------------------------------------------------------
    \033[92mscan <ip>\033[0m             Run default 65k port audit
    \033[92m-t, --timing <1-3>\033[0m    1: Aggressive, 2: Standard, 3: Polite
    \033[92m-o, --output <name>\033[0m   Specify a custom filename for reports
    \033[92m-f, --format <type>\033[0m   json, txt, or both (default: both)
    
    \033[92mhelp\033[0m                  Display this menu
    \033[92mclear\033[0m                 Clear terminal screen
    \033[92mexit\033[0m                  Shutdown GhostRunner
    """)

def main():
    os.system('clear')
    print_banner()
    print("\033[96mGhostRunner v2.2-PRO Loaded.\033[0m Full 65k Port Audit Active.")
    print("Type 'help' for flag syntax.")

    while True:
        try:
            line = input("\033[92mghostrunner > \033[0m").strip()
            if not line: continue
            
            parts = line.split()
            cmd = parts[0].lower()

            if cmd in ["exit", "quit"]: break
            elif cmd == "help": print_help()
            elif cmd == "clear": os.system('clear'); print_banner()
            elif cmd == "scan":
                # Handle internal flags properly
                parser = argparse.ArgumentParser(exit_on_error=False, add_help=False)
                parser.add_argument('target')
                parser.add_argument('-t', '--timing', type=int, default=2)
                parser.add_argument('-o', '--output', default=None)
                parser.add_argument('-f', '--format', default='both', choices=['json', 'txt', 'both'])
                
                try:
                    args = parser.parse_args(parts[1:])
                    all_ports = list(range(1, 65536))
                    scanner.scan_target(args.target, all_ports, args.timing, args.output, args.format)
                except:
                    print(f"\033[91m[-] Usage: scan <ip> [-t 1-3] [-o filename] [-f json|txt|both]\033[0m")
            else:
                print(f"[-] Unknown command: {cmd}")
        except KeyboardInterrupt: 
            print("\n")
            continue

if __name__ == "__main__":
    main()
