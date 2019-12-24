import pygame
import sys
from pygame.locals import *
#from day13.modules.screen import Screen

class DrawScreen():
    ''' Draws the screen image with pygame '''
    # Colors
    empty=(0,0,0)
    walls=(255,255,255)
    block=(30,144,255)
    paddle=(220,20,60)
    ball=(255,215,0)

    # Scale the image so it's easier to see
    imgScale = 20

    pygame.init()

    # 0 is an empty tile. No game object appears in this tile.
    # 1 is a wall tile. Walls are indestructible barriers.
    # 2 is a block tile. Blocks can be broken by the ball.
    # 3 is a horizontal paddle tile. The paddle is indestructible.
    # 4 is a ball tile. The ball moves diagonally and bounces off objects.


    imgWidth = 40 * imgScale
    imgHeight = 24 * imgScale

    display=pygame.display.set_mode((imgWidth,imgHeight),0,32)

    @staticmethod
    def Update(screen):
        # Scale the image so it's easier to see
        DrawScreen.display.fill(DrawScreen.empty)
        for tile in screen.grid.keys():
            scaleX = (screen.grid[tile].x) * DrawScreen.imgScale
            scaleY = (screen.grid[tile].y) * DrawScreen.imgScale
            if screen.grid[tile].tileType == 0: color = DrawScreen.empty
            elif screen.grid[tile].tileType == 1: color = DrawScreen.walls
            elif screen.grid[tile].tileType == 2: color = DrawScreen.block
            elif screen.grid[tile].tileType == 3: color = DrawScreen.paddle
            elif screen.grid[tile].tileType == 4: color = DrawScreen.ball

            pygame.draw.rect(DrawScreen.display, color, pygame.Rect(scaleX, scaleY, DrawScreen.imgScale-1, DrawScreen.imgScale-1))
        pygame.display.update()

    @staticmethod
    def Quit(screen):
        pygame.time.delay(5000)
        pygame.quit()
