from dataclasses import dataclass
from .flipper_output import FlipperOutput
@dataclass
class Paddle:
    x: int = 0
    y: int = 0
    direction: int = 0

    def update(self, output: FlipperOutput):
        if self.x > output.x:
            self.direction = -1
        elif self.x < output.x:
            self.direction = 1
        else:
            self.direction = 0
        self.x = output.x
        self.y = output.y