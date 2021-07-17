# Implementation Plan

## Features

### Custom Quiz Support
* Create Data module designed to read external json files
    * Function to read the files & parse the list of questions
    * Function to read the list of quiz files from within data/quizes
* Create a menu function to select the custom quiz files
* Create quiz module to interpret the custom json files
    * Function to display the question text
    * Function to get the user's answer
    * Function to see if the user was right

### Local Multiplayer
* Create function inside UI module to make handling of special characters easier. Use getch module, as it allows you to know who answered first & feels more responsive generally
* Create custom function inside scoring module to return who answered & whether they were right
* Create custom quiz function inside quiz module to handle the custom display & scoring required
* Create additional summary screens more appropriate for multiplayer
* Create different scoring rules for points, for example negative points to punish fast innaccurate answering (blocking people if they're ahead)

### Multi-page scrolling menu
* Create a menu module with a menu function
    * Create for loop over a list for displaying options, allowing various amounts/lengths
    * Create reusable UI code in UI module to save time creating borders & clearing screen
    * Make automatically adjustable based on terminal width using UI module function
    * Return "LEFT" & "RIGHT" for multipage-wrapper function
* Create a multipage-menu wrapper which hands in slices of the total list of options to the menu, showing later options or earlier options based off the index (thus allowing theoretically infinite custom files)
* If on the first or last page, loop

## Kanban

Kanban is a scheduling technique developed by an engineer at Toyota that focuses on creating "cards" that move in a single direction through the system. It's ideal for agile projects that constantly create deliverables, so it's fairly common in Software Development. Using this technique I created a project on Trello, and created a list of tasks and put some of the most important minimum viable product tasks, with the goal of doing as many non-essential cards as possible if given enough time

![Kanban Table](./img/Trello/Kanban(2).png)