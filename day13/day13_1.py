#!/usr/bin/env python3
# --- Day 13: Care Package ---
# Part One

import sys
from day13.modules.flipper_logic import FlipperLogic


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
    
    intCode = IntCode(instrPoint, opCodeList)  # init the IntCode class

    # Go through the oplist and check the values
    while instrPoint < len(opCodeList):
        intCode.reset(instrPoint,relativeBase)
        if intCode.opcode == 1:
            intCode.Add()
        elif intCode.opcode == 2:
            intCode.Multiply()
        elif intCode.opcode == 3:
            intCode.GetInput()
        elif intCode.opcode == 4:
            intCode.SendOutput()
        elif intCode.opcode == 5:
            intCode.JumpIfTrue()
        elif intCode.opcode == 6:
            intCode.JumpIfFalse()
        elif intCode.opcode == 7:
            intCode.IfLessThan()
        elif intCode.opcode == 8:
            intCode.IfEquals()
        elif intCode.opcode == 9:
            intCode.ChangeBase()
        elif intCode.opcode == 99:
            print("OpCode 99 Exit")
            flipper.screen.CountBlockTiles()
            DrawImage(flipper.screen)
            sys.exit(0)
        else:
            print("Error no opCode??!!")
            sys.exit(0)
        instrPoint = (
            intCode.GetInstrPointer()
        )  # Get back the updated instruction pointer
        relativeBase = (
            intCode.GetBasePointer()
        )  # and alsi the BasePointer or as called Relative Pointer.

    print("Didn't find a solution!!!!!!")


if __name__ == "__main__":
    main()
