from dataclasses import dataclass
from .flipper_output import FlipperOutput

@dataclass
class Ball:
    x:int = 0
    y:int = 0
    nextX:int = 0
    nextY:int = 0
    direction:int = 0

    def update(self, output: FlipperOutput):
        if self.x > output.x:
            self.direction = -1
            self.nextX = output.x - 1
        elif self.x < output.x:
            self.direction = 1
            self.nextX = output.x + 1
        else:
            self.direction = 0
        if self.y > output.y:
            self.nextY = output.y - 1
        elif self.y < output.y:
            self.nextY = output.y + 1
        self.x = output.x
        self.y = output.y