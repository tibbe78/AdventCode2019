# --- Day 9: Sensor Boost ---
# Part One & Two

import sys
from dataclasses import dataclass

# Classes------------------------------------------

@dataclass
class IntCode:
    def __init__(self, _instrPoint : int, _compMem: list):
        self.blob = str(_compMem[_instrPoint]) # Like "1102"
        self.opcode = int(self.blob[-2:]) # Like 02
        self.param = list() # parameters to the opcode
        self.value = list() # values based on parameter & mode
        self.pModesRaw = self.blob[:-2] # parameter modes
        self.pMode = [0,0,0] # set the parameter modes default
        self.instrPoint = _instrPoint
        self.basePointer = None
        self.compMem = _compMem # Pointer to the rest of the program
        # find & set parameter modes
        for i in range(len(self.pModesRaw)-1,-1,-1): # the range goes from 2 to 0 backwards -1 because it don't stop with 0 
            self.pMode[i] = (int(list(self.pModesRaw)[::-1][i])) # Wow this took time... maka a list of the string, reverse it [::-1] and the select num i.

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

    def GetInput(self):
        self.SetParameters(1,0)
        self.compMem[self.value[0]] = int(input("Enter number: "))
        self.instrPoint += 2   
    
    def SendOutput(self):
        self.SetParameters(1)
        print(self.value[0])
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

try:  
    file = open('day09_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

opCodeRaw = file.readline().strip()
opCodeList = list(map(int, opCodeRaw.split(","))).copy()

# Example takes no input and produces a copy of itself as output.
#opCodeList = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] 

# Example should output a 16-digit number.
#opCodeList = [1102,34915192,34915192,7,4,7,99,0] 

# Example should output the large number in the middle.
#opCodeList = [104,1125899906842624,99] 

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
    elif intCode.opcode == 3: intCode.GetInput()
    elif intCode.opcode == 4: intCode.SendOutput()
    elif intCode.opcode == 5: intCode.JumpIfTrue()
    elif intCode.opcode == 6: intCode.JumpIfFalse()
    elif intCode.opcode == 7: intCode.IfLessThan()
    elif intCode.opcode == 8: intCode.IfEquals()
    elif intCode.opcode == 9: intCode.ChangeBase()
    elif intCode.opcode == 99: 
        print("OpCode 99 Exit")
        sys.exit(0)
    else:
        print("Error no opCode??!!")
        sys.exit(0)
    
    instrPoint = intCode.GetInstrPointer() # Get back the updated instruction pointer
    relativeBase = intCode.GetBasePointer() # and alsi the BasePointer or as called Relative Pointer.
    

print("Didn't find a solution!!!!!!")
