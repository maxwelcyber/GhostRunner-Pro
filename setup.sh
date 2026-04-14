#!/bin/bash

# GhostRunner v2.2-PRO Installer
echo -e "\e[96m[+] Initializing GhostRunner Global Setup...\e[0m"

# Ensure script is executable
chmod +x ghostrunner.py

# Create a symbolic link to /usr/local/bin
# This allows running 'ghostrunner' from anywhere
sudo ln -sf "$(pwd)/ghostrunner.py" /usr/local/bin/ghostrunner

# Check if reports directory exists
if [ ! -d "reports" ]; then
    mkdir reports
    chmod 777 reports
    echo "[+] Created reports directory."
fi

echo -e "\e[92m[+] Installation Complete!\e[0m"
echo -e "\e[93m[!] You can now run GhostRunner by simply typing: ghostrunner\e[0m"
