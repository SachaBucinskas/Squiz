# Software Development Plan

A Command Line Interface quiz game

Created by Sacha Bucinskas for Coder Academy

### Features

* Custom Quiz File Support using JSON
* Local Multiplayer
* Scrollable Menus
* Instanteous input
* Dynamically scales with window size 

## Purpose & Scope

### Description

The terminal application is a fairly simple quiz format, questions are printed before giving the user/s the options below. The user/s is rewarded for correct & timely answers. It supports user made quizes

### Problems it solves

Learning is done best when the individual is well engaged with the activity at hand, and one of the best ways to engage someone is through gamification. This application does so by using the quiz template everyone's familiar with, and adding some more modern video game mechanics. Gamification is also more effective with younger demographics who are more familiar with video game concepts. Not every computer is well equipped whether they have limited display options or simply slow, a simplistic CLI application like this is able to be ran on slow computers, or even on remote computers in SSH sessions, allowing this to be used on computers which don't even have window managers.

### Audience

This application is primarily targeted at the education space, particularly younger age groups who engage with video games more readily than older demographics. The ability to easily add quizes as well as play local multiplayer makes it ideal in Computer Lab environments, as teachers or students can create quizes, and engage with their peers in their tasks. 

## User Experience

Users will be greeted by a Menu allowing them to pick Single Player, Multi Player, or Exit

![Main Menu](./img/tests/mainMenu.png)

If they select Single Player they will then have to select which quiz from the pagedMenu

![Paged Menu](./img/tests/quizSelect.png)

They'll then have the question slowly printed before their answer options are revealed with the relevant keys/controls printed alongside it

![SP Quiz Question](./img/tests/spQuizQuestion.png)

If they answer wrong, it will notify them & tell them the correct answer before waiting for any key to display the next question

![SP Wrong Answer](./img/tests/spWrongAnswer.png)

If they answer correctly, it will notify them & tell them how many points they gained before waiting for any key to display the next question

![SP Correct Answer](./img/tests/spCorrectAnswer.png)

Once they've answered all the questions, it will display a short summary of how many questions there were, how many they answered correct, their accuracy in % and their score

![SP End Summary](./img/tests/spEndSummary.png)

The Multiplayer experience is very similar, they experience the same quiz selection screen

![Paged Menu](./img/tests/quizSelect.png)

The question page again is very similar, however it now displays 2 sets of controls & 2 sets of scores at the top

![2P Quiz Question](./img/tests/mpQuizQuestion.png)

If they answer wrong, it's largely the same except now they also lose points to discourage blocking the other person answering with bad answers

![2P Wrong Answer](./img/tests/mpWrongAnswer.png)

If they answer right, again, largely the same except display 2 scores

![2P Correct Answer](./img/tests/mpCorrectAnswer.png)

The end summary page is tweaked a decent bit. It provides both combined/culmative stats for people playing cooperatively, as well as individual scores for those playing competitively

![2P End Summary](./img/tests/mpEndSummary.png)

Hitting exit in the Menu, well, exits immediately

![Exit](./img/tests/exit.png)

## Flow Diagrams

### Main

![Main.py Flowchart](./img/flowcharts/main.png)

### pagedMenu

![pagedMenu Function Flowchart](./img/flowcharts/pagedMenu.png)

### SP Quiz

![SP Quiz Flowchart](./img/flowcharts/spQuiz.png)

### MP Quiz

![MP Quiz Flowchart](./img/flowcharts/mpQuiz.png)