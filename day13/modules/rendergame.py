"""[summary]
"""
import pygame
import sys
from pygame.locals import *

#from day13.modules.screen import Screen

class RenderGame():
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

    topscore = 40

    imgWidth = 40 * imgScale
    imgHeight = 24 * imgScale + topscore # 100 pix for text at top

    display=pygame.display.set_mode((imgWidth,imgHeight),0,32)
    font = pygame.font.Font(None, 30)

    frame = 0

    @staticmethod
    def Update(arcade):
        text = RenderGame.font.render("Score: {}".format(arcade.score.value), True, (255, 255, 255))
        RenderGame.display.fill(RenderGame.empty)
        for tile in arcade.screen.grid.keys():
            scaleX = (arcade.screen.grid[tile].x) * RenderGame.imgScale
            scaleY = (arcade.screen.grid[tile].y) * RenderGame.imgScale
            if arcade.screen.grid[tile].type == 0: color = RenderGame.empty
            elif arcade.screen.grid[tile].type == 1: color = RenderGame.walls
            elif arcade.screen.grid[tile].type == 2: color = RenderGame.block
            elif arcade.screen.grid[tile].type == 3: color = RenderGame.paddle
            elif arcade.screen.grid[tile].type == 4: color = RenderGame.ball

            pygame.draw.rect(RenderGame.display, color, pygame.Rect(scaleX, scaleY + RenderGame.topscore, RenderGame.imgScale - 1, RenderGame.imgScale - 1))
        RenderGame.display.blit(text, (10, 2))
        pygame.display.update()
        RenderGame.frame += 1
        pygame.image.save(RenderGame.display, "./capture/{}.png".format(RenderGame.frame))
        #pygame.time.delay(500)


    @staticmethod
    def Quit():
        pygame.time.delay(5000)
        pygame.quit()
