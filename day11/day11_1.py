#!/usr/bin/env python3
# --- Day 11: Space Police ---
# Part One

import sys
from dataclasses import dataclass


# Classes------------------------------------------
@dataclass
class Plate:
    def __init__(self,x,y, color=0):
        self.x = x
        self.y = y
        self.timesTraversed = 1
        self.color = color
        self.name = "Plate_X:{}_Y:{}".format(self.x, self.y)

    def __repr__(self):
        return self.name

@dataclass
class Hull:
    def __init__(self):
        # directory of Grid Plates
        self.grid = {}

    def AddPlate(self, plate: Plate):
        self.grid[plate.name] = plate

    def CheckIfExists(self, plate: Plate):
        if not plate.name in self.grid.keys():
            self.AddPlate(plate)

    def getColor(self, plate) -> int:
        self.CheckIfExists(plate)
        return self.grid[plate.name].color

    def SetColor(self, plate):
        self.CheckIfExists(plate)
        self.grid[plate.name].color = plate.color
        self.grid[plate.name].timesTraversed += 1


@dataclass
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        # 0=up, 1=right, 2=down, 3=left
        self.direction = 0
        self.outputstate = 0
        # The hull of the ship.
        self.hull = Hull()
        
    def Move(self):
        # Take on step in direction
        if self.direction == 0: self.y += 1
        elif self.direction == 1: self.x += 1
        elif self.direction == 2: self.y -= 1
        elif self.direction == 3: self.x -= 1
    
    def DetectColor(self) -> int:
        # Get the color of tile 0=black 1=white
        return self.hull.getColor(Plate(self.x, self.y))
    
    def Paint(self, color:int):
        # paint color of tile 0=black 1=white
        self.hull.SetColor(Plate(self.x, self.y, color))
    
    def Turn(self, heading:int):
        if heading == 0:
            self.direction -=1
            if self.direction == -1: self.direction = 3
        elif heading == 1:
            self.direction +=1
            if self.direction == 4: self.direction = 0
        else: print("Errror Turning")
        self.Move()  
    
    def HandleOutput(self, output):
        if self.outputstate == 0:
            self.outputstate = 1
            self.Paint(output)
        else:
            self.outputstate = 0
            self.Turn(output) 

    
@dataclass
class IntCode:
    def __init__(self, _instrPoint : int, _compMem: list):
        """
        Init the Class IntCode with the instruction pointer and a pointer to the ComputerMem (program)
        """
        self.blob = str(_compMem[_instrPoint]) # Like '1102'
        self.opcode = int(self.blob[-2:]) # start at -2 in string. Like '02' from blob
        self.param = list() # parameters to the opcode as a list.
        self.value = list() # values based on parameter & mode as a list
        self.pModesRaw = self.blob[:-2] # parameter modes, end at -2 in string. like '11' from above '1102' blob
        self.pModesRevList = list(self.pModesRaw)[::-1] # Reveresed list of the parameters
        self.pMode = [0,0,0] # set the parameter modes default
        self.instrPoint = _instrPoint
        self.basePointer = None
        self.compMem = _compMem # Pointer to the rest of the computerMem or program.
        # find & set parameter modes like [0,1,1] from above raw pmodes.
        for i in range(len(self.pModesRevList)): # for each parameter we have a setting for. Else 0
            self.pMode[i] = (int(self.pModesRevList[i])) # set the pmode to the pmode in the list

    def GetInstrPointer(self) -> int:
        return self.instrPoint

    def SetBasePointer(self, baseP : int):
        self.basePointer = baseP
    
    def GetBasePointer(self) -> int:
        return self.basePointer
    
    def SetParameters(self, num, writeNum=9): 
        """
        Set the parameters acompaning the Operation Code. Can be up to three
        parameters. num is equal to the amount of parameters and writeNum specifies if one
        of them is the write parameter and should be handled specially.
        """
        for i in range(num): # Create one parameter at the time.
            paramLocation = self.instrPoint+(i+1) # the location of the parameter in the Computer Mem
            self.param.append(self.compMem[paramLocation]) # Create the parameter to the opcode.
            
            # if the parameter refers to a memory outside of range, add more memory
            if (self.pMode[i] == 0 or self.pMode[i] == 2): # not applicable for direct mode.
                totalMem = (self.basePointer + self.param[i]) if self.pMode[i] == 2 else self.param[i]
                if totalMem >= len(self.compMem):
                    for j in range(totalMem-len(self.compMem)+1): # Add the amount of memory missing
                        self.compMem.append(0)

            # If the mode to parameter is 0 = Position mode.
            if (self.pMode[i] == 0): 
                if i == writeNum: self.value.append(self.param[i]) # if this is the write parameter send only back location
                else: self.value.append(self.compMem[self.param[i]]) # Else send back value of location

            # If the mode to parameter is 1 = Direct mode.
            elif (self.pMode[i] == 1): self.value.append(self.param[i])

            # If the mode to parameter is 2 = Relative mode
            elif (self.pMode[i] == 2): 
                if i == writeNum: self.value.append(self.basePointer + self.param[i])
                else: self.value.append(self.compMem[self.basePointer + self.param[i]])

            else: print("Error!!")

    def Add(self): # Add function that Add two values together
        self.SetParameters(3,2)
        self.compMem[self.value[2]] = self.value[0] + self.value[1]
        self.instrPoint += 4   

    def Multiply(self): # Add function that Multiply two values together
        self.SetParameters(3,2)
        self.compMem[self.value[2]] = self.value[0] * self.value[1]
        self.instrPoint += 4   

    def GetInput(self, robot):
        self.SetParameters(1,0)
        self.compMem[self.value[0]] = robot.DetectColor()
        self.instrPoint += 2   
    
    def SendOutput(self, robot):
        self.SetParameters(1)
        robot.HandleOutput(self.value[0])
        self.instrPoint += 2

    def JumpIfTrue(self):
        self.SetParameters(2)
        if self.value[0] != 0: self.instrPoint = self.value[1]
        else: self.instrPoint += 3   
    
    def JumpIfFalse(self):
        self.SetParameters(2)
        if self.value[0] == 0: self.instrPoint = self.value[1]
        else: self.instrPoint += 3
    
    def IfLessThan(self):
        self.SetParameters(3,2)
        if self.value[0] < self.value[1]: self.compMem[self.value[2]] = 1
        else: self.compMem[self.value[2]] = 0
        self.instrPoint += 4
    
    def IfEquals(self):
        self.SetParameters(3,2)
        if self.value[0] == self.value[1]: self.compMem[self.value[2]] = 1
        else: self.compMem[self.value[2]] = 0
        self.instrPoint += 4
    
    def ChangeBase(self):
        self.SetParameters(1)
        self.basePointer += self.value[0]
        self.instrPoint += 2

    def __repr__(self):
        return "OpCode: {}".format(self.opcode)

# Functions----------------------------------------



# Main Code -------------------------------------------------

robot = Robot()

try:  
    file = open('day11_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

opCodeRaw = file.readline().strip()
opCodeList = list(map(int, opCodeRaw.split(","))).copy()

# instruction pointer in the opcode so we know where in the code we are.
instrPoint = 0

# Relative Base Pointer, will be changed by the program.
relativeBase = 0

# Go through the oplist and check the values
while instrPoint < len(opCodeList):

    intCode = IntCode(instrPoint,opCodeList) # init the IntCode class
    intCode.SetBasePointer(relativeBase) # set the basePointer
    if intCode.opcode == 1: intCode.Add()
    elif intCode.opcode == 2: intCode.Multiply()
    elif intCode.opcode == 3: intCode.GetInput(robot)
    elif intCode.opcode == 4: intCode.SendOutput(robot)
    elif intCode.opcode == 5: intCode.JumpIfTrue()
    elif intCode.opcode == 6: intCode.JumpIfFalse()
    elif intCode.opcode == 7: intCode.IfLessThan()
    elif intCode.opcode == 8: intCode.IfEquals()
    elif intCode.opcode == 9: intCode.ChangeBase()
    elif intCode.opcode == 99: 
        print("OpCode 99 Exit")
        print("Grid Plates walked at: {}".format(len(robot.hull.grid)))
        sys.exit(0)
    else:
        print("Error no opCode??!!")
        sys.exit(0)
    
    instrPoint = intCode.GetInstrPointer() # Get back the updated instruction pointer
    relativeBase = intCode.GetBasePointer() # and alsi the BasePointer or as called Relative Pointer.
    

print("Didn't find a solution!!!!!!")
