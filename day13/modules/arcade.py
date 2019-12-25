from dataclasses import dataclass
from day13.modules.screen import Screen
from day13.modules.tile import Tile
from day13.modules.score import Score
from day13.modules.ball import Ball
from day13.modules.paddle import Paddle
from day13.modules.output import Output
from day13.modules.rendergame import RenderGame

@dataclass
class Arcade:
    """ class of the Arcade cabinet """

    def __init__(self):
        # The screen of the arcade cabinet
        self.screen = Screen()
        self.score = Score()
        self.ball = Ball()
        self.paddle = Paddle()
        # Temp storage for the output.
        self.output = Output()
        # 0 = neutral, -1 = left, 1 = right
        self.joystickPosition = 0

    def  UpdatePaddle(self):
        if self.output.type == 3:
            self.paddle.Update(self.output)

    def  UpdateBall(self):
        if self.output.type == 4:
            self.ball.Update(self.output)

    def HandleOutput(self, data):
        self.output.Update(data)
        if self.output.state == 0:
            if self.output.x == -1 and self.output.y == 0:
                self.score.UpdateScore(self.output.type)
            else:
                self.UpdateBall()
                self.UpdatePaddle()
                self.screen.SetType(Tile(self.output.x,self.output.y, self.output.type))

    def GetJoystickPos(self) -> int:
        if self.ball.x > self.paddle.x: self.joystickPosition = 1
        elif self.ball.x < self.paddle.x: self.joystickPosition = -1
        else: self.joystickPosition = 0
        RenderGame.Update(self)
        return self.joystickPosition

