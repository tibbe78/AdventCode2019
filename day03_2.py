# --- Day 3: Crossed Wires ---
# Part Two

import sys , string
from dataclasses import dataclass

@dataclass
class Point(object):
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init
    # Return a Name of the object if asked...
    #def __repr__(self):
    #    return self

# Should we debug or not.
debug = False



# list of steps to count two lists in this list...
stepsTaken=[]
stepsTaken.append([])
stepsTaken.append([])

# List of crossings
lineCross = []

# create two positions for each list so we know where they are in X, Y
linePos = []
linePos.append(Point(0,0))
linePos.append(Point(0,0))

# Set lists to find unique steps.
setList = []
setList.append(set())
setList.append(set())


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
    if debug: print("Going " + steps + " Steps for line: " + str(lineNum))
    # Fetch the previous position
    localX = linePos[lineNum].x
    localY = linePos[lineNum].y
    for x in range(int(steps)):
        # Move in correct direction
        localX += xDir
        localY += yDir
        # Adding hash to set to get unique steps
        setList[lineNum].add(str(localX) + '_' + str(localY))
        # add steps to list of steps so we can count them later.
        stepsTaken[lineNum].append(Point(localX,localY))
    linePos[lineNum].x = localX
    linePos[lineNum].y = localY
    if debug: print("local X = " + str(localX))
    if debug: print("local Y = " + str(localY))

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

# small test for debugging 30 steps
#lineRaw[0] = 'R8,U5,L5,D3'
#lineRaw[1] = 'U7,R6,D4,L4'

# test example 1 for debugging 610 steps
#lineRaw[0] = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
#lineRaw[1] = 'U62,R66,U55,R34,D71,R55,D58,R83'

# test example 2 for debugging 410 steps
lineRaw[0] = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
lineRaw[1] = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

# Create lists to store the lines and the position we are in.
lineLists = []

# split the raw string in a list
for nr in range(2):
    lineLists.append(lineRaw[nr].split(","))
    if debug:
        print("Line "+ str(nr) +" List data: ")
        print(*lineLists[nr], sep = ",")
    if debug: print("Line "+ str(nr) +" List lenght: " + str(len(lineLists[nr])))
 
for nr in range(2):
    for i in range(len(lineLists[nr])):
        if debug: print("Dir: " + str(lineLists[nr][i][:1]) + " Len: " + str(lineLists[nr][i][1:]))
        # Split substring to only look at direction and value.
        if (lineLists[nr][i][:1] == 'U'): GoUp(lineLists[nr][i][1:],nr)
        elif (lineLists[nr][i][:1] == 'D'): GoDown(lineLists[nr][i][1:],nr)
        elif (lineLists[nr][i][:1] == 'R'): GoRight(lineLists[nr][i][1:],nr)
        elif (lineLists[nr][i][:1] == 'L'): GoLeft(lineLists[nr][i][1:],nr)
        else: print("ERRROR!!!")

tempSteps = []
tempSteps.append(set())
tempSteps.append(set())

temp2Steps = []
temp2Steps.append(0)
temp2Steps.append(0)

optimizedSteps = []
optimized2Steps = []

# find steps in both lists = crossings
for hashName in (setList[0] & setList[1]):
    x = int(hashName.split("_")[0])
    y = int(hashName.split("_")[1])
    if debug: print(str(abs(x)+abs(y)))
    if debug:
        print("x=" + str(x))
        print("y=" + str(y))
    # Count the steps taken until we come to a crossing
    for i in range(2):
        j = 0
        tempSteps[i].clear()
        temp2Steps[i] = 1
        tempSteps[i].add(str(stepsTaken[i][j].x) + '_' + str(stepsTaken[i][j].y))
        while (stepsTaken[i][j].x != x) or (stepsTaken[i][j].y != y):
            j+=1
            temp2Steps[i] += 1
            tempSteps[i].add(str(stepsTaken[i][j].x) + '_' + str(stepsTaken[i][j].y))
            if debug: print("x=" + str(stepsTaken[i][j].x) + ' y=' + str(stepsTaken[i][j].y))
    optimized2Steps.append(temp2Steps[0] + temp2Steps[1])
    optimizedSteps.append(len(tempSteps[0]) + len(tempSteps[1]))

# One short!!???
optimizedSteps.sort()             
print(optimizedSteps)
           
print('\n\n')

# this works don't know why???
optimized2Steps.sort()             
print(optimized2Steps)


"""  It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.
To do this, calculate the number of steps each wire takes to reach each intersection; 
choose the intersection where the sum of both wires' steps is lowest. 
If a wire visits a position on the grid multiple times, use the steps value from the first time 
it visits that position when calculating the total value of a specific intersection.
The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including 
the intersection being considered. Again consider the example from above:
"""