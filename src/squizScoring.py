# Name:    squizScoring.py
# Purpose: This is responsible for checking if it's the correct answer, as well as scoring
 
def checkAnswer(chosen, correct):
    if chosen.upper() in "Q":
        if "0" in correct: return(True)
        else: return(False)
    elif chosen.upper() in "W":
        if "1" in correct: return(True)
        else: return(False)
    elif chosen.upper() in "E":
        if "2" in correct: return(True)
        else: return(False)
    elif chosen.upper() in "R":
        if "3" in correct: return(True)
        else: return(False)
    else:
        return("invalid")

def checkAnswerMP(chosen, correct):
    # Player One Controls
    if chosen.upper() in "Q":
        if "0" in correct: return(1,True)
        else: return(1, False)
    elif chosen.upper() in "W":
        if "1" in correct: return(1,True)
        else: return(1, False)
    elif chosen.upper() in "E":
        if "2" in correct: return(1,True)
        else: return(1, False)
    elif chosen.upper() in "R":
        if "3" in correct: return(1, True)
        else: return(1, False)
    
    # Player Two Controls
    if chosen.upper() in "U":
        if "0" in correct: return(2,True)
        else: return(2, False)
    elif chosen.upper() in "I":
        if "1" in correct: return(2,True)
        else: return(2, False)
    elif chosen.upper() in "O":
        if "2" in correct: return(2,True)
        else: return(2, False)
    elif chosen.upper() in "P":
        if "3" in correct: return(2, True)
        else: return(2, False)    
    else:
        return("invalid")