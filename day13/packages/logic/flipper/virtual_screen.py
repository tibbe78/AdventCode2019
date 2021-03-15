from dataclasses import dataclass, field
from typing import List, Dict, Type
from .screen_tile import ScreenTile

@dataclass
class VirtualScreen:
    """ Class of the the screen of the Arcade, it contains tiles """
    grid: Dict[str,Type[ScreenTile]] = field(default_factory=dict)
    minX:int = 0
    maxX:int = 0
    minY:int = 0
    maxY:int = 0

    def addTile(self, tile: ScreenTile):
        if tile.x > self.maxX:
            self.maxX = tile.x
        if tile.y > self.maxY:
            self.maxY = tile.y
        if tile.x < self.minX:
            self.minX = tile.x
        if tile.y < self.minY:
            self.minY = tile.y
        self.grid[tile.name] = tile

    def checkIfExists(self, tile: ScreenTile):
        if not tile.name in self.grid.keys():
            self.addTile(tile)

    def setType(self, tile):
        self.checkIfExists(tile)
        self.grid[tile.name].type = tile.type

    def countBlockTiles(self):
        """ Count Block tiles """
        i = 0
        for tile in self.grid.keys():
            if self.grid[tile].type == 2:
                i += 1
        print("There are {} blocks on the screen.".format(i))