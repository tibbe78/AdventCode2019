from dataclasses import dataclass
from day13.modules.tile import Tile
#from typing import Dict
from day13.modules.drawscreen import DrawScreen

@dataclass
class Screen:
    ''' Class of the the screen of the Arcade, it contains tiles '''
    def __init__(self):
        # directory of Screen Tiles
        self.grid = dict()
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0

    def AddTile(self, tile: Tile):
        if tile.x > self.maxX: self.maxX = tile.x
        if tile.y > self.maxY: self.maxY = tile.y
        if tile.x < self.minX: self.minX = tile.x
        if tile.y < self.minY: self.minY = tile.y
        self.grid[tile.name] = tile

    def CheckIfExists(self, tile: Tile):
        if not tile.name in self.grid.keys():
            self.AddTile(tile)

    def GetType(self, tile: Tile) -> int:
        self.CheckIfExists(tile)
        return self.grid[tile.name].tileType

    def SetType(self, tile):
        self.CheckIfExists(tile)
        self.grid[tile.name].tileType = tile.tileType
        DrawScreen.Update(self)