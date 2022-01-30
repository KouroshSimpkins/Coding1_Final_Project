# Building a Multiplayer Game of Battleships Using Python

**What is this repository?**

This repository contains the code for a game of Battleships. I wrote this code for the final project of my coding_1 module during my BSc in Creative Computing.

> For an explanation of the game of battleships look at Writeup.docx.

To run the game, run the file titled "battleships.py" in the terminal.
There are no other external requirements, all the modules utilised are part of the standard library. Ensure you have both the file class_board.py and class_ship.py in the same directory as battleships.py.

The game itself relies on an honor system, there is currently no way to check if a player is cheating by looking at the other players board.

I decided to write the game in the terminal, as it allows me to see my ability to write a game without relying on an engine, regardless of how low level the engine is.
This is just a personal preference, there is nothing to say that the game could not be written to run as a pygame version, however I believe that it works just fine as a textbased game.

The codebase is laid out as follows, the main file is battleships.py. This contains the majority of the game logic and functionality for the game (i.e. main menu, board storage, ships etc.). Supplementing this code there are two other files, class_board and class_ship. These contain the classes for the board and the ship.

The other files are not important for the running of the program. They are programs I wrote for my personal testing/preparation. As such you can see a lot of my thought process, as well as how I refactored a lot of code around to reach this final project.

Enjoy!
