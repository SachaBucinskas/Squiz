# Name:    main.py
# Purpose: This is the main python, it's the one that should ran to actually start the program

import squizMenu
import squizQuiz
import squizData

from squizUI import clearScreen, printBotLine, printMiddleLine, printTopLine, terminalHeight, terminalWidth, getChar

while True:
    userChoice = squizMenu.menu("Main Menu", ["Single Player","Multiplayer","Exit"])
    if userChoice == 0: 
        squizQuiz.spQuiz(squizData.getQuestions("template"))
    elif userChoice == 1:
        print("Multiplayer Coming soon!")
    elif userChoice == 2: 
        exit()