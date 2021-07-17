#!/bin/bash
# Check if modules are installed
if python3 -c "import getch" &> /dev/null; then
    echo "Found getch"
else
    echo "ERROR: Could not find getch" 
    echo "Would you like to install getch with pip now?"
    echo "   -If you don't, you'll have to exit"
    read -p "(Y/N): " installGetch
    if grep -q "$installGetch" <<< "yY"; then
        pip3 install getch
    else
        echo "Exitting now. Please reconsider installing getch! Have a nice day!"
        exit 0
    fi
fi
cd src
python3 ./main.py $1 $2