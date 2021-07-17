# Name:    squizMenu.py
# Purpose: This is responsible for displaying user interfaces & receiving user input

from squizUI import clearScreen, printBotLine, printMiddleLine, printTopLine, terminalHeight, terminalWidth, getChar

def menu(topText, items, bottomText): # Designed to take a list of options & return the index of the option chosen
    choice = 0

    while True:
        clearScreen()
        # Print Top Text & Box
        printTopLine()
        printMiddleLine("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        printMiddleLine("██░▄▄▄░█░▄▄░█░██░██▄██▄▄░██")
        printMiddleLine("██▄▄▄▀▀█░▀▀░█░██░██░▄█▀▄███")
        printMiddleLine("██░▀▀▀░████░██▄▄▄█▄▄▄█▄▄▄██")
        printMiddleLine("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        printMiddleLine(str(topText))
        print("╞" + ("═" * terminalWidth()) + "╡")

        # Print the items
        for i in range(len(items)):
            if i == choice:
                printMiddleLine("→ " + str(items[i]) + " ←")
            else:
                printMiddleLine(str(items[i]))
        
        # Print controls
        print("╞" + ("═" * terminalWidth()) + "╡")
        printMiddleLine(str(bottomText))
        print("╞" + ("═" * terminalWidth()) + "╡")
        printMiddleLine("--Controls--")
        printMiddleLine("[W] or [↑] Move Selection Up  [S] or [↓] Move Selection Down")
        printMiddleLine("[A] or [←] Earlier Page  [D] or [→] Later Page")
        printMiddleLine("[Enter] Chooses your Selection")
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
            return("LEFT")
        # Go to a later page
        elif action in ["RIGHT","D"]:
            return("RIGHT")
        elif action in ["ENTER"]:
            return(choice) # Returns the index of the choice in the items list

def pagedMenu(topText, items): # Designed to take a list of options & return the index of the option chosen

    index = 0
    pageLength = 10
    while True:
        userAction = menu(topText, items[index:index+pageLength], "Items: ("+str(index+1) +"-" + str(index+pageLength)+ ")")
        # Go to an earlier page
        if userAction in ["LEFT","A"]:
            if index < pageLength: # If on first page, loop to last page
                index = len(items) - pageLength
                if index < 0:
                    index = 0
            else:
                index -= pageLength
        # Go to a later page
        elif userAction in ["RIGHT","D"]:
            if index >= len(items) - pageLength + 1: # If on last page, loop to first
                index = 0
            else:
                index += pageLength
                if index > (len(items)):
                    index = index - pageLength
        else:
            return(index + userAction)