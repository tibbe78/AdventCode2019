''' Class of the hull of the ship that is a grid of plates '''

from dataclasses import dataclass
from day15.modules.utils import Vector2D

@dataclass
class Plate:
    ''' Class of one plate of the hull, like a pixel. '''

    def __init__(self, x, y, _type=0):
        # x, y position
        self.position = Vector2D(x, y)
        # What type of plate it is (empty, wall, exit)
        self.type = _type
        self.times_traversed = 1
        self.name = f"x{self.position.x}_y{self.position.y}"

    def __repr__(self):
        return self.name
