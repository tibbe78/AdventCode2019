#!/usr/bin/env python3
# --- Day 13: Care Package ---
# Part Two

import sys
from day13.modules.arcadewindow import ArcadeWindow


def main():
    try:
        file = open('./day13_input.txt', 'r')
    except IOError:
        print("Can't open file!!")
        sys.exit(0)
    opCodeRaw = file.readline().strip()
    file.close()
    opCodeList = list(map(int, opCodeRaw.split(","))).copy()
    _arcadeWindow = ArcadeWindow()
    _arcadeWindow.setup()
    _arcadeWindow.start()


if __name__ == "__main__":
    main()


def ProcessIntCode():
    _flipper = Flipper()
    # instruction pointer in the opcode so we know where in the code we are.
    instrPoint = 0
    # Relative Base Pointer, will be changed by the program.
    relativeBase = 0
    # Add quarters to play for free
    opCodeList[0] = 2
    # Go through the oplist and check the values
    while instrPoint < len(opCodeList):
        intCode = IntCode(instrPoint,opCodeList) # init the IntCode class
        intCode.SetBasePointer(relativeBase) # set the basePointer
        if intCode.opcode == 1: intCode.Add()
        elif intCode.opcode == 2: intCode.Multiply()
        elif intCode.opcode == 3: intCode.GetInput(_flipper)
        elif intCode.opcode == 4: intCode.SendOutput(_flipper)
        elif intCode.opcode == 5: intCode.JumpIfTrue()
        elif intCode.opcode == 6: intCode.JumpIfFalse()
        elif intCode.opcode == 7: intCode.IfLessThan()
        elif intCode.opcode == 8: intCode.IfEquals()
        elif intCode.opcode == 9: intCode.ChangeBase()
        elif intCode.opcode == 99:
            print("Game Quit")
            print("Arcade Score: {}".format(_flipper.score.value))
            _arcadeWindow.quit()
            sys.exit(0)
        else:
            print("Error no opCode??!!")
            sys.exit(0)
        # Get back the updated instruction pointer
        instrPoint = intCode.GetInstrPointer()
        # and also the BasePointer or as called Relative Pointer.
        relativeBase = intCode.GetBasePointer()
    print("Didn't find a solution!!!!!!")
