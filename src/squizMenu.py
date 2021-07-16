# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input

import getch

from squizUI import clearScreen, printBotLine, printMiddleLine, printTopLine, terminalWidth

def menu(topText, items): # Designed to take a list of options & return the index of the option chosen

    choice = 0

    clearScreen()

    # Print Top Text & Box
    printTopLine()
    printMiddleLine(topText)
    print("╞" + ("═" * terminalWidth()) + "╡")

    # Print the items
    for index in range(len(items)):
        if index == choice:
            printMiddleLine("→ " + str(items[index]) + " ←")
            printMiddleLine("")
        else:
            printMiddleLine(str(items[index]))
            printMiddleLine("")
    
    # Print controls
    print("╞" + ("═" * terminalWidth()) + "╡")
    printMiddleLine("Controls")
    printMiddleLine("")
    printBotLine()


menu("Test","test",[1,2,3])