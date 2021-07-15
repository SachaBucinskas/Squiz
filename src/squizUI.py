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
    totalCorrect = 0

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
        
        points = 1000
        for response in questionData["responses"]: # Get length of longest response for formatting
            if len(response) > longestResponse: longestResponse = len(response) 
        for response in questionData["responses"]:
            print(("[" + controls[responseNumber]+ "] " + response.center(longestResponse)).center(terminalWidth()))
            responseNumber += 1
        while True:
            userInput = getch.getch()
            wasResponseCorrect = squizScoring.checkAnswer(userInput, questionData["answer"])        
            if wasResponseCorrect == "invalid": 
                print('"' + userInput + '" is not a valid answer.')
                continue
            elif wasResponseCorrect:
                totalCorrect += 1
                printTopLine()
                printMiddleLine("☆ Correct! ☆")
                printMiddleLine("Score: " + str(score) + " + " + str(points))
                score += points
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getch.getch()
                break
            else:
                printTopLine()
                printMiddleLine("↓ Wrong! Bad Luck! ↓")
                printMiddleLine("Score: ")
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getch.getch()
                break


    printTopLine()
    printMiddleLine("Total Questions: " + str(totalQuestions))
    printMiddleLine("Correct Answers: " + str(totalCorrect))

spQuiz(squizData.getQuestions("template"))