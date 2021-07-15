# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input
 
import getch
import os
import squizData

def quiz(questionsArg):
    questionNumber = 0 # For tracking which question currently on
    totalQuestions = len(questionsArg) # The total number of questions in the quiz
    score = 0

    terminalWidth, terminalHeight = os.get_terminal_size(0)

    for questionData in questionsArg:
        questionNumber += 1
        print(("Question: " + str(questionNumber) + "/" + str(totalQuestions)).center(terminalWidth))
        print(("Score: " + str(score)).center(terminalWidth))
        print("\n")
        print(questionData["question"])
        print("-" * terminalWidth)


quiz(squizData.getQuestions("template"))