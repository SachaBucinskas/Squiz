# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input
 
import getch
import os
import squizData
import squizScoring

controls = ["Q","W","E","R"]

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

def spQuiz(questionsArg):
    questionNumber = 0 # For tracking which question currently on
    totalQuestions = len(questionsArg) # The total number of questions in the quiz
    score = 0

     # Save terminal width and height so the formatting is correct & adjustable

    for questionData in questionsArg: # Loop over each question
        clearScreen()
        questionNumber += 1

        printTopLine()
        printMiddleLine(("Question: " + str(questionNumber) + "/" + str(totalQuestions)))
        printMiddleLine(("Score: " + str(score)))
        printBotLine()
        printTopLine()
        print(questionData["question"].center(terminalWidth()+2))
        printBotLine()
        

        responseNumber = 0
        longestResponse = 0
        for response in questionData["responses"]: # Get length of longest response for formatting
            if len(response) > longestResponse: longestResponse = len(response) 
        for response in questionData["responses"]:
            print(("[" + controls[responseNumber]+ "] " + response.center(longestResponse)).center(terminalWidth()))
            responseNumber += 1
        score += squizScoring.checkAnswer(getch.getch(), questionData["answer"])

    print()

spQuiz(squizData.getQuestions("template"))