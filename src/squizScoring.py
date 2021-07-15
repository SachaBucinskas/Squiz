# Name:    squizScoring.py
# Purpose: This is responsible for checking if it's the correct answer, as well as scoring
 
def checkAnswer(chosen, correct):
    if chosen.lower() in "1q":
        if "0" in correct: return(True)
        else: return(False)
    elif chosen.lower() in "2w":
        if "1" in correct: return(True)
        else: return(False)
    elif chosen.lower() in "3e":
        if "2" in correct: return(True)
        else: return(False)
    elif chosen in "4r":
        if "3" in correct: return(True)
        else: return(False)
    else:
        return("invalid")