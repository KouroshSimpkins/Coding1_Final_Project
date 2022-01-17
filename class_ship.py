"""this module contains the code for the ship class"""


class Ship:
    """The ship class"""
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
        self.sunk = False

    def hit(self):
        """When called record a hit.
        If the number of hits is the same as the length, sunk is true."""
        self.hits += 1
        if self.hits == self.size:
            self.sunk = True

    def record_position(self, coordinates):
        """Record the position of the ship on the board"""
        self.positions.append(coordinates)

    def __str__(self):
        """Return a string representation of the ship"""
        return self.name
