#! /usr/bin/python3
# # --- Day 2: 1202 Program Alarm ---
# Part One

import sys

# Should we debug or not.
debug = False

opCodeList = []

def Addfunct(pos1, pos2, pos3):
    if debug: print("Add function args are:  " + str(pos1) + " " + str(pos2) + " " + str(pos3))
    opCodeList[pos3] = opCodeList[pos1] + opCodeList[pos2]

def Multfunct(pos1, pos2, pos3):
    if debug: print("Mult function args are: " + str(pos1) + " " + str(pos2) + " " + str(pos3))
    opCodeList[pos3] = opCodeList[pos1] * opCodeList[pos2]

def Exitfunct():
    if debug: 
        print("OpCode List values are: ")
        print(*opCodeList, sep = ",")
    print("The value left at position 0 is: " + str(opCodeList[0]) + '\n')
    sys.exit(0)

# Open input opCode file run the computer based on the rules.
# Input file has opcode and values split by comma
try:  
    file = open('day02_input.txt', 'r') 
except IOError:
    print("Can't open file!!")
    sys.exit(0)

# Read first line and strip end '\n'
opCodeLine = file.readline().strip()
if debug: print("OpCode Line: " + opCodeLine)

# split the string in a list and map the values to int
opCodeList = list(map(int, opCodeLine.split(",")))
if debug: print("OpCode List lenght: " + str(len(opCodeList)))

# test example for debugging
#opCodeList = [1,1,1,4,99,5,6,0,99]

# instruction pointer in the opcode
i = 0

# Fix special state
# Replace position 1 with the value 12 and replace position 2 with the value 2.
opCodeList[1] = 12
opCodeList[2] = 2

# Go through the oplist and check the values
while i < len(opCodeList) - 3:
    if opCodeList[i] == 1:
        Addfunct(opCodeList[i+1],opCodeList[i+2],opCodeList[i+3])
        if debug: print("Opcode 1")
    elif opCodeList[i] == 2:
        Multfunct(opCodeList[i+1],opCodeList[i+2],opCodeList[i+3])
        if debug: print("Opcode 2")
    elif opCodeList[i] == 99:
        if debug: print("Opcode 99")
        Exitfunct()
    else:
        print("Error no opCode??!!")
        sys.exit(1)
    # Jump forward to next opcode
    i += 4
