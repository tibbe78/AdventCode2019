from dataclasses import dataclass, field
from typing import List, Dict, Type

@dataclass
class Output:
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


@dataclass
class Tile:
    """ Class of one tile on the screen """

    def __init__(self, x: int, y: int, tiletype: int):
        self.x = x
        self.y = y
        self.type = tiletype
        self.name = "T_X:{}_Y:{}".format(x, y)

    def __repr__(self):
        return self.name


@dataclass
class Paddle:
    x: int = 0
    y: int = 0
    direction: int = 0

    def update(self, output: Output):
        if self.x > output.x:
            self.direction = -1
        elif self.x < output.x:
            self.direction = 1
        else:
            self.direction = 0
        self.x = output.x
        self.y = output.y


@dataclass
class Ball:
    x:int = 0
    y:int = 0
    nextX:int = 0
    nextY:int = 0
    direction:int = 0

    def update(self, output: Output):
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


@dataclass
class Screen:
    """ Class of the the screen of the Arcade, it contains tiles """
    grid: Dict[str,Type[Tile]] = field(default_factory=dict)
    minX:int = 0
    maxX:int = 0
    minY:int = 0
    maxY:int = 0

    def AddTile(self, tile: Tile):
        if tile.x > self.maxX:
            self.maxX = tile.x
        if tile.y > self.maxY:
            self.maxY = tile.y
        if tile.x < self.minX:
            self.minX = tile.x
        if tile.y < self.minY:
            self.minY = tile.y
        self.grid[tile.name] = tile

    def CheckIfExists(self, tile: Tile):
        if not tile.name in self.grid.keys():
            self.AddTile(tile)

    def SetType(self, tile):
        self.CheckIfExists(tile)
        self.grid[tile.name].type = tile.type

    def CountBlockTiles(self):
        """ Count Block tiles """
        i = 0
        for tile in self.grid.keys():
            if self.grid[tile].type == 2:
                i += 1
        print("There are {} blocks on the screen.".format(i))


class FlipperLogic:
    """ class of the Arcade cabinet """

    def __init__(self):
        # The screen of the arcade cabinet
        self.screen = Screen()
        self.score = 0
        self.ball = Ball()
        self.paddle = Paddle()
        # Temp storage for the output.
        self.output = Output()
        # 0 = neutral, -1 = left, 1 = right
        self.joystickPosition = 0

    def UpdatePaddle(self):
        if self.output.type == 3:
            self.paddle.Update(self.output)

    def UpdateBall(self):
        if self.output.type == 4:
            self.ball.Update(self.output)

    def HandleOutput(self, data):
        self.output.update(data)
        if self.output.state == 0:
            if self.output.x == -1 and self.output.y == 0:
                self.score = self.output.type
            else:
                self.UpdateBall()
                self.UpdatePaddle()
                self.screen.SetType(
                    Tile(self.output.x, self.output.y, self.output.type)
                )

    def GetJoystickPos(self) -> int:
        if self.ball.x > self.paddle.x:
            self.joystickPosition = 1
        elif self.ball.x < self.paddle.x:
            self.joystickPosition = -1
        else:
            self.joystickPosition = 0
        # Wait for screen update
        return self.joystickPosition


