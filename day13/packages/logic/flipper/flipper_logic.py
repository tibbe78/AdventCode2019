from dataclasses import dataclass, field
from typing import List, Dict, Type
from .screen_tile import ScreenTile
from .flipper_output import FlipperOutput
from .ball import Ball
from .paddle import Paddle
from .virtual_screen import VirtualScreen

class FlipperLogic:
    """ class of the Flipper login of the Arcade cabinet """

    def __init__(self):
        # The screen of the arcade cabinet
        self.screen = VirtualScreen()
        self.score = 0
        self.ball = Ball()
        self.paddle = Paddle()
        # Temp storage for the output.
        self.output = FlipperOutput()
        # 0 = neutral, -1 = left, 1 = right
        self.joystickPosition = 0

    def UpdatePaddle(self):
        if self.output.type == 3:
            self.paddle.update(self.output)

    def UpdateBall(self):
        if self.output.type == 4:
            self.ball.update(self.output)

    def HandleOutput(self, data):
        self.output.update(data)
        if self.output.state == 0:
            if self.output.x == -1 and self.output.y == 0:
                self.score = self.output.type
            else:
                self.UpdateBall()
                self.UpdatePaddle()
                self.screen.SetType(
                    ScreenTile(self.output.x, self.output.y, self.output.type)
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


