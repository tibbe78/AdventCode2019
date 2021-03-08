#!/usr/bin/env python3

# --- Day 8: Space Image Format ---
# Part One

import sys, string

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



layerinfo = list()
# Count the zeros in each layer
for layer in range(len(imgLayers)):
    numZeros = 0
    for height in range(imgHeight):
        for width in range(imgWidth):
            if imgLayers[layer][height][width] == 0: numZeros +=1
    layerinfo.append(numZeros)

# find layer with fewest zeros
zeroes = 999
leastZeroLayer = 999
for num in range(len(layerinfo)):
    if zeroes > layerinfo[num]:
        zeroes = layerinfo[num]
        leastZeroLayer = num

# Count 1 * count 2
ones = 0
twos = 0
for height in range(imgHeight):
    for width in range(imgWidth):
        if imgLayers[leastZeroLayer][height][width] == 1: ones +=1
        elif imgLayers[leastZeroLayer][height][width] == 2: twos +=1

answer = ones * twos
print("The Answer is: {}".format(answer))