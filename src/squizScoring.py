# Name:    squizScoring.py
# Purpose: This is responsible for checking if it's the correct answer, as well as scoring
 
def checkAnswer(chosen, correct):
    points = 1000
    if chosen.lower() in "1q":
        if "0" in correct: return(points)
        else: return(0)
    elif chosen.lower() in "2w":
        if "1" in correct: return(points)
        else: return(0)
    elif chosen.lower() in "3e":
        if "2" in correct: return(points)
        else: return(0)
    elif chosen in "4r":
        if "3" in correct: return(points)
        else: return(0)
    else:
        print("Invalid input")