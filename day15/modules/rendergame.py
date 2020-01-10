"""
renders game via pygame
"""
import pygame
import sys
from day15.modules.robot import Robot
from day15.modules.plate import Plate
from pygame.locals import *

# Storage types for Plates
EMPTY = 0
WALL = 1
EXIT = 2

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_EMPTY = (40, 40, 40)
COLOR_WALL = (180, 180, 180)
COLOR_EXIT = (30, 144, 255)
COLOR_ROBOT = (220, 20, 60)


# Scale the image so it's easier to see
IMAGE_SCALE = 10

IMAGE_WIDTH = 1800
IMAGE_HEIGHT = 1000

# Size of the rectangles...
PIXEL_SIZE = IMAGE_SCALE - 1

class RenderGame():
    ''' Draws the screen image with pygame '''

    @staticmethod
    def init_game() -> object:
        ''' init the game engine '''
        pygame.init()
        return pygame.display.set_mode((IMAGE_WIDTH, IMAGE_HEIGHT), 0, 32)

    @staticmethod
    def update_game(robot: Robot, display: object):
        ''' write to pygame output to show screen '''

        # Draw black background
        display.fill(COLOR_BLACK)

        # Draw all plates (pixels)
        for plate in robot.hull.values():
            x_scaled = (plate.position.x * IMAGE_SCALE) + (IMAGE_WIDTH / 2)
            y_scaled = (plate.position.y * IMAGE_SCALE) + (IMAGE_HEIGHT / 2)

            if plate.type == 0:
                pixel_color = COLOR_EMPTY
            elif plate.type == 1:
                pixel_color = COLOR_WALL
            elif plate.type == 2:
                pixel_color = COLOR_EXIT
            rectangle = pygame.Rect(x_scaled, y_scaled, PIXEL_SIZE, PIXEL_SIZE)
            pygame.draw.rect(display, pixel_color, rectangle)

        # Draw Robot
        x_scaled = (robot.position.x * IMAGE_SCALE) + (IMAGE_WIDTH / 2)
        y_scaled = (robot.position.y * IMAGE_SCALE) + (IMAGE_HEIGHT / 2)
        rectangle = pygame.Rect(x_scaled, y_scaled, PIXEL_SIZE, PIXEL_SIZE)
        pygame.draw.rect(display, COLOR_ROBOT, rectangle)

        # Check if the game quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.flip()


    @staticmethod
    def quit_game():
        ''' quit the game '''
        pygame.quit()
        sys.exit(0)
