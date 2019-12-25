from dataclasses import dataclass
from day13.modules.output import Output
#from typing import Dict

@dataclass
class Ball:
    ''' Class of the Ball '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.nextX = 0
        self.nextY = 0
        self.direction = 0

    def Update(self, output: Output):
        if self.x > output.x:
            self.direction = -1
            self.nextX = output.x - 1
        elif self.x < output.x:
            self.direction = 1
            self.nextX = output.x + 1
        else: self.direction = 0

        if self.y > output.y:
            self.nextY = output.y - 1
        elif self.y < output.y:
            self.nextY = output.y + 1
        self.x = output.x
        self.y = output.y

