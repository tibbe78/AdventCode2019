from dataclasses import dataclass
from day13.modules.screen import Screen
from day13.modules.tile import Tile
import time

@dataclass
class Arcade:
    """ class of the Arcade cabinet """

    def __init__(self):
        # The screen of the arcade cabinet
        self.screen = Screen()

        # the values we collect as output before draw to screen
        self.outputState = 0
        self.outputX = 0
        self.outputY = 0
        self.outputType = 0

    def DrawTile(self):
        # draw a tile on screen
        self.screen.SetType(Tile(self.outputX, self.outputY, self.outputType))

    def HandleOutput(self, output):
        if self.outputState == 0:
            self.outputState += 1
            self.outputX = output
        elif self.outputState == 1:
            self.outputState += 1
            self.outputY = output
        elif self.outputState == 2:
            self.outputState = 0
            self.outputType = output
            self.DrawTile()

