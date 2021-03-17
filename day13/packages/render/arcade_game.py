"""[summary]
The arcade game engine to draw game to screen
"""
import sys
from typing import List
import arcade
from pyglet.libs.win32.constants import TRUE
from day13.packages.logic.computer.maincode import MainCode

COLOREMPTY = arcade.color.BLACK
COLORWALLS = arcade.color.WHITE
COLORBLOCKS = arcade.color.BLUEBERRY
COLORPADDLE = arcade.color.RED
COLORBALL = arcade.color.YELLOW


class ArcadeWindow(arcade.Window):
    def __init__(self):
        self.time_elapsed = 0.0
        # Scale the image so it's easier to see
        self.imgScale = 20
        self.scale = float(self.imgScale) - 2
        self.paused = False
        # 0 is an empty tile. No game object appears in this tile.
        # 1 is a wall tile. Walls are indestructible barriers.
        # 2 is a block tile. Blocks can be broken by the ball.
        # 3 is a horizontal paddle tile. The paddle is indestructible.
        # 4 is a ball tile. The ball moves diagonally and bounces off objects.
        self.topscore = 40
        self.imgWidth = 41 * self.imgScale
        self.imgHeight = 24 * self.imgScale + self.topscore  # 100 pix for text at top
        super().__init__(self.imgWidth, self.imgHeight, "Day13_2 arcade window")
        arcade.set_background_color(COLOREMPTY)
        self.mainCode = None
        self.updateNum = 0
        self.graphNum = 0
        self.finished = 0

    def setup(self, opCodeList: List, startValue: int):
        """ Set up the game here. Call this function to restart the game. """
        self.mainCode = MainCode(opCodeList, startValue)

    def start(self):
        arcade.run()

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing
        Arguments:
            delta_time {float} -- Time since the last update
        """

        self.updateNum += 1
        # If paused, don't update anything
        if self.paused:
            return
        # Update everything
        codeBack = self.mainCode.runCodeOnce()
        if (codeBack == 0):
            self.quit()
        if (codeBack == 1):
            pass  # ok
        if (codeBack == 2):
            self.finished = TRUE

    def on_draw(self):
        """
        Render the screen.
        """
        self.graphNum += 1
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # start_x and start_y make the start point for the text.
        # We draw a dot to make it easy too see
        # the text in relation to its start x and y.
        # Create the image
        for tile in self.mainCode.flipper.screen.grid.keys():
            scaleX = (
                (self.mainCode.flipper.screen.grid[tile].x) * self.imgScale) + self.imgScale
            scaleY = (
                (self.mainCode.flipper.screen.grid[tile].y) * self.imgScale) + self.imgScale
            # draw pixel but scaled
            if self.mainCode.flipper.screen.grid[tile].type == 1:
                arcade.draw_rectangle_filled(
                    scaleX, scaleY, self.scale, self.scale, COLORWALLS)
            elif self.mainCode.flipper.screen.grid[tile].type == 2:
                arcade.draw_rectangle_filled(
                    scaleX, scaleY, self.scale, self.scale, COLORBLOCKS)
            elif self.mainCode.flipper.screen.grid[tile].type == 3:
                arcade.draw_rectangle_filled(
                    scaleX, scaleY, self.scale, self.scale, COLORPADDLE)
            elif self.mainCode.flipper.screen.grid[tile].type == 4:
                arcade.draw_rectangle_filled(
                    scaleX, scaleY, self.scale, self.scale, COLORBALL)

        arcade.draw_text(
            f"Graphics number:{self.graphNum} Update number:{self.updateNum}",
            10,
            self.imgHeight-20,
            arcade.color.WHITE_SMOKE,
            12,
        )
        arcade.finish_render

        if self.finished:
            arcade.pause(5)
            self.quit()

    def quit(self):
        arcade.close_window()
        sys.exit(0)
