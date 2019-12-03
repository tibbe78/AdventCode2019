# --- Day 2: 1202 Program Alarm ---
# Part Two

import sys

# Should we debug or not.
debug = False

opCodeList = list

def Addfunct(pos1, pos2, pos3, _len):
    if debug: print("Add function args are:  " + str(pos1) + " " + str(pos2) + " " + str(pos3))
    if pos1 > _len or pos2 > _len or pos3 > _len:
        return True
    else:
        opCodeList[pos3] = opCodeList[pos1] + opCodeList[pos2]
        return False

def Multfunct(pos1, pos2, pos3, _len):
    if debug: print("Mult function args are: " + str(pos1) + " " + str(pos2) + " " + str(pos3))
    if pos1 > _len or pos2 > _len or pos3 > _len:
        return True
    else:
        opCodeList[pos3] = opCodeList[pos1] * opCodeList[pos2]
        return False

def Exitfunct(_noun, _verb):
    if debug: 
        print("OpCode List values are: ")
        print(*opCodeList, sep = ",")
    print("correct values are noun: " + str(_noun) + " and verb: " + str(_verb))
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

# Opcode 1 adds together numbers read from two positions and stores the result in a third position.
# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
# Opcode 99 means that the program is finished and should immediately halt.

# You need to determine what pair of inputs produces the output 19690720? 


""" The inputs should still be provided to the program by replacing the values at addresses 1 and 2, 
just like before. In this program, the value placed in address 1 is called the noun, 
and the value placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0 

Find the input noun and verb that cause the program to produce the output 19690720.
What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
"""