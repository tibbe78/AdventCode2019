#! /usr/bin/python3
# --- Day 10: Monitoring Station ---
# Part One

import sys, math
from dataclasses import dataclass

# Classes------------------------------------------

@dataclass
class Asteroid:
    def __init__(self, x, y, visibleNeighbours = None):
        """
        Init the Class Astroid with it's position
        """
        self.x = x
        self.y = y
        self.visibleNeighbours = visibleNeighbours

# Functions----------------------------------------

def CheckIfBounds(x, y, xMax, yMax) -> bool:
    # Check if out of bounds
    if x >= xMax or x < 0 or y >= yMax or y < 0: return False
    else: return True
    
def FindObstructed(_starMap: list, asteroid1: Asteroid, asteroid2: Asteroid, xMax, yMax, astLeftToTest) -> int:
    ''' calc the diff between two asteroids and remove obstructed asteroids '''
    xDiff = asteroid2.x - asteroid1.x
    yDiff = asteroid2.y - asteroid1.y
    if xDiff == 0:
        yDiff = int(yDiff / abs(yDiff))
        GCD = 1
    elif yDiff == 0:
        xDiff = int(xDiff / abs(xDiff))
        GCD = 1
    else:
        GCD = math.gcd(xDiff,yDiff)
    x = asteroid2.x + int(xDiff/GCD)
    y = asteroid2.y + int(yDiff/GCD)
    ''' example
      0  1  2  3  4
    0 .  .  .  .  .
    1 .  #1 .  .  .
    2 .  .  .  .  .
    3 .  .  #2 .  .
    4 .  .  .  .  .
    5 .  .  .  #3 .
    x = 1 (2 - 1)
    y = 2 (3 - 1)
    hide #3
    '''       
    while CheckIfBounds(x,y,xMax,yMax):
        if _starMap[y][x] == 4:
            _starMap[y][x] = 3 # hide it.
            astLeftToTest -= 1
        x += int(xDiff/GCD)
        y += int(yDiff/GCD)
    # return the asteroids left to test.
    return astLeftToTest

def ChangeDirection(direction) -> int:
    direction += 1
    if direction > 3: return 0
    else: return direction
    
def TestAstroid(starMap2: list, _asteroid : Asteroid, _asteroidCount: int, xMax, yMax) -> int:
    # Test around the asteroid in a growing circle
    x = _asteroid.x
    y = _asteroid.y
    astLeftToTest = _asteroidCount
    direction = 0 # Right, 1 = Down, 2 = Left, 3 = Up (Like clock...)
    stepsCircle = 1 # how big is the circle in radius
    stepsTaken = 0 # How many steps have we taken.
    timesStep = 0 # two times to move before increase in stepsCircle
    visibleNeighbours = 0
    while astLeftToTest > 1: # test as long as there are viable asteroids left.
        
        ''' test around following numbers..
        6  7  8  9
        5  #  1  10
        4  3  2  11
        15 14 13 12
        '''
        
        # Take on step in direction
        if direction == 0: x += 1
        elif direction == 1: y += 1
        elif direction == 2: x -= 1
        elif direction == 3:  y -= 1
        stepsTaken += 1
        
        # Check if we have taken the circle steps
        if stepsTaken >= stepsCircle:
            direction = ChangeDirection(direction)
            stepsTaken = 0
            timesStep += 1
            # increase the circle after two times
            if timesStep >= 2:
                stepsCircle += 1
                timesStep = 0
                
        # Do tests if we are in bound in map and it's a planet
        if CheckIfBounds(x,y,xMax,yMax) and starMap2[y][x] == 4: # if there is a planet.
            #print("planet nr: {} pos x: {} y: {}".format(astLeftToTest,x,y))
            visibleNeighbours += 1
            astLeftToTest -= 1
            astLeftToTest = FindObstructed(starMap2, _asteroid, Asteroid(x,y), xMax, yMax, astLeftToTest)        
                
        
    return Asteroid(_asteroid.x,_asteroid.y,visibleNeighbours)

                

def LoopEachAstroid(_starMap: list, _asteroidCount: int) -> list:
    # Test each in X lenght and y lenght of the map
    asteroidList = list()
    xMax = len(_starMap[0])
    yMax = len(_starMap)
    for y in range(xMax):
        for x in range(yMax):
            # if there is an asteroid here (4) test it for how many visible neighbours it has.
            # 3 = hidden asteroid
            if _starMap[y][x] == 4:
                #copy the starmap to get a "deep copy"
                copyMap = list()
                for line in _starMap:
                    copyMap.append(line.copy())
                asteroidList.append(TestAstroid(copyMap, Asteroid(x,y), _asteroidCount, xMax, yMax))
    return asteroidList


def CountAsteroids(_starMap: list) -> int:
    # count each in X lenght and y lenght of the map
    i = 0 # Amount of asteroids
    xMax = len(_starMap[0])
    yMax = len(_starMap)
    for y in range(xMax):
        for x in range(yMax):
            # if there is an asteroid here (4) test it for validity
            if _starMap[y][x] == 4:
                i += 1
    return i             
                

# Main Code -------------------------------------------------

# Example 1
# Best is 5,8 with 33 other asteroids detected:
try:  
    file = open('day10_input.txt', 'r') 
    #file = open('day10_example1.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

starMap = list()

# Loop each line in file
for line in file:
    # '.' = 0 = space
    # '#' = 4 = visible asteroid
    starConvDict = {'.': 0, '#': 4} # Dictionay used for converting strings to numbers
    mapLineRaw = list(line.strip())
    mapLine = [starConvDict[point] for point in mapLineRaw] # Map each point string to a value
    starMap.append(mapLine)
file.close()

# How many asteroids are there in the map.
asteroidCount = CountAsteroids(starMap)

# Loop through each astroid to test it's visibiltiy count
asteroidList = LoopEachAstroid(starMap, asteroidCount)
# Sort list
asteroidList.sort(key=lambda x: x.visibleNeighbours, reverse=True)
print("Asteroid with best view is:")
print("X: {} Y: {} with {} neighbours visible".format(asteroidList[0].x,asteroidList[0].y,asteroidList[0].visibleNeighbours))




