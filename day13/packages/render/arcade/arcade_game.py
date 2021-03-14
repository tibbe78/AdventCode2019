"""[summary]
The arcade game engine to draw game to screen
"""
import arcade
import sys
import time
from numbers import Number
import gc
import os

# Colors
colorEmpty = arcade.color.BLACK
colorWalls = arcade.color.WHITE
colorBlock = arcade.color.BLUEBERRY
colorPaddle = arcade.color.RED
colorBall = arcade.color.YELLOW


class ArcadeWindow(arcade.Window):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(colorEmpty)
        self.time_elapsed = 0.0
        # Scale the image so it's easier to see
        self.imgScale = 20
        self.paused = False

        # 0 is an empty tile. No game object appears in this tile.
        # 1 is a wall tile. Walls are indestructible barriers.
        # 2 is a block tile. Blocks can be broken by the ball.
        # 3 is a horizontal paddle tile. The paddle is indestructible.
        # 4 is a ball tile. The ball moves diagonally and bounces off objects.
        self.topscore = 40
        self.imgWidth = 40 * self.imgScale
        self.imgHeight = 24 * self.imgScale + self.topscore  # 100 pix for text at top

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def start(self):
        arcade.run()

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing
        Arguments:
            delta_time {float} -- Time since the last update
        """
        # If paused, don't update anything
        if self.paused:
            return
        # Update everything
        self.time_elapsed += delta_time   


    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # start_x and start_y make the start point for the text.
        # We draw a dot to make it easy too see
        # the text in relation to its start x and y.
        start_x = 50
        start_y = 450
        arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text(
            "Simple line of text in 12 point",
            start_x,
            start_y,
            arcade.color.WHITE_SMOKE,
            12,
        )
        arcade.finish_render

    def quit(self):
        arcade.pause(5)
        arcade.close_window()
