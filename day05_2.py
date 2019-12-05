# --- Day 5: Sunny with a Chance of Asteroids ---
# Part Two

import sys

# Should we debug or not.
debug = False

# the opcode list initilized as a list... :)
opCodeList = list()

def Addfunct(arg1, param1, arg2, param2, arg3):
    if debug: print("Add function args are:  " + str(arg1) + " " + str(arg2) + " " + str(arg3))
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]    
    opCodeList[arg3] = val1 + val2

def Multfunct(arg1, param1, arg2, param2, arg3):
    if debug: print("Mult function args are: " + str(arg1) + " " + str(arg2) + " " + str(arg3))
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]    
    opCodeList[arg3] = val1 * val2

def GetInput(arg1):
    if debug: print("Get input args are: " + str(arg1))
    value = input("Enter number input: ")
    opCodeList[arg1] = int(value)

def SendOutput(arg1,param1):
    if debug: print("send output args are: " + str(arg1))
    val1 = arg1 if param1 else opCodeList[arg1]
    print(val1)

def JumpIfTrue(arg1, param1, arg2, param2, i):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 != 0: return val2
    else:
        i += 3
        return i

def JumpIfFalse(arg1, param1, arg2, param2, i):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 == 0: return val2
    else:
        i += 3
        return i

def IfLessThan(arg1, param1, arg2, param2, arg3):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 < val2: opCodeList[arg3] = 1
    else: opCodeList[arg3] = 0

def IfEquals(arg1, param1, arg2, param2, arg3):
    val1 = arg1 if param1 else opCodeList[arg1]
    val2 = arg2 if param2 else opCodeList[arg2]
    if val1 == val2: opCodeList[arg3] = 1
    else: opCodeList[arg3] = 0

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

# Example code 1 output 0 if the input was zero or 1 if the input was non-zero:
#opCodeList = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

# Example code 2 Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#opCodeList = [3,9,8,9,10,9,4,9,99,-1,8]

# Example Code 3 Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#opCodeList = [3,3,1108,-1,8,3,4,3,99]

# Example Code 4
#opCodeList = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
""" The above example program uses an input instruction to ask for a single number. 
The program will then output 999 if the input value is below 8, 
output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8. """

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
        Addfunct(opCodeList[i+1],param1,opCodeList[i+2],param2,opCodeList[i+3])
        if debug: print("Opcode 1")
        i += 4
    elif oper == 2:
        Multfunct(opCodeList[i+1],param1,opCodeList[i+2],param2,opCodeList[i+3])
        if debug: print("Opcode 2")
        i += 4
    elif oper == 3:
        GetInput(opCodeList[i+1])
        if debug: print("Opcode 3: ")
        i += 2
    elif oper == 4:
        SendOutput(opCodeList[i+1], param1)
        if debug: print("Opcode 4: ")
        i += 2
    elif oper == 5:
        i = JumpIfTrue(opCodeList[i+1], param1, opCodeList[i+2], param2, i)
        if debug: print("Opcode 5: ")
    elif oper == 6:
        i = JumpIfFalse(opCodeList[i+1], param1, opCodeList[i+2], param2, i)
        if debug: print("Opcode 6: ")
    elif oper == 7:
        IfLessThan(opCodeList[i+1], param1, opCodeList[i+2], param2, opCodeList[i+3])
        if debug: print("Opcode 7: ")
        i += 4
    elif oper == 8:
        IfEquals(opCodeList[i+1], param1, opCodeList[i+2], param2, opCodeList[i+3])
        if debug: print("Opcode 7: ")
        i += 4
        
    elif oper == 99:
        if debug: print("Opcode 99")
        Exitfunct()
    else:
        print("Error no opCode??!!")
        sys.exit(0)
    # Jump forward to next opcode
    

print("Didn't find a solution!!!!!!")


"""
The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. 
Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. 
Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. 
Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. 
Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. 
However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?
"""