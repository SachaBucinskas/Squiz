
# Name:    squizUI.py
# Purpose: This is responsible for displaying user interfaces & receiving user input

from squizUI import *
import time

controls = ["Q","W","E","R"]
controlsP2 = ["U","I","O","P"]

def spQuiz(questionsArg):
    questionNumber = 0 # For tracking which question currently on
    totalQuestions = len(questionsArg) # The total number of questions in the quiz
    score = 0
    totalCorrect = 0

    for questionData in questionsArg: # Loop over each question
        clearScreen()
        questionNumber += 1

        printTopLine()
        printMiddleLine(("Question: " + str(questionNumber) + "/" + str(totalQuestions)))
        printMiddleLine(("Score: " + str(score)))
        printBotLine()
        printTopLine()
        slowPrint(questionData["question"].center(terminalWidth()+2))
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
    playerOneAnswered = 0
    playerTwoScore = 0
    playerTwoCorrect = 0
    playerTwoAnswered = 0

    for questionData in questionsArg: # Loop over each question
        clearScreen()
        questionNumber += 1

        printTopLine()
        printMiddleLine(("Question: " + str(questionNumber) + "/" + str(totalQuestions)))
        printMiddleLine("P1 Score: " + str(playerOneScore) + "  |  P2 Score: "+ str(playerTwoScore))
        printBotLine()
        printTopLine()
        slowPrint(questionData["question"].center(terminalWidth()+2))
        printBotLine()
        
        responseNumber = 0
        longestResponse = 0
        points = 1000

        # Displays the responses
        for response in questionData["responses"]: # Get length of longest response for formatting
            if len(response) > longestResponse: longestResponse = len(response) 
        for response in questionData["responses"]: # Prints all the text with the the controls displayed in line with eachother
            print(("[" + controls[responseNumber]+ "] " + response.center(longestResponse) + " [" + controlsP2[responseNumber] + "]").center(terminalWidth())) 
            responseNumber += 1

        # Gets user input/choice of the responses
        while True: # Loops until a valid input is given, different result for correct or wrong answer
            userInput = getChar()
            whoResponded, wasResponseCorrect = squizScoring.checkAnswerMP(userInput, questionData["answer"])        
            if wasResponseCorrect == "invalid": # Tell user which key we think they hit & tell them it's not accepted
                print('"' + userInput + '" is not a valid answer.')
                continue
            elif wasResponseCorrect: # Correct answer
                printTopLine()
                printMiddleLine("☆ Correct! ☆")
                # Player 1 Correct
                if whoResponded == 1:
                    playerOneAnswered += 1
                    playerOneCorrect += 1        
                    printMiddleLine("P1 Score: " + str(playerOneScore) + " + " + str(points))
                    playerOneScore += points
                    printMiddleLine("")
                    printMiddleLine("P2 Score: " + str(playerTwoScore))
                #Player 2 Correct
                elif whoResponded == 2:
                    playerTwoAnswered += 1
                    playerTwoCorrect += 1
                    printMiddleLine("P2 Score: " + str(playerTwoScore) + " + " + str(points))
                    playerTwoScore += points
                    printMiddleLine("")
                    printMiddleLine("P1 Score: " + str(playerOneScore))

                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getChar()
                time.sleep(1)
                break
            else: # Wrong answer
                printTopLine()
                printMiddleLine("↓ Wrong! Bad Luck! ↓")
                # Player 1 Wrong
                if whoResponded == 1:
                    playerOneAnswered += 1
                    printMiddleLine("P1 Score: " + str(playerOneScore) + " - " + str(points))
                    playerOneScore -= points
                    printMiddleLine("")
                    printMiddleLine("P2 Score: " + str(playerTwoScore))
                # Player 2 Wrong
                if whoResponded == 2:
                    playerTwoAnswered += 1
                    printMiddleLine("P2 Score: " + str(playerTwoScore) + " - " + str(points))
                    playerTwoScore -= points
                    printMiddleLine("")
                    printMiddleLine("P1 Score: " + str(playerOneScore))
                    
                printMiddleLine("")
                printMiddleLine("Press any key to Continue")
                printBotLine()
                getChar()
                time.sleep(1)
                break

    # End Summary Screen
    clearScreen()

    try: combinedAccuracy = round(float(playerOneCorrect+playerTwoCorrect) / float(totalQuestions) * 100, 2)
    except: combinedAccuracy = 0.00
    try: playerOneAccuracy = round(float(playerOneCorrect) / float(playerOneAnswered) * 100, 2)
    except: playerOneAccuracy = 0.00
    try: playerTwoAccuracy = round(float(playerTwoCorrect) / float(playerTwoAnswered) * 100, 2)
    except: playerTwoAccuracy = 0.00
    printTopLine()
    printMiddleLine("Total Questions: " + str(totalQuestions))
    printMiddleLine("Combined Correct: " + str(playerOneCorrect + playerTwoCorrect))
    printMiddleLine("Combined Accuracy: " + str(combinedAccuracy) + "%")
    printMiddleLine("Combined Score: " + str(playerOneScore + playerTwoScore))
    print("╞" + ("═" * terminalWidth()) + "╡")
    # Player 1 Wins Summary
    if playerOneScore > playerTwoScore:
        printMiddleLine("☆ Player 1 - Wins! ☆")
        printMiddleLine("Correct: " + str(playerOneCorrect))
        printMiddleLine("Accuracy: " + str(playerOneAccuracy) + "%")
        printMiddleLine("Score: " + str(playerOneScore))
        print("╞" + ("═" * terminalWidth()) + "╡")
        printMiddleLine("Player 2 - Loses. Bad Luck!")
        printMiddleLine("Correct: " + str(playerTwoCorrect))
        printMiddleLine("Accuracy: " + str(playerTwoAccuracy) + "%")
        printMiddleLine("Score: " + str(playerTwoScore))
    # Player 2 Wins Summary
    elif playerOneScore < playerTwoScore:
        printMiddleLine("☆ Player 2 - Wins! ☆")
        printMiddleLine("Correct: " + str(playerTwoCorrect))
        printMiddleLine("Accuracy: " + str(playerTwoAccuracy) + "%")
        printMiddleLine("Score: " + str(playerTwoScore))
        print("╞" + ("═" * terminalWidth()) + "╡")
        printMiddleLine("Player 1 - Loses. Bad Luck!")
        printMiddleLine("Correct: " + str(playerOneCorrect))
        printMiddleLine("Accuracy: " + str(playerOneAccuracy) + "%")
        printMiddleLine("Score: " + str(playerOneScore))
    # Tie / Draw Summary
    else:
        printMiddleLine("☆ Player 1 - Ties! ☆")
        printMiddleLine("Correct: " + str(playerOneCorrect))
        printMiddleLine("Accuracy: " + str(playerOneAccuracy) + "%")
        printMiddleLine("Score: " + str(playerOneScore))
        print("╞" + ("═" * terminalWidth()) + "╡")
        printMiddleLine("☆ Player 2 - Ties! ☆")
        printMiddleLine("Correct: " + str(playerTwoCorrect))
        printMiddleLine("Accuracy: " + str(playerTwoAccuracy) + "%")
        printMiddleLine("Score: " + str(playerTwoScore))

    print("╞" + ("═" * terminalWidth()) + "╡")
    printMiddleLine("Press Any Key to Continue")
    printBotLine()
    getChar()