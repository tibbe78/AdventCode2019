"""renders via pygame
"""
import pygame
import sys
from pygame.locals import *
from day15.modules.robot import Robot
from day15.modules.hull import Plate

#from day13.modules.screen import Screen


class RenderGame():
    ''' Draws the screen image with pygame '''
    # Colors
    colors = None
    colors.empty = (0, 0, 0)
    colors.walls = (255, 255, 255)
    colors.oxygen = (30, 144, 255)
    colors.robot = (220, 20, 60)

    # Scale the image so it's easier to see
    imgScale = 20

    pygame.init()

    imgWidth = 100 * imgScale
    imgHeight = 100 * imgScale

    display = pygame.display.set_mode((imgWidth, imgHeight), 0, 32)

    @staticmethod
    def update_game(robot):
        ''' write to pygame output to show screen '''
        RenderGame.display.fill(RenderGame.colors.empty)
        for plate in robot.grid.values():
            x_scaled = plate.pos_x * RenderGame.imgScale
            y_scaled = plate.pos_y * RenderGame.imgScale

            if plate.type == 0:
                color = RenderGame.colors.empty
            elif plate.type == 1:
                color = RenderGame.colors.walls
            elif plate.type == 2:
                color = RenderGame.colors.block
            elif plate.type == 3:
                color = RenderGame.colors.paddle
            elif plate.type == 4:
                color = RenderGame.colors.ball
            rect_size = RenderGame.imgScale - 1
            rectangle = pygame.Rect(x_scaled, y_scaled, rect_size, rect_size)
            pygame.draw.rect(RenderGame.display, color, rectangle)

        pygame.display.update()
        pygame.time.delay(1000)

    @staticmethod
    def quit_game():
        ''' quit the game '''
        pygame.time.delay(3000)
        pygame.quit()
