# Name:    squizData.py
# Purpose: This is responsible for the handling of json files for squiz, 
#          including quizes (questions, answers), leaderboards, etc.

import json
import os.path

def getQuestions(quizFile):
    if os.path.isfile(os.path.join('data','quizes','subscriptions.json')): 
        with open(os.path.join('data','quizes',quizFile+'.json'),'r') as tempFile:
            questionsData = json.load(tempFile)["questions"]
            tempFile.close()
        return(questionsData)
    else:
        raise ValueError(quizFile + ".json does not exist inside Data/Quizes.")


#questionData = getQuestions("template") 
#for i in questionData:
#    print(i["question"])
#    print(i["responses"])
#    print(i["answer"])