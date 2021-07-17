#!/bin/bash
# Check if modules are installed
if python3 -c "import getch" &> /dev/null; then
    echo "Found getch"
else
    echo "ERROR: Could not find getch" 
    echo ""
    dialog --title "Install Module" \
    --backtitle "Squiz Startup Script"
    --yesno "Would you like to install getch with pip now? Or do you want to exit?"
    response=$?
        case $response in
        0) pip3 install getch;; # Yes
        1) exit 0;; # No
        255) exit 0;; # Hit Escape
    esac 
fi
cd src
python3 ./main.py