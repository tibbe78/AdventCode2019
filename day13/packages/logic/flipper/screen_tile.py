from dataclasses import dataclass
@dataclass
class ScreenTile:
    """ Class of one tile on the screen """

    def __init__(self, x: int, y: int, tiletype: int):
        self.x = x
        self.y = y
        self.type = tiletype
        self.name = "T_X:{}_Y:{}".format(x, y)

    def __repr__(self):
        return self.name