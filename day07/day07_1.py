#!/usr/bin/env python3

# --- Day 7: Amplification Circuit ---
# Part One

import sys

# Should we debug or not.
debug = False

def Addfunct(arg1, param1, arg2, param2, arg3, opCodeList: list):
    if debug: print("Add function args are:  " + str(arg1) + " " + str(arg2) + " " + str(arg3))
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]    
    opCodeList[arg3] = val1 + val2

def Multfunct(arg1, param1, arg2, param2, arg3, opCodeList: list):
    if debug: print("Mult function args are: " + str(arg1) + " " + str(arg2) + " " + str(arg3))
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]    
    opCodeList[arg3] = val1 * val2

def GetInput(arg1 , inputValues: list, inputNum: int, opCodeList: list):
    if debug: print("Get input args are: " + str(arg1))
    value = inputValues[inputNum]
    opCodeList[arg1] = int(value)

def SendOutput(arg1, param1, opCodeList: list) -> int:
    if debug: print("send output args are: " + str(arg1))
    val1 = arg1 if param1 else opCodeList[arg1]
    return val1

def JumpIfTrue(arg1, param1, arg2, param2, i, opCodeList: list):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 != 0: return val2
    else:
        i += 3
        return i

def JumpIfFalse(arg1, param1, arg2, param2, i, opCodeList: list):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 == 0: return val2
    else:
        i += 3
        return i

def IfLessThan(arg1, param1, arg2, param2, arg3, opCodeList: list):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 < val2: opCodeList[arg3] = 1
    else: opCodeList[arg3] = 0

def IfEquals(arg1, param1, arg2, param2, arg3, opCodeList: list):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 == val2: opCodeList[arg3] = 1
    else: opCodeList[arg3] = 0



# Run the computer, takes a list of two values for ampPhase and InputValue
def RunComputer(inputValues: list, opCodeList: list) -> int:
    # instruction pointer in the opcode
    i = 0

    # Which input should be given
    inputNum = 0

    # Set the return Value for this function
    returnValue = None

    # Go through the oplist and check the values
    while i < len(opCodeList):
        # Save to string so we can substring it.
        opCode = str(opCodeList[i])
        oper = int(opCode[-2:])
        params = opCode[:-2]

        param1 = 0
        param2 = 0
        param3 = 0
        # find & set parameters
        if len(params) == 3:
            param1 = int(params[2:])
            param2 = int(params[1:-1])
            param3 = int(params[:-2])
        elif len(params) == 2:
            param1 = int(params[1:])
            param2 = int(params[:-1])
        elif len(params) == 1:
            param1 = int(params)

        if debug: print(int(opCode[-2:]))
        # run the operators with the params
        if oper == 1:
            Addfunct(opCodeList[i+1],param1,opCodeList[i+2],param2,opCodeList[i+3], opCodeList)
            if debug: print("Opcode 1: Addition")
            i += 4
        elif oper == 2:
            Multfunct(opCodeList[i+1],param1,opCodeList[i+2],param2,opCodeList[i+3], opCodeList)
            if debug: print("Opcode 2: Multiply")
            i += 4
        elif oper == 3:
            GetInput(opCodeList[i+1], inputValues, inputNum, opCodeList)
            if debug: print("Opcode 3: Get Input")
            inputNum += 1
            i += 2
        elif oper == 4:
            returnValue = SendOutput(opCodeList[i+1], param1, opCodeList)
            if debug: print("Opcode 4: Return Value")
            i += 2
        elif oper == 5:
            i = JumpIfTrue(opCodeList[i+1], param1, opCodeList[i+2], param2, i, opCodeList)
            if debug: print("Opcode 5: Jump if true")
        elif oper == 6:
            i = JumpIfFalse(opCodeList[i+1], param1, opCodeList[i+2], param2, i, opCodeList)
            if debug: print("Opcode 6: Jump if False")
        elif oper == 7:
            IfLessThan(opCodeList[i+1], param1, opCodeList[i+2], param2, opCodeList[i+3], opCodeList)
            if debug: print("Opcode 7: If Less Than")
            i += 4
        elif oper == 8:
            IfEquals(opCodeList[i+1], param1, opCodeList[i+2], param2, opCodeList[i+3], opCodeList)
            if debug: print("Opcode 8: If Equals")
            i += 4
        elif oper == 99:
            if debug: print("Opcode 99 Exit")
            return returnValue
            sys.exit(0)
        else:
            print("Error no opCode??!!")
            sys.exit(0)
        # Jump forward to next opcode
    print("ERROR End of CODE!!")
    sys.exit(0)

# Python sort of sublist.
def SortSub(sub_list): 
    sub_list.sort(reverse = True, key = lambda x: x[0]) 
    return sub_list

# Open input opCode file run the computer based on the rules.
# Input file has opcode and values split by comma
try:  
    file = open('day07_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

# Read first line and strip end '\n'
opCodeRaw = file.readline().strip()
if debug: print("OpCode Raw: {}".format(opCodeRaw))

# Close the file.
file.close()

# the opcode list initilized as a list... :)
opCodeList = list()

# store the Phase Sequence for the amplifiers
phaseSequence = list()

# split the string in a list and map the values to int
opCodeList = list(map(int, opCodeRaw.split(","))).copy()

if debug: print("OpCode List lenght: " + str(len(opCodeList)))

# First Phase then Input Signal
# First Input Signal is always 0

# Example code 1 Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
#opCodeList = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#phaseSequence = [4,3,2,1,0]

# Example code 2 Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
#opCodeList = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#phaseSequence = [0,1,2,3,4]

# Example Code 3 Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
#opCodeList = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#phaseSequence = [1,0,4,3,2]

amplifiersNum = 5
listOutputValues = list()

# run the computer for each phase value
# Phase only used ONCE!!
for a in range(5):
    for b in range(5):
        if b == a: continue
        for c in range(5):
            if c == a or c == b: continue
            for d in range(5):
                if d == a or d == b or d == c: continue
                for e in range(5):
                    if e == a or e == b or e == c or e == d: continue
                    phaseSequence = [a,b,c,d,e]
                    # Init the first inputVale
                    output = 0
                    # Run the program for each amp with a copy of the list.
                    for amp in range(amplifiersNum):
                        inputValues = [phaseSequence[amp], output]
                        output = RunComputer(inputValues, opCodeList.copy())
                    listOutputValues.append([output, phaseSequence])

# Find largest OutPut and corresponding Phasesequence
maxOutput = 0
phaseSequence = [0,0,0,0,0]
for pair in listOutputValues:
    if pair[0] > maxOutput: 
        maxOutput = pair[0]
        phaseSequence = pair[1]

print(phaseSequence)
print(maxOutput)

#SortSub(listOutputValues)
#print(listOutputValues[0])


