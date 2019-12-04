# --- Day 3: Crossed Wires ---
# Part One

import sys , string

class Point:
    def __init__(self,x_init,y_init,line_init):
        self.x = x_init
        self.y = y_init
        self.line = line_init
   

    # Return a Name of the object if asked...
    def __repr__(self):
        return "x: "+ str(self.x) +" y: "+ str(self.y) +" line: "+  str(self.line)

# Should we debug or not.
debug = False

# Create lists to store the lines and the position we are in.
lineLists = []
linePos = []

# List of crossings
lineCross = []

# create two positions for each list so we know where they are in X, Y and linenum
linePos.append(Point(0,0,0))
linePos.append(Point(0,0,1))

gridSize = 20000
# Init a 2D grid with gridSize/2 i each direction. so we have enough space... (Ugly)
#grid = [[Point(0,0,0) for i in range(10)] for j in range(gridSize)]
grid = [[0]*gridSize for i in range(gridSize)]

# set the middle of the grid. (don't want minus in my list array)
gridNull = int(gridSize / 2)

# Go in the correct direction.
def GoUp(steps, lineNum):
    if debug: print("Going Up: " + str(steps) + " Steps for line: " + str(lineNum))
    GoSteps(steps, 0, 1, lineNum)

def GoDown(steps, lineNum):
    if debug: print("Going Down: " + str(steps) + " Steps for line: " + str(lineNum))
    GoSteps(steps, 0, -1, lineNum)

def GoRight(steps, lineNum):
    if debug: print("Going Right: " + str(steps) + " Steps for line: " + str(lineNum))
    GoSteps(steps, 1, 0, lineNum)

def GoLeft(steps, lineNum):
    if debug: print("Going Left: " + str(steps) + " Steps for line: " + str(lineNum))
    GoSteps(steps, -1, 0, lineNum)
    
# Go steps in a direction
def GoSteps(steps, xDir, yDir, lineNum):
    if debug: print("Going " + str(steps) + " Steps for line: " + str(lineNum))
    localX = linePos[lineNum].x
    localY = linePos[lineNum].y
    for x in range(0, int(steps)):
        localX += xDir
        localY += yDir
        if grid[gridNull+localX][gridNull+localY] == 0:
            grid[gridNull+localX][gridNull+localY] = Point(localX,localY,lineNum)
        elif grid[gridNull+localX][gridNull+localY].line != lineNum:
            if debug: print("Crossing at X:" + str(localX) +" & Y:" + str(localY)  + " !!")
            lineCross.append(CalcDist(localX,localY))
        if debug: print(grid[gridNull+localX][gridNull+localY])
    linePos[lineNum].x = localX
    linePos[lineNum].y = localY
    if debug: print("local X = " + str(localX))
    if debug: print("local Y = " + str(localY))

def CalcDist(x,y):
    return abs((0-x) + (0-y))

# Open input opCode file run the computer based on the rules.
# Input file has opcode and values split by comma
try:  
    file = open('day03_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

# list of the raw string lines
lineRaw = []

# read the two lines... not dynamic if more than two lines...
for i in range(2):
    # Read lines from file and strip end '\n'
    lineRaw.append(file.readline().strip())
    if debug: print("Raw" + str(i) + ": " + lineRaw[i] + '\n')

#lineRaw[0] = 'R8,U5,L5,D3'
#lineRaw[1] = 'U7,R6,D4,L4'

# test example 1 for debugging intersect at distance 159
#lineRaw[0] = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
#lineRaw[1] = 'U62,R66,U55,R34,D71,R55,D58,R83'

# test example 2 for debugging intersect at distance 135
#lineRaw[0] = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
#lineRaw[1] = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

# split the raw string in a list
for i in range(2):
    lineLists.append(lineRaw[i].split(","))
    if debug:
        print("Line "+ str(i) +" List data: ")
        print(*lineLists[i], sep = ",")
    if debug: print("Line "+ str(i) +" List lenght: " + str(len(lineLists[i])))


for nr in range(2):
    for i in range(len(lineLists[nr])):
        # Split substring to only look at direction and value.
        if (lineLists[nr][i][:1] == 'U'): GoUp(lineLists[nr][i][1:],nr)
        elif (lineLists[nr][i][:1] == 'D'): GoDown(lineLists[nr][i][1:],nr)
        elif (lineLists[nr][i][:1] == 'R'): GoRight(lineLists[nr][i][1:],nr)
        elif (lineLists[nr][i][:1] == 'L'): GoLeft(lineLists[nr][i][1:],nr)

lineCross.sort()
print(lineCross)

"""  two wires are connected to a central port and extend outward on a grid. 
You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).
The wires twist and turn, but the two wires occasionally cross paths. 
To fix the circuit, you need to find the intersection point closest to the central port. 
Because the wires are on a grid, use the Manhattan distance for this measurement. 
While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.
"""