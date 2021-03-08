#!/usr/bin/env python3

# --- Day 7: Amplification Circuit ---
# Part Two

import sys
""" from dataclasses import dataclass """

# Should we debug or not.
debug = False

# Wrapper so python send the Computer Memory as "pointer" instead of copy
""" @dataclass
class MemWrapper(object):
    def __init__(self, value):
        self.value = value """

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

def GetInput(arg1 , inputValues: list, firstRun, opCodeList: list):
    if debug: print("Get input args are: " + str(arg1))
    if inputValues[2]: 
        if firstRun: value = inputValues[0]
        else: value = inputValues[1]
    else: value = inputValues[1]

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

    # Set the return Value for this function
    returnValue = None
    # Set the instruction pointer
    i = inputValues[3]
    firstRun = True

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
            GetInput(opCodeList[i+1], inputValues, firstRun, opCodeList)
            if debug: print("Opcode 3: Get Input")
            i += 2
            firstRun = False
        elif oper == 4:
            returnValue = SendOutput(opCodeList[i+1], param1, opCodeList)
            if debug: print("Opcode 4: Return Value")
            i += 2
            #print("return op4: " + str(returnValue))
            return [returnValue, False, i]
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
            #print("return exit: " + str(returnValue))
            if debug: print("Opcode 99 Exit")
            return [returnValue, True, i]
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
if debug: print("OpCode Raw: " + opCodeRaw)

# Close the file.
file.close()

# the opcode list initilized as a list... :)
opCodeListOrg = list()

# store the Phase Sequence for the amplifiers
phaseSequence = list()

# split the string in a list and map the values to int
opCodeListOrg = list(map(int, opCodeRaw.split(","))).copy()

if debug: print("OpCode List lenght: " + str(len(opCodeListOrg)))

# First Phase then Input Signal
# First Input Signal is always 0

# Example code 1 Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):
#opCodeListOrg = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#phaseSequence = [9,8,7,6,5]

# Example code 2 Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
#opCodeListOrg = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
#phaseSequence = [9,7,8,5,6]

# Wrap each value in list to mutable object to get the "pointer feature"
""" computerMem = []
for value in opCodeList:
    computerMem.append(MemWrapper(value)) """

phaseMin = 5
phaseMax = 9

amplifiersNum = 5
listOutputValues = list()

# run the computer for each phase value
# Phase only used ONCE!!
for a in range(phaseMin,phaseMax+1):
    for b in range(phaseMin,phaseMax+1):
        if b == a: continue
        for c in range(phaseMin,phaseMax+1):
            if c == a or c == b: continue
            for d in range(phaseMin,phaseMax+1):
                if d == a or d == b or d == c: continue
                for e in range(phaseMin,phaseMax+1):
                    if e == a or e == b or e == c or e == d: continue
                    phaseSequence = [a,b,c,d,e]

                    # create the state of the amps so we know if it's the first start or not.            
                    runState = list()
                    for amp in range(amplifiersNum):
                        runState.append(True)

                    # create the response state of the amps so we know if they are finished or not?.            
                    ResponseState = list()
                    for amp in range(amplifiersNum):
                        ResponseState.append(False)

                    # Init the running memory for each amp as it should be kept between runs
                    runMemory = list()
                    for amp in range(amplifiersNum):
                        runMemory.append(opCodeListOrg.copy())
                    
                    # Init the IntPointer for each amp as it should be kept between runs
                    intPoint = list()
                    for amp in range(amplifiersNum):
                        intPoint.append(0)

                    # Init the first inputVale
                    output = 0

                    # The response from the program should be a output but also if it's finished.
                    response = list()

                    # Run as long as the last amp isn't finished?
                    while (not ResponseState[0]):
                        # Run the program for each amp with a reference to computer memory
                        for amp in range(amplifiersNum):
                            # set the input values for the computer with phase, previus output and first run state, plus the int pointer
                            inputValues = [phaseSequence[amp], output, runState[amp], intPoint[amp]]
                            # Run program and return the response    
                            response = RunComputer(inputValues, runMemory[amp])
                            # Save int Pointer
                            intPoint[amp] = response[2]
                            if response[1] == True:
                                #print("program finished")
                                ResponseState[amp] = True
                                break
                            else:
                                # Set the output value
                                output = response[0]
                            # After the first run set the state to False
                            runState[amp] = False
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


