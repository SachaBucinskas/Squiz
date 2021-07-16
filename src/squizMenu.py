# Name:    squizMenu.py
# Purpose: This is responsible for displaying user interfaces & receiving user input

from squizUI import clearScreen, printBotLine, printMiddleLine, printTopLine, terminalHeight, terminalWidth, getChar

def mainMenu(items): # Designed to take a list of options & return the index of the option chosen
    choice = 0
    index = 0

    while True:
        clearScreen()
        # Print Top Text & Box
        printTopLine()
        printMiddleLine("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        printMiddleLine("██░▄▄▄░█░▄▄░█░██░██▄██▄▄░██")
        printMiddleLine("██▄▄▄▀▀█░▀▀░█░██░██░▄█▀▄███")
        printMiddleLine("██░▀▀▀░████░██▄▄▄█▄▄▄█▄▄▄██")
        printMiddleLine("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        print("╞" + ("═" * terminalWidth()) + "╡")

        # Print the items
        for i in range(len(items)):
            if i == choice:
                printMiddleLine("→ " + str(items[i]) + " ←")
            else:
                printMiddleLine(str(items[i]))
        
        # Print controls
        print("╞" + ("═" * terminalWidth()) + "╡")
        printMiddleLine(str(index + choice))
        printMiddleLine("")
        printBotLine()

        # Depending on key pressed, move arrow or select option
        action = getChar()

        # Move arrow up
        if action in ["UP", "W"]:
            if choice == 0: # If at the top, loop to the bottom
                choice = len(items) - 1 
            else: choice -= 1 # Otherwise move up
        # Move arrow down
        elif action in ["DOWN", "S"]:
            if choice == len(items) - 1: # If at bottom, loop to top
                choice = 0
            else:
                choice += 1 # Otherwise, move down

        # Go to an earlier page
        elif action in ["LEFT", "A"]:
            if index <= 15: # if on first page, loop to last page
                index = len(items) - 15
                if index < 0: index = 0
            else:
                index -= 15
        # Go to a later page
        elif action in ["RIGHT","D"]:
            if index >= len(items) - 16: # if on last page, go to first page
                index = 0
            else:
                index += 15
        elif action in ["ENTER"]:
            return(index + choice) # Returns the index of the choice in the items list