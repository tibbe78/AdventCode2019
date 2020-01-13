''' Class of the hull of the ship that is a grid of plates '''

from dataclasses import dataclass
from typing import TypedDict

@dataclass
class Plate():
    ''' Class of one plate of the hull, like a pixel. '''

    def __init__(self, position_x: int, position_y: int, _type=0):
        # x, y position
        self.position_x = position_x
        self.position_y = position_y
        # What type of plate it is (empty, wall, exit)
        self.type = _type
        self.times_traversed = 1
        self.name = f"x{self.position_x}_y{self.position_y}"

    def __repr__(self):
        return self.name

@dataclass
class Point(TypedDict):
    ''' Class of one plate of the hull, like a pixel. '''
    # x, y position
    position_x: int = 0
    position_y: int = 0
    # What type of plate it is (empty, wall, exit)
    kind: int = 0
    times_traversed = 1
    name = f"x{position_x}_y{position_y}"

    def __repr__(self):
        return self.name
