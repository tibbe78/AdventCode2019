# --- Day 10: Monitoring Station ---
# Part One

import sys
from dataclasses import dataclass

# Classes------------------------------------------


# Functions----------------------------------------



# Main Code -------------------------------------------------

# Example 1
# Best is 5,8 with 33 other asteroids detected:
try:  
    #file = open('day10_input.txt', 'r') 
    file = open('day10_example1.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

starMap = list()

# Loop each line in file
for line in file:
    # '.' = 0 = space
    # '#' = 4 = asteroid
    starConvDict = {'.': 0, '#': 4} # Dictionay used for converting strings to numbers
    mapLineRaw = list(line.strip())
    mapLine = [starConvDict[point] for point in mapLineRaw] # Map each point string to a value
    starMap.append(mapLine)
file.close()

# Find first Asteroid
i = 0

for x0 in range(len(starMap[0])):
    for y0 in range(len(starMap)):
        if starMap[x0][y0] == 4:
            searchX=1
            searchY=0


