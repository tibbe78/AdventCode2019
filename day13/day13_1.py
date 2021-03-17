#!/usr/bin/env python3
# --- Day 13: Care Package ---
# Part One

import sys
from day13.packages.logic.flipper.flipper_logic import FlipperLogic
from day13.packages.logic.computer.intcode import IntCode
from day13.packages.render.draw_image import drawImage

def main():
    flipper = FlipperLogic()
    try:
        file = open("./day13_input.txt", "r")
    except IOError as err:
        print("Can't open file!!: {0}".format(err))
        sys.exit(0)
    opCodeRaw = file.readline().strip()
    opCodeList = list(map(int, opCodeRaw.split(","))).copy()
    # instruction pointer in the opcode so we know where in the code we are.
    instrPoint = 0
    # Relative Base Pointer, will be changed by the program.
    relativeBase = 0
    intCode = IntCode(instrPoint, opCodeList)  
    # Go through the oplist and check the values (Run the computer)
    while instrPoint < len(opCodeList):
        intCode.reset(instrPoint, relativeBase)
        if intCode.opcode == 1:
            intCode.add()
        elif intCode.opcode == 2:
            intCode.multiply()
        elif intCode.opcode == 3:
            intCode.getInput(flipper.getJoystickPos())
        elif intCode.opcode == 4:
            flipper.handleOutput(intCode.sendOutput())
        elif intCode.opcode == 5:
            intCode.jumpIfTrue()
        elif intCode.opcode == 6:
            intCode.jumpIfFalse()
        elif intCode.opcode == 7:
            intCode.ifLessThan()
        elif intCode.opcode == 8:
            intCode.ifEquals()
        elif intCode.opcode == 9:
            intCode.setBasePointer()
        elif intCode.opcode == 99:
            print("OpCode 99 Exit")
            flipper.screen.countBlockTiles()
            drawImage(flipper.screen)
            sys.exit(0)
        else:
            print("Error no opCode??!!")
            sys.exit(0)
        instrPoint = intCode.getInstrPointer() # Get back the updated instruction pointer
        relativeBase = intCode.getBasePointer() # and alsi the BasePointer or as called Relative Pointer.
    print("Didn't find a solution!!!!!!")

if __name__ == "__main__":
    main()
