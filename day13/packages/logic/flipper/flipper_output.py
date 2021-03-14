from dataclasses import dataclass
@dataclass
class FlipperOutput:
    x: int = 0
    y: int = 0
    type: int = 0
    state: int = 0

    def update(self, data):
        if self.state == 0:
            self.state += 1
            self.x = data
        elif self.state == 1:
            self.state += 1
            self.y = data
        elif self.state == 2:
            self.state = 0
            self.type = data