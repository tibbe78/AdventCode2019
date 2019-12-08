#! /usr/bin/python

# --- Day 8: Space Image Format ---
# Part Two

import sys, string
from PIL import Image
from PIL import ImageDraw

# Should we debug or not.
debug = False

imgWidth = 25
imgHeight = 6

try:  
    file = open('day08_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)


# Read first line and strip end '\n' put it in a list
imgList = list(file.readline().strip())
if debug: print("Raw file data {}".format(imgList))
# Close the file.
file.close()

# The layers
imgLayers = list()


# Create the layers with a 3 dimensional list
layer = 0
i = 0
while i < len(imgList):
    imgLayers.append(list())
    for height in range(imgHeight):
        imgLayers[layer].append(list())
        for width in range(imgWidth):
            imgLayers[layer][height].append(list())
            imgLayers[layer][height][width] = int(imgList[i])
            i += 1
    layer += 1

# 0 = black
# 1 = white
# 2 = transparent (ignore)

# Scale the image so it's easier to see
imgScale = 10

# Create the black & white image with one value size 25 x 6 * scale
img = Image.new('1', (imgWidth*imgScale,imgHeight*imgScale))
draw = ImageDraw.Draw(img)

# Create the image
for height in range(imgHeight):
    for width in range(imgWidth):
        pixelval = 3
        for layer in range(len(imgLayers)):
            if imgLayers[layer][height][width] == 0:
                if pixelval == 3: 
                    pixelval = 0
                    break
            elif imgLayers[layer][height][width] == 1:
                if pixelval == 3: 
                    pixelval = 1
                    break
        scalex = width * imgScale
        scaley = height * imgScale
        # draw pixel but scaled
        if pixelval == 1: draw.rectangle([(scalex, scaley), (scalex+imgScale-1, scaley+imgScale-1)], fill=True)    
img.show() 