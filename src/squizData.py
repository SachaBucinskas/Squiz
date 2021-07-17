# Name:    squizData.py
# Purpose: This is responsible for the handling of json files for squiz, 
#          including quizes (questions, answers), leaderboards, etc.

import json
import os.path
import os

def getQuestions(quizFile):
    try: 
        with open(os.path.join("data","quizes",quizFile),"r") as tempFile:
            questionsData = json.load(tempFile)["questions"]
            tempFile.close()
        return(questionsData)
    except:
        raise ValueError(quizFile + " does not exist inside Data/Quizes.")

def getListOfQuizes():
    try:
        return(os.listdir(os.path.join("data","quizes")))
    except:
        raise ValueError(os.path.join("data","quizes") + " is missing!")