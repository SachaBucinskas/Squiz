# Name:    squizData.py
# Purpose: This is responsible for the handling of json files for squiz, 
#          including quizes (questions, answers), leaderboards, etc.

import json
import os.path
import os

def getQuestions(quizFile):
    print(os.getcwd())
    try: 
        with open(os.path.join("data","quizes",quizFile+".json"),"r") as tempFile:
            questionsData = json.load(tempFile)["questions"]
            tempFile.close()
        return(questionsData)
    except:
        raise ValueError(quizFile + ".json does not exist inside Data/Quizes.")

#for i in questionData:
#    print(i["question"])
#    print(i["responses"])
#    print(i["answer"])