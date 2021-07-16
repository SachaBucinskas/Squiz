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