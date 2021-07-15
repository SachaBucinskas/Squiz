# Name:    squizData.py
# Purpose: This is responsible for the handling of json files for squiz, 
#          including quizes (questions, answers), leaderboards, etc.

import json
import os.path

testFile = []

with open(os.path.join('data','quizes','template.json'),'r') as testFile:
    questions = json.load(testFile)
    testFile.close()

print(questions)
