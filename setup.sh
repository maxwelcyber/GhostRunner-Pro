#!/bin/bash

# GhostRunner v2.2-PRO Installer
echo -e "\e[96m[+] Initializing GhostRunner Global Setup...\e[0m"

# Get the absolute path of the current directory
INSTALL_DIR=$(pwd)

# Ensure script is executable
chmod +x "$INSTALL_DIR/ghostrunner.py"

# Create a symbolic link to /usr/local/bin
# Using the absolute path ensures it works from any directory
sudo ln -sf "$INSTALL_DIR/ghostrunner.py" /usr/local/bin/ghostrunner

# Check if reports directory exists
if [ ! -d "$INSTALL_DIR/reports" ]; then
    mkdir "$INSTALL_DIR/reports"
    chmod 777 "$INSTALL_DIR/reports"
    echo "[+] Created reports directory."
fi

echo -e "\e[92m[+] Installation Complete!\e[0m"
echo -e "\e[93m[!] Launch by typing: ghostrunner\e[0m"
