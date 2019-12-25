# --- Day 13: Care Package ---
# Part One

import sys
from day13.modules.arcade import Arcade
from day13.modules.intcode import IntCode
from day13.modules.drawimage import DrawImage
from day13.modules.utils import CountBlockTiles

arcade = Arcade()

try:
    file = open('day13/day13_input.txt', 'r')
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
    elif intCode.opcode == 3: intCode.GetInput(arcade)
    elif intCode.opcode == 4: intCode.SendOutput(arcade)
    elif intCode.opcode == 5: intCode.JumpIfTrue()
    elif intCode.opcode == 6: intCode.JumpIfFalse()
    elif intCode.opcode == 7: intCode.IfLessThan()
    elif intCode.opcode == 8: intCode.IfEquals()
    elif intCode.opcode == 9: intCode.ChangeBase()
    elif intCode.opcode == 99:
        print("OpCode 99 Exit")
        CountBlockTiles(arcade.screen)
        DrawImage(arcade)
        sys.exit(0)
    else:
        print("Error no opCode??!!")
        sys.exit(0)
    instrPoint = intCode.GetInstrPointer() # Get back the updated instruction pointer
    relativeBase = intCode.GetBasePointer() # and alsi the BasePointer or as called Relative Pointer.

print("Didn't find a solution!!!!!!")
