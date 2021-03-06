from day11.hullplate import Plate
from dataclasses import dataclass

@dataclass
class Hull:
    ''' Class of the hull of the ship containing lots of plates '''
    def __init__(self):
        # directory of Grid Plates
        self.grid = {}
        self.minX = 0
        self.maxX = 0
        self.minY = 0
        self.maxY = 0
    
    def AddPlate(self, plate: Plate):
        if plate.x > self.maxX: self.maxX = plate.x
        if plate.y > self.maxY: self.maxY = plate.y
        if plate.x < self.minX: self.minX = plate.x
        if plate.y < self.minY: self.minY = plate.y
        self.grid[plate.name] = plate
        
    def CheckIfExists(self, plate: Plate):
        if not plate.name in self.grid.keys(): 
            self.AddPlate(plate)
    
    def getColor(self, plate) -> int:
        self.CheckIfExists(plate)
        return self.grid[plate.name].color
    
    def SetColor(self, plate):
        self.CheckIfExists(plate)
        self.grid[plate.name].color = plate.color
        self.grid[plate.name].timesTraversed += 1

