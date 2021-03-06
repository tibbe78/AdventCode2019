
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from day11.robot import Robot

def DrawImage(robot :Robot):
    ''' Draws the hull image '''
    # 0 = black
    # 1 = white

    # Scale the image so it's easier to see
    imgScale = 8
    
    imgWidth = 100
    imgHeight = 100

    # Create the black & white image with one value size 25 x 6 * scale
    img = Image.new('1', (imgWidth*imgScale,imgHeight*imgScale))
    draw = ImageDraw.Draw(img)
    # Create the image
    for plate in robot.hull.grid.keys():
        scalex = (robot.hull.grid[plate].x + 30) * imgScale
        scaley = (robot.hull.grid[plate].y + 50) * imgScale
        # draw pixel but scaled
        if robot.hull.grid[plate].color == 1: draw.rectangle([(scalex, scaley), (scalex+imgScale-1, scaley+imgScale-1)], fill=True)    
    rotated = img.rotate(180)
    flipped = ImageOps.mirror(rotated)
    flipped.show() 