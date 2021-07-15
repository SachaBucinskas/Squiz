# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input
 
import getch
import os
import squizData
import squizScoring

controls = ["Q","W","E","R"]

def terminalWidth():
    width, height = os.get_terminal_size(0)
    return(width)

def spQuiz(questionsArg):
    questionNumber = 0 # For tracking which question currently on
    totalQuestions = len(questionsArg) # The total number of questions in the quiz
    score = 0

     # Save terminal width and height so the formatting is correct & adjustable

    for questionData in questionsArg:
        print("=" * terminalWidth())
        questionNumber += 1
        print(("Question: " + str(questionNumber) + "/" + str(totalQuestions)).center(terminalWidth()))
        print(("Score: " + str(score)).center(terminalWidth()))
        print("\n")
        print(questionData["question"])
        print("=" * terminalWidth())
        responseNumber = 0
        longestResponse = 0
        for response in questionData["responses"]:
            if len(response) > longestResponse: longestResponse = len(response) 
        for response in questionData["responses"]:
            print(("[" + controls[responseNumber]+ "] " + response.center(longestResponse)).center(terminalWidth()))
            responseNumber += 1
        score += squizScoring.checkAnswer(getch.getch(), questionData["answer"])

spQuiz(squizData.getQuestions("template"))