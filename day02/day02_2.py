#!/usr/bin/env python3
# --- Day 2: 1202 Program Alarm ---
# Part Two

import sys

# Should we debug or not.
debug = False

# the opcode list initilized as a list... :)
opCodeList = []

# Add function that returns true if there is an error.
def Addfunct(pos1, pos2, pos3, _len):
    if debug: print("Add function args are:  " + str(pos1) + " " + str(pos2) + " " + str(pos3))
    # check so the values isn't larger than lenght of List (error otherwise)
    if pos1 > _len or pos2 > _len or pos3 > _len:
        return True
    else:
        opCodeList[pos3] = opCodeList[pos1] + opCodeList[pos2]
        return False

# Multiply function that returns true if there is an error.
def Multfunct(pos1, pos2, pos3, _len):
    if debug: print("Mult function args are: " + str(pos1) + " " + str(pos2) + " " + str(pos3))
    # check so the values isn't larger than lenght of List (error otherwise)
    if pos1 > _len or pos2 > _len or pos3 > _len:
        return True
    else:
        opCodeList[pos3] = opCodeList[pos1] * opCodeList[pos2]
        return False

# Exit function that should run when program is finished
def Exitfunct(_noun, _verb):
    if debug: 
        print("OpCode List values are: ")
        print(*opCodeList, sep = ",")
    print("correct values are noun: " + str(_noun) + " and verb: " + str(_verb))
    print("correct answer is: " + str(100 * _noun + _verb))
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
cleanOpCodeList = list(map(int, opCodeLine.split(",")))

if debug: print("Clean OpCode List lenght: " + str(len(cleanOpCodeList)))

# test values for noun and verb 0-99 each.
for noun1 in range(0, 100):
    for verb1 in range(0, 100):
        #set clean memory
        # instruction pointer in the opcode
        i = 0
        contLoop = True
        opCodeList = cleanOpCodeList.copy()
        opCodeList[1] = noun1
        if debug: print("Noun: " + str(opCodeList[1]))
        opCodeList[2] = verb1
        if debug: print("verb: " + str(opCodeList[2]))
        opCodeListLen = len(opCodeList)
        if debug: print("opCodeListLen: " + str(opCodeListLen))
        # Go through the oplist and check the values
        while i < (opCodeListLen - 3) or contLoop:
            if opCodeList[i] == 1:
                if Addfunct(opCodeList[i+1],opCodeList[i+2],opCodeList[i+3],opCodeListLen):
                    contLoop = False
                else:
                    if debug: print("Opcode 1")
            elif opCodeList[i] == 2:
                if Multfunct(opCodeList[i+1],opCodeList[i+2],opCodeList[i+3],opCodeListLen):
                    contLoop = False
                else:
                    if debug: print("Opcode 2")
            elif opCodeList[i] == 99:
                if debug: print("Opcode 99")
                if debug: print("Return value is: " + str(opCodeList[0]))
                if opCodeList[0] == 19690720:
                    Exitfunct(noun1, verb1)
                contLoop = False # break while loop
            else:
                if debug: print("Error wrong opCode??!!")
                contLoop = False # break while loop
            # Jump forward to next opcode
            i += 4

print("Didn't find a solution!!!!!!")
