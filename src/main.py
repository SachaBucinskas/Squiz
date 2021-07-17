# Name:    main.py
# Purpose: This is the main python, it's the one that should ran to actually start the program
__version__ = "1.0"
import squizMenu
import squizQuiz
import squizData
import sys


from squizUI import clearScreen, printBotLine, printMiddleLine, printTopLine, terminalHeight, terminalWidth, getChar
userChoice = ""


if len(sys.argv)>2:
    if sys.argv[1] == "--help":
        print("squiz " + __version__ + " (python3)")
        print("Usage: python main.py [options]")
        print("\nSquiz is a command line quiz program made in Python 3 supporting custom quiz files & local Multiplayer!")
        print("""\nAvailable Arguements:
        --help - Prints out this message with help on how to use the program
        -sp - Allows you to choose & play a quiz without going through the main menu or quiz selector
        -mp - Allows you to choose & play a quiz in Multiplayer without going through the main menu or quiz selector""")
        sys.exit()
    elif sys.argv[1] == "-sp":
        try:
            if str(sys.argv[2]).strip() == "":
                print("Please specify a quiz to open")
                sys.exit()
            try: squizQuiz.spQuiz(squizData.getQuestions(str(sys.argv[2])))
            except:
                try: squizQuiz.spQuiz(squizData.getQuestions(str(sys.argv[2])+".json")) # see if .json was missing
                except:
                    print("Cannot find \""+str(sys.argv[2])+"\" inside data/quizes")
                    sys.exit()
        except KeyboardInterrupt:
            print("Hate to see you leave so soon! Take care!")
            sys.exit()
    elif sys.argv[1] == "-mp":
        try:
            if str(sys.argv[2]).strip() == "":
                print("Please specify a quiz to open")
                sys.exit()
            try: squizQuiz.mpQuiz(squizData.getQuestions(str(sys.argv[2])))
            except:
                try: squizQuiz.mpQuiz(squizData.getQuestions(str(sys.argv[2])+".json")) # see if .json was missing
                except:
                    print("Cannot find \""+str(sys.argv[2])+"\" inside data/quizes")
                    sys.exit()
        except KeyboardInterrupt:
            print("Hate to see you leave so soon! Take care!")
            sys.exit()

try:
    while True:
        if userChoice == 0:
            userChoice = squizMenu.pagedMenu("Select a Quiz", squizData.getListOfQuizes(),"") 
            squizQuiz.spQuiz(squizData.getQuestions(squizData.getListOfQuizes()[userChoice]))
        elif userChoice == 1:
            userChoice = squizMenu.pagedMenu("Select a Quiz", squizData.getListOfQuizes(),"") 
            squizQuiz.mpQuiz(squizData.getQuestions(squizData.getListOfQuizes()[userChoice]))
        elif userChoice == 2: 
            sys.exit()
        userChoice = squizMenu.menu("Main Menu",["Single Player","Multiplayer","Exit",],"")
except KeyboardInterrupt:
    print("Hate to see you leave so soon! Take care!")
    sys.exit()