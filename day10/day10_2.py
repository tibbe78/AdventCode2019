# --- Day 10: Monitoring Station ---
# Part One

import sys, math
from dataclasses import dataclass

# Classes------------------------------------------

@dataclass
class Asteroid:
    def __init__(self, x, y, origin = False):
        """
        Init the Class Astroid with it's position
        """
        self.x = x
        self.y = y
        self.angle = 99999.9
        self.distance = None
        self.origin = origin
    
    def SetAngle(self, angle: float):
        self.angle = angle
    
    def SetDistance(self, distance: float):
        self.distance = distance
    
    def __repr__(self):
        return "Asteroid X:{} Y:{}".format(self.x, self.y)
        

# Functions----------------------------------------


def calculateAsteroid(asteroidList: list):
    asteroid1 = None
    # find origin
    for asteroid1 in asteroidList:
        if asteroid1.origin:
            break
    
    # calc ang & distance for each asteroid
    for asteroid2 in asteroidList:
        if asteroid2.origin: continue
        
        # Calc diff between origin and ast2
        xDiff = asteroid2.x - asteroid1.x
        yDiff = asteroid2.y - asteroid1.y

        # Get the angle in degrees and move it 90 degrees so up is 0
        degrees = math.degrees(math.atan2(yDiff,xDiff) + math.radians(90))

        #fix if degrees is <0
        if degrees < 0:
            degrees += 360.0
        
        # Add angle and dist but round off a bit.            
        asteroid2.SetAngle(round(degrees,3))
        asteroid2.SetDistance(round(math.sqrt((xDiff)**2 + (yDiff)**2),3))

def IndexAsteroids(_starMap: list, x0, y0) -> list:
    ''' get the map and convert it to a list of class Asteroids '''
    asteroidList = list()
    xMax = len(_starMap[0])
    yMax = len(_starMap)
    for y in range(yMax):
        for x in range(xMax):
            origin = False
            # if there is an asteroid here (4) test it for validity
            if _starMap[y][x] == 4:
                if x == x0 and y == y0: origin = True # Mark the origin asteroid.
                asteroidList.append(Asteroid(x,y,origin))
    return asteroidList
                

# Main Code -------------------------------------------------


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

#Answer part one
#X: 26 Y: 36 with 347 neighbours visible
# Count the 200:th scan from this position.
originX = 26
originY = 36

# Example 1
'''
In the large example (the one with the best monitoring station location at 11,13):
The 1st asteroid to be vaporized is at 11,12.
The 2nd asteroid to be vaporized is at 12,1.
The 3rd asteroid to be vaporized is at 12,2.
The 10th asteroid to be vaporized is at 12,8.
The 20th asteroid to be vaporized is at 16,0.
The 50th asteroid to be vaporized is at 16,9.
The 100th asteroid to be vaporized is at 10,16.
The 199th asteroid to be vaporized is at 9,6.
The 200th asteroid to be vaporized is at 8,2.
The 201st asteroid to be vaporized is at 10,9.
The 299th and final asteroid to be vaporized is at 11,1.
'''
#originX = 11
#originY = 13

# index the asteroids in the map
asteroidList = IndexAsteroids(starMap, originX, originY)

# Calculate angle & distance for each asteroid from origin
calculateAsteroid(asteroidList)

# Sort list with first angle and then distance from origin.
asteroidList.sort(key=lambda x: (x.angle, x.distance))


prevAngle=99999.0
i = 0

# Remove origin
asteroidList.pop()

# Loop through astroid to test it's visibiltiy count
destructList = list()

# Loop the asteroid list and find each angle and remove it.
j = 0
totAst = len(asteroidList)
while i < totAst: # check that we find each asteroid
    while j < len(asteroidList): # check that we get the current 360 degree loop
        if asteroidList[j].angle != prevAngle:
            destructList.append(asteroidList[j]) # add the asteroid to the destruct list order
            prevAngle = asteroidList[j].angle
            asteroidList.pop(j) # Remove it from the list so we don't use it next 360 degree loop
            i += 1
        else: j += 1 # only need to change when we find a asteroid with same angle as othervise the pop removes the current j
    # now we have rotated 360 degrees no need to reset.
    prevAngle = 99999.0
    j = 0
        

print("The 200:th asteroid to be blown up is:")
print("X: {} Y: {}".format(destructList[199].x,destructList[199].y))




