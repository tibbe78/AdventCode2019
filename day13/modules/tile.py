from dataclasses import dataclass

@dataclass
class Tile:
    ''' Class of one tile on the screen '''
    def __init__(self, x, y, tileType):
        self.x = x
        self.y = y
        self.tileType = tileType
        self.name = "T_X:{}_Y:{}".format(self.x, self.y)

    def __repr__(self):
        return self.name