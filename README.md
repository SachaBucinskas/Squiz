# Squiz

A Command Line Interface quiz game

### Features

* 

# Software Development Plan

## Purpose & Scope

### Description

The terminal application is a fairly simple quiz format, questions are printed before giving the user/s the options below. The user/s is rewarded for correct & timely answers. It supports user made quizes

## Problems it solves

Learning is done best when the individual is well engaged with the activity at hand, and one of the best ways to engage someone is through gamification. This application does so by using the quiz template everyone's familiar with, and adding some more modern video game mechanics. Gamification is also more effective with younger demographics who are more familiar with video game concepts. Not every computer is well equipped whether they have limited display options or simply slow, a simplistic CLI application like this is able to be ran on slow computers, or even on remote computers in SSH sessions, allowing this to be used on computers which don't even have window managers.

## Audience

This application is primarily targeted at the education space, particularly younger age groups who engage with video games more readily than older demographics. The ability to easily add quizes as well as play local multiplayer makes it ideal in Computer Lab environments, as teachers or students can create quizes, and engage with their peers in their tasks. 


## Implementation Plan

### Features

### Kanban Schedule

Initial task list with all the tasks I could think of in the backlog
!["Kanban 1"](./img/Kanban(1).png)

I moved all the tasks required for a minimum viable product into the To-Do area
!["Kanban 2"](./img/Kanban(2).png)

Started implementing the squizData module & json, as it's very foundational to a lot of my other modules & will make testing them easier
!["Kanban 3"](./img/Kanban(3).png)

Began testing & implementing the json & data, ran into issues with my JSON file not using proper syntax which I only found when testing the data module. Added some error handling for missing files.
!["missing File Test"](/img/squizDataMissingFile.png)
!["Kanban 4"](./img/Kanban(4).png)