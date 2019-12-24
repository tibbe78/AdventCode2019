
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from day13.modules.arcade import Arcade


def DrawImage(arcade: Arcade):
    ''' Draws the hull image '''


    # 0 is an empty tile. No game object appears in this tile.
    # 1 is a wall tile. Walls are indestructible barriers.
    # 2 is a block tile. Blocks can be broken by the ball.
    # 3 is a horizontal paddle tile. The paddle is indestructible.
    # 4 is a ball tile. The ball moves diagonally and bounces off objects.

    empty=(0,0,0)
    walls=(255,255,255)
    block=(30,144,255)
    paddle=(220,20,60)
    ball=(255,215,0)


    # Scale the image so it's easier to see
    imgScale = 20

    imgWidth = (arcade.screen.maxX + 1) * imgScale
    imgHeight = (arcade.screen.maxY + 1) * imgScale

    # Create the RGB image with
    img = Image.new(mode = "RGB", size = (imgWidth,imgHeight))
    draw = ImageDraw.Draw(img)
    # Create the image
    for tile in arcade.screen.grid.keys():
        scaleX = (arcade.screen.grid[tile].x) * imgScale
        scaleY = (arcade.screen.grid[tile].y) * imgScale
        # draw pixel but scaled

        if arcade.screen.grid[tile].tileType == 1: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=walls)
        elif arcade.screen.grid[tile].tileType == 2: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=block)
        elif arcade.screen.grid[tile].tileType == 3: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=paddle)
        elif arcade.screen.grid[tile].tileType == 4: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=ball)
    rotated = img.rotate(180)
    flipped = ImageOps.mirror(rotated)
    img.show()