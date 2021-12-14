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

import random
import time
import numpy as np
# Generate a grid of 5 rows and 5 columns
grid = np.zeros((5, 5))


def generate_grid():
    """Generate a grid of 5 rows and 5 columns"""
    grid = np.zeros((5, 5))
    return grid


def generate_ships(grid):
    """Generate 5 random hidden ships on the grid"""
    ships = []
    for i in range(5):
        ships.append(random.randint(0, 4))
    return ships


def print_grid(grid):
    """Print the grid"""
    print(grid)


def get_guess():
    """Get the user's guess"""
    guess = input("Enter a guess: ")
    return guess


def check_guess(guess, ships):
    """Check if the guess is a hit or a miss"""
    if guess in ships:
        print("Hit!")
    else:
        print("Miss!")


def play_again():
    """Ask the user if they would like to play again"""
    play_again = input("Would you like to play again? (y/n): ")
    return play_again


def main():
    """Run the game"""
    grid = generate_grid()
    ships = generate_ships(grid)
    print_grid(grid)
    guess = get_guess()
    check_guess(guess, ships)
    if play_again() == "y":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

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
