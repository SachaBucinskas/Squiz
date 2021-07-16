# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input

from squizUI import *

controls = ["Q","W","E","R"]

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

        # Displays the responses
        for response in questionData["responses"]: # Get length of longest response for formatting
            if len(response) > longestResponse: longestResponse = len(response) 
        for response in questionData["responses"]: # Prints all the text with the the controls displayed in line with eachother
            print(("[" + controls[responseNumber]+ "] " + response.center(longestResponse)).center(terminalWidth())) 
            responseNumber += 1

        # Gets user input/choice of the responses
        while True: # Loops until a valid input is given, different result for correct or wrong answer
            userInput = getChar()
            wasResponseCorrect = squizScoring.checkAnswer(userInput, questionData["answer"])        
            if wasResponseCorrect == "invalid": # Tell user which key we think they hit & tell them it's not accepted
                print('"' + userInput + '" is not a valid answer.')
                continue
            elif wasResponseCorrect: # Correct answer
                totalCorrect += 1
                printTopLine()
                printMiddleLine("☆ Correct! ☆")
                printMiddleLine("Score: " + str(score) + " + " + str(points))
                score += points
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getChar()
                break
            else: # Wrong answer
                printTopLine()
                printMiddleLine("↓ Wrong! Bad Luck! ↓")
                printMiddleLine("Score: " + str(score))
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getChar()
                break

    # End Summary Screen
    clearScreen()
    accuracy = round(float(totalCorrect) / float(totalQuestions) * 100, 2)
    printTopLine()
    printMiddleLine("Total Questions: " + str(totalQuestions))
    printMiddleLine("Correct Answers: " + str(totalCorrect))
    printMiddleLine('Accuracy ' + str(accuracy) + "%")
    print("╞" + ("═" * terminalWidth()) + "╡")
    printMiddleLine("Press Any Key to Continue")
    printBotLine()
    getChar()

def mpQuiz(questionsArg):
    questionNumber = 0 # For tracking which question currently on
    totalQuestions = len(questionsArg) # The total number of questions in the quiz
    playerOneScore = 0
    playerOneCorrect = 0
    playerTwoScore = 0
    playerTwossCorrect = 0

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

        # Displays the responses
        for response in questionData["responses"]: # Get length of longest response for formatting
            if len(response) > longestResponse: longestResponse = len(response) 
        for response in questionData["responses"]: # Prints all the text with the the controls displayed in line with eachother
            print(("[" + controls[responseNumber]+ "] " + response.center(longestResponse)).center(terminalWidth())) 
            responseNumber += 1

        # Gets user input/choice of the responses
        while True: # Loops until a valid input is given, different result for correct or wrong answer
            userInput = getChar()
            wasResponseCorrect = squizScoring.checkAnswer(userInput, questionData["answer"])        
            if wasResponseCorrect == "invalid": # Tell user which key we think they hit & tell them it's not accepted
                print('"' + userInput + '" is not a valid answer.')
                continue
            elif wasResponseCorrect: # Correct answer
                totalCorrect += 1
                printTopLine()
                printMiddleLine("☆ Correct! ☆")
                printMiddleLine("Score: " + str(score) + " + " + str(points))
                score += points
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getChar()
                break
            else: # Wrong answer
                printTopLine()
                printMiddleLine("↓ Wrong! Bad Luck! ↓")
                printMiddleLine("Score: " + str(score))
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getChar()
                break

    # End Summary Screen
    clearScreen()
    accuracy = round(float(totalCorrect) / float(totalQuestions) * 100, 2)
    printTopLine()
    printMiddleLine("Total Questions: " + str(totalQuestions))
    printMiddleLine("Correct Answers: " + str(totalCorrect))
    printMiddleLine('Accuracy ' + str(accuracy) + "%")
    print("╞" + ("═" * terminalWidth()) + "╡")
    printMiddleLine("Press Any Key to Continue")
    printBotLine()
    getChar()