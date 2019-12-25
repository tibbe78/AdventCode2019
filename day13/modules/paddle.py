from dataclasses import dataclass
from day13.modules.output import Output
#from typing import Dict

@dataclass
class Paddle:
    ''' Class of the Paddle '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def Update(self, output: Output):
        if self.x > output.x: self.direction = -1
        elif self.x < output.x: self.direction = 1
        else: self.direction = 0
        self.x = output.x
        self.y = output.y

