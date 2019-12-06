# --- Day 5: Sunny with a Chance of Asteroids ---
# Part One

import sys

# Should we debug or not.
debug = False

# the opcode list initilized as a list... :)
opCodeList = list()

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


"""
The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input). 
The TEST diagnostic program will run on your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:
Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. 
For example, the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. 
For example, the instruction 4,50 would output the value at address 50.
Programs that use these instructions will come with documentation that explains what should be connected to the input and output. 
The program 3,0,4,0,99 outputs whatever it gets as input, then halts.

Second, you'll need to add support for parameter modes:
Each parameter of an instruction is handled based on its parameter mode. 
Right now, your ship computer already understands parameter mode 0, position mode, 
which causes the parameter to be interpreted as a position - if the parameter is 50, 
its value is the value stored at address 50 in memory. Until now, all parameters have been in position mode.

Now, your ship computer will also need to handle parameters in mode 1, immediate mode. 
In immediate mode, a parameter is interpreted as a value - if the parameter is 50, its value is simply 50.

Parameter modes are stored in the same value as the instruction's opcode. 
The opcode is a two-digit number based only on the ones and tens digit of the value, that is, 
the opcode is the rightmost two digits of the first value in an instruction. 
Parameter modes are single digits, one per parameter, read right-to-left from the 
opcode: the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, 
the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.

For example, consider the program 1002,4,3,4,33.

The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost two digits of the first value, 02, 
indicate opcode 2, multiplication. Then, going right to left, the parameter modes are 0 (hundreds digit), 
1 (thousands digit), and 0 (ten-thousands digit, not present and therefore zero):

ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,  omitted due to being a leading zero
This instruction multiplies its first two parameters. 
The first parameter, 4 in position mode, works like it did before - its value is the value stored at address 4 (33). 
The second parameter, 3 in immediate mode, simply has value 3. 
The result of this operation, 33 * 3 = 99, is written according to the third parameter, 4 in position mode, 
which also works like it did before - 99 is written to address 4.

Parameters that an instruction writes to will never be in immediate mode.

Finally, some notes:

It is important to remember that the instruction pointer should increase by the number of values in the instruction 
after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).
The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an 
input instruction - provide it 1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, 
like parameter modes, function correctly. For each test, it will run an output instruction indicating 
how far the result of the test was from the expected value, where 0 means the test was successful. 
Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the 
output instruction to see which one failed.

Finally, the program will output a diagnostic code and immediately halt. 
This final output isn't an error; an output followed immediately by a halt means the program finished. 
If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce?
"""