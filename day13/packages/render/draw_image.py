
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from day13.packages.logic.flipper.screen_tile import ScreenTile

def DrawImage(screen: ScreenTile):
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

    imgWidth = (screen.maxX + 1) * imgScale
    imgHeight = (screen.maxY + 1) * imgScale

    # Create the RGB image with
    img = Image.new(mode = "RGB", size = (imgWidth,imgHeight))
    draw = ImageDraw.Draw(img)
    # Create the image
    for tile in screen.grid.keys():
        scaleX = (screen.grid[tile].x) * imgScale
        scaleY = (screen.grid[tile].y) * imgScale
        # draw pixel but scaled

        if screen.grid[tile].type == 1: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=walls)
        elif screen.grid[tile].type == 2: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=block)
        elif screen.grid[tile].type == 3: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=paddle)
        elif screen.grid[tile].type == 4: draw.rectangle([(scaleX, scaleY), (scaleX+imgScale-2, scaleY+imgScale-2)], fill=ball)
    rotated = img.rotate(180)
    flipped = ImageOps.mirror(rotated)
    img.show()