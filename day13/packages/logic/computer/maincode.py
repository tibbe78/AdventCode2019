import sys
from day13.packages.logic.flipper.flipper_logic import FlipperLogic
from .intcode import IntCode

class MainCode(object):
    def __init__(self, opCodeList: list, startValue: int):
        _flipper = FlipperLogic()
        # instruction pointer in the opcode so we know where in the code we are.
        instrPoint = 0
        # Relative Base Pointer, will be changed by the program.
        relativeBase = 0
        # Add quarters to play for free
        opCodeList[0] = startValue
        # Go through the oplist and check the values
        while instrPoint < len(opCodeList):
            intCode = IntCode(instrPoint,opCodeList) # init the IntCode class
            intCode.setBasePointer(relativeBase) # set the basePointer
            if intCode.opcode == 1: intCode.add()
            elif intCode.opcode == 2: intCode.multiply()
            elif intCode.opcode == 3: intCode.getInput(_flipper.getJoystickPos())
            elif intCode.opcode == 4: _flipper.handleOutput(intCode.sendOutput())
            elif intCode.opcode == 5: intCode.jumpIfTrue()
            elif intCode.opcode == 6: intCode.jumpIfFalse()
            elif intCode.opcode == 7: intCode.ifLessThan()
            elif intCode.opcode == 8: intCode.ifEquals()
            elif intCode.opcode == 9: intCode.setBasePointer()
            elif intCode.opcode == 99:
                print("Game Quit")
                print("Arcade Score: {}".format(_flipper.score.value))
                self.quit()
                sys.exit(0)
            else:
                print("Error no opCode??!!")
                sys.exit(0)
            # Get back the updated instruction pointer
            instrPoint = intCode.getInstrPointer()
            # and also the BasePointer or as called Relative Pointer.
            relativeBase = intCode.getBasePointer()
        print("Didn't find a solution!!!!!!")