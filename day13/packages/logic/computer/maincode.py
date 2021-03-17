import sys
from ..flipper.flipper_logic import FlipperLogic
from .intcode import IntCode

class MainCode(object):
    def __init__(self, opCodeList: list, startValue: int):
        self.flipper = FlipperLogic()
        # instruction pointer in the opcode so we know where in the code we are.
        self.instrPoint = 0
        # Relative Base Pointer, will be changed by the program.
        self.relativeBase = 0
        self.opCodeList = opCodeList
        # Special for second version as 2 initiates continues
        self.opCodeList[0] = startValue
        self.intCode = IntCode(self.instrPoint,self.opCodeList, self.relativeBase) # init the IntCode class

    def runCodeOnce(self) -> int:        
        # Go through the oplist and check the values
        while self.instrPoint < len(self.opCodeList):
            self.intCode.__init__(self.instrPoint, self.opCodeList, self.relativeBase)
            if self.intCode.opcode == 1: self.intCode.add()
            elif self.intCode.opcode == 2: self.intCode.multiply()
            elif self.intCode.opcode == 3: 
                self.intCode.getInput(self.flipper.getJoystickPos())
                # Get back the updated instruction pointer
                self.instrPoint = self.intCode.getInstrPointer()
                # and also the BasePointer or as called Relative Pointer.
                self.relativeBase = self.intCode.getBasePointer()
                # 1 = render screen
                #return 1
            elif self.intCode.opcode == 4: self.flipper.handleOutput(self.intCode.sendOutput())
            elif self.intCode.opcode == 5: self.intCode.jumpIfTrue()
            elif self.intCode.opcode == 6: self.intCode.jumpIfFalse()
            elif self.intCode.opcode == 7: self.intCode.ifLessThan()
            elif self.intCode.opcode == 8: self.intCode.ifEquals()
            elif self.intCode.opcode == 9: self.intCode.setBasePointer()
            elif self.intCode.opcode == 99:
                print("Game Quit")
                print("Arcade Score: {}".format(self.flipper.score))
                # 0 = quit
                return 2
            else:
                print("Error no opCode??!!")
                return 0
            # Get back the updated instruction pointer
            self.instrPoint = self.intCode.getInstrPointer()
            # and also the BasePointer or as called Relative Pointer.
            self.relativeBase = self.intCode.getBasePointer()
        print("Didn't find a solution!!!!!!")
        return 0