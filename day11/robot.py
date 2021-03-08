from dataclasses import dataclass
from day11.hull import Hull
from day11.hullplate import Plate

@dataclass
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        # 0=up, 1=right, 2=down, 3=left
        self.direction = 0
        self.outputstate = 0
        # The hull of the ship.
        self.hull = Hull()
        self.firstPlate = 1

    def Move(self):
        # Take on step in direction
        if self.direction == 0: self.y += 1
        elif self.direction == 1: self.x += 1
        elif self.direction == 2: self.y -= 1
        elif self.direction == 3: self.x -= 1

    def DetectColor(self) -> int:
        # Get the color of tile 0=black 1=white
        if self.firstPlate == 1:
            return self.hull.getColor(Plate(self.x, self.y, 1))
            self.firstPlate = 0
        else:
            return self.hull.getColor(Plate(self.x, self.y))

    def Paint(self, color:int):
        # paint color of tile 0=black 1=white
        self.hull.SetColor(Plate(self.x, self.y, color))

    def Turn(self, heading:int):
        if heading == 0:
            self.direction -=1
            if self.direction == -1: self.direction = 3
        elif heading == 1:
            self.direction +=1
            if self.direction == 4: self.direction = 0
        else: print("Errror Turning")
        self.Move()

    def HandleOutput(self, output):
        if self.outputstate == 0:
            self.outputstate = 1
            self.Paint(output)
        else:
            self.outputstate = 0
            self.Turn(output) 
