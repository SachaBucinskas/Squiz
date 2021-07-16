# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input
 
import getch
import os
import squizData
import squizScoring

def clearScreen():
    # Windows
    if os.name == 'nt': os.system("cls")
    # Mac/Linux/Posix
    else: os.system("clear")

def terminalHeight():
    width, height = os.get_terminal_size(0)
    height = height - 2
    return(height)

def terminalWidth():
    width, height = os.get_terminal_size(0)
    width = width - 2
    return(width)

def printMiddleLine(line):
    print("│" + line.center(terminalWidth()) + "│")

def printTopLine():
    print("┌" + ("─"*terminalWidth()) + "┐")

def printBotLine():
    print("└" + ("─"*terminalWidth()) + "┘")

def getChar():
    userInput = getch.getch()
    
    # Special keys
    if userInput == "\n":
        return("ENTER")
    elif userInput == "\t":
        return("TAB")
    elif userInput == " ":
        return("SPACE")
    elif userInput == "\x1b":
        userInput = getch.getch()
        if userInput == "[":
            userInput = getch.getch()
            # Arrow Keys
            if userInput == "A":
                return("UP")
            elif userInput == "B":
                return("DOWN")
            elif userInput == "C":
                return("RIGHT")
            elif userInput == "D":
                return("LEFT")
            # Numpad & Other keys
            elif userInput == "E":
                return("MIDDLENUM")
            elif userInput == "F":
                return("END")
            elif userInput == "H":
                return("HOME")
            elif userInput == "2":
                userInput = getch.getch() # Catches unnecessary ~ character that appears as extra input otherwise
                return("INS")
            elif userInput == "3":
                userInput = getch.getch() # Catches unnecessary ~
                return("DEL")
            elif userInput == "5":
                userInput = getch.getch() # Catches unnecessary ~
                return("PGUP")
            elif userInput == "6":
                userInput = getch.getch() # Catches unnecessary ~
                return("PGDN")
    else: # These should all be single character & representative of what's on the keyboard
        return(userInput.upper())