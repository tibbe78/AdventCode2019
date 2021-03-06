#! /usr/bin/python3
# --- Day 5: Sunny with a Chance of Asteroids ---
# Part One

import sys

# Should we debug or not.
debug = False

# the opcode list initilized as a list... :)
opCodeList = []

def Addfunct(arg1, param1, arg2, param2, arg3, param3):
    if debug: print("Add function args are:  " + str(arg1) + " " + str(arg2) + " " + str(arg3))
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]    
    opCodeList[arg3] = val1 + val2

def Multfunct(arg1, param1, arg2, param2, arg3, param3):
    if debug: print("Mult function args are: " + str(arg1) + " " + str(arg2) + " " + str(arg3))
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]    
    opCodeList[arg3] = val1 * val2

def GetInput(pos1):
    if debug: print("Get input args are: " + str(pos1))
    value = input("Enter number input: ")
    opCodeList[pos1] = int(value)

def SendOutput(pos1):
    if debug: print("send output args are: " + str(pos1))
    print(opCodeList[pos1])

def Exitfunct():
    print("Exit the program!!!")
    sys.exit(0)

# Open input opCode file run the computer based on the rules.
# Input file has opcode and values split by comma
try:  
    file = open('day05_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

# Read first line and strip end '\n'
opCodeRaw = file.readline().strip()
if debug: print("OpCode Raw: " + opCodeRaw)

# split the string in a list and map the values to int
opCodeList = list(map(int, opCodeRaw.split(","))).copy()

if debug: print("OpCode List lenght: " + str(len(opCodeList)))

# Example code 1
#opCodeList = [3,0,4,0,99]

# instruction pointer in the opcode
i = 0

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
        Addfunct(opCodeList[i+1],param1,opCodeList[i+2],param2,opCodeList[i+3],param3)
        if debug: print("Opcode 1")
        i += 4
    elif oper == 2:
        Multfunct(opCodeList[i+1],param1,opCodeList[i+2],param2,opCodeList[i+3],param3)
        if debug: print("Opcode 2")
        i += 4
    elif oper == 3:
        GetInput(opCodeList[i+1])
        if debug: print("Opcode 3: ")
        i += 2
    elif oper == 4:
        SendOutput(opCodeList[i+1])
        if debug: print("Opcode 4: ")
        i += 2
    elif oper == 99:
        if debug: print("Opcode 99")
        Exitfunct()
    else:
        print("Error no opCode??!!")
        sys.exit(0)
    # Jump forward to next opcode
    

print("Didn't find a solution!!!!!!")
