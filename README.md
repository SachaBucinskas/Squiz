# Squiz - Python Terminal Quiz

### Description

This is a fairly simple quiz game made for a Terminal/CLI interface made in Python 3. It reads quizes from external json files making additional quizes easy to add. Supports local Multiplayer

## Instructions and Help

### System Requirements

This should run on any mainstream operating system with Python 3 installed, as well as the [Getch module](https://pypi.org/project/getch/). Development & production was done on Ubuntu based Linux, so support may be better on Linux/MacOS/Posix, while it should work fine on Windows, testing has not been done.

### Python
This application requires [Python **3**](https://www.python.org/downloads/) to be installed on your machine. To check what version of Python you have you can run the following command

    python3 --version

If you receive "command not found" try running this command

    python --version

If this reports a version of Python 2.x.x or you receive "command not found" you can install Python 3 with the following methods on this website [here](https://realpython.com/installing-python/) or if you know what you're doing you can get the official Python 3 releases [here](https://www.python.org/downloads/)

### Dependencies
Squiz tries to rely on the standard library as much as possible, with the exception of one module, [getch](https://pypi.org/project/getch/). In order to use Squiz, you will have to install it. To install it with pip install it with either

    pip3 install getch

or

    pip install getch 

### Usage
You can start Squiz using the provided Bash launcher by using the following command

    ./script.sh

Alternatively you can start Squiz using the main.py file within the src directory directly with this command

    python3 main.py

### Launch Arguments
The following launch arguments are available:

    --help - Prints out this message with help on how to use the program

    -sp <quizFile.json> - Allows you to choose & play a quiz without going through the main menu or quiz selector. Opens <quizFile.json> from within data/quizes

    -mp <quizFile.json> - Allows you to choose & play a quiz in Multiplayer without going through the main menu or quiz selector. Opens <quizFile.json> from within data/quizes
        