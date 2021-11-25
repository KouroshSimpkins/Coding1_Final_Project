"""Working out the basic logic for a game of battleships built using Python"""

# Implement a text based game of battleships
#
# 1. The computer will generate a grid that is 5 columns by 5 rows.
# 2. The computer will then generate 5 random hidden ships on the grid.
# 3. The player will then have to guess where the hidden ships are.
# 4. The player will then be told if their guess was a hit or a miss.
# 5. The player will then be told if they have won or lost the game.
# 6. The player will then be asked if they would like to play again.
# 7. The game will then repeat from step 2.

import numpy as np
import random
import time

# Ask the player to choose the size of the grid
print("Welcome to Battleships!")
print("Please choose the size of the grid:")
print("1. 5x5")
print("2. 10x10")
print("3. 15x15")
print("4. 20x20")
print("5. 25x25")
grid_size = int(input("Please enter your choice: "))

# Create a grid the size that the player has selected
if grid_size == 1:
    grid_size = 5
elif grid_size == 2:
    grid_size = 10
elif grid_size == 3:
    grid_size = 15
elif grid_size == 4:
    grid_size = 20
elif grid_size == 5:
    grid_size = 25
else:
    print("Invalid input. Please try again.")
    exit()


# Create a grid of the size that the player has selected
grid = np.zeros((grid_size, grid_size))

# Print the grid, but strip any items from a list
def print_grid(grid):
    for row in grid:
        print(row)


# define a structure for the ships
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []


# Create a list of ships
ships = [
    Ship("Carrier", 5),
    Ship("Battleship", 4),
    Ship("Cruiser", 3),
    Ship("Submarine", 3),
    Ship("Destroyer", 2)
]
