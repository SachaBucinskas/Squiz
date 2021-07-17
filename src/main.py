# Name:    main.py
# Purpose: This is the main python, it's the one that should ran to actually start the program

import squizMenu
import squizQuiz
import squizData
import sys

from squizUI import clearScreen, printBotLine, printMiddleLine, printTopLine, terminalHeight, terminalWidth, getChar

while True:
    userChoice = squizMenu.menu("Main Menu",["Single Player","Multiplayer","Exit",],"")
    if userChoice == 0:
        userChoice = squizMenu.pagedMenu("Select a Quiz", squizData.getListOfQuizes(),"") 
        squizQuiz.spQuiz(squizData.getQuestions(squizData.getListOfQuizes()[userChoice]))
    elif userChoice == 1:
        squizQuiz.mpQuiz(squizData.getQuestions("template"))
    elif userChoice == 2: 
        sys.exit()