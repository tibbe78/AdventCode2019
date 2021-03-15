

class IntCode(object):
    def __init__(self, _instrPoint: int, _compMem: list):
        """
        Init the Class IntCode with the instruction pointer and a pointer to the ComputerMem (program)
        """
        self.blob = str(_compMem[_instrPoint])  # Like '1102'
        self.opcode = int(self.blob[-2:])  # start at -2 in string. Like '02' from blob
        self.param = list()  # parameters to the opcode as a list.
        self.value = list()  # values based on parameter & mode as a list
        self.pModesRaw = self.blob[
            :-2
        ]  # parameter modes, end at -2 in string. like '11' from above '1102' blob
        self.pModesRevList = list(self.pModesRaw)[
            ::-1
        ]  # Reversed list of the parameters
        self.pMode = [0, 0, 0]  # set the parameter modes default
        self.instrPoint = _instrPoint
        self.basePointer = None
        self.compMem = _compMem  # Pointer to the rest of the computerMem or program.
        # find & set parameter modes like [0,1,1] from above raw pmodes.
        for i in range(
            len(self.pModesRevList)
        ):  # for each parameter we have a setting for. Else 0
            self.pMode[i] = int(
                self.pModesRevList[i]
            )  # set the pmode to the pmode in the list

    def reset(self,intPoint:int, baseP:int):
        self.__init__(intPoint,self.compMem)
        self.basePointer = baseP

    def getInstrPointer(self) -> int:
        return self.instrPoint

    def getBasePointer(self) -> int:
        return self.basePointer

    def setParameters(self, num, writeNum=9):
        """
        Set the parameters accompanying the Operation Code. Can be up to three
        parameters. num is equal to the amount of parameters and writeNum specifies if one
        of them is the write parameter and should be handled specially.
        """
        for i in range(num):  # Create one parameter at the time.
            paramLocation = self.instrPoint + (
                i + 1
            )  # the location of the parameter in the Computer Mem
            self.param.append(
                self.compMem[paramLocation]
            )  # Create the parameter to the opcode.

            # if the parameter refers to a memory outside of range, add more memory
            if (
                self.pMode[i] == 0 or self.pMode[i] == 2
            ):  # not applicable for direct mode.
                totalMem = (
                    (self.basePointer + self.param[i])
                    if self.pMode[i] == 2
                    else self.param[i]
                )
                if totalMem >= len(self.compMem):
                    for j in range(
                        totalMem - len(self.compMem) + 1
                    ):  # Add the amount of memory missing
                        self.compMem.append(0)

            # If the mode to parameter is 0 = Position mode.
            if self.pMode[i] == 0:
                if i == writeNum:
                    self.value.append(
                        self.param[i]
                    )  # if this is the write parameter send only back location
                else:
                    self.value.append(
                        self.compMem[self.param[i]]
                    )  # Else send back value of location

            # If the mode to parameter is 1 = Direct mode.
            elif self.pMode[i] == 1:
                self.value.append(self.param[i])

            # If the mode to parameter is 2 = Relative mode
            elif self.pMode[i] == 2:
                if i == writeNum:
                    self.value.append(self.basePointer + self.param[i])
                else:
                    self.value.append(self.compMem[self.basePointer + self.param[i]])

            else:
                print("Error!!")

    def add(self):  # Add function that Add two values together
        self.setParameters(3, 2)
        self.compMem[self.value[2]] = self.value[0] + self.value[1]
        self.instrPoint += 4

    def multiply(self):  # Add function that Multiply two values together
        self.setParameters(3, 2)
        self.compMem[self.value[2]] = self.value[0] * self.value[1]
        self.instrPoint += 4

    def getInput(self, flipperinput : int):
        self.setParameters(1, 0)
        self.compMem[self.value[0]] = flipperinput
        self.instrPoint += 2

    def sendOutput(self):
        self.setParameters(1)
        self.instrPoint += 2
        return self.value[0]

    def jumpIfTrue(self):
        self.setParameters(2)
        if self.value[0] != 0:
            self.instrPoint = self.value[1]
        else:
            self.instrPoint += 3

    def jumpIfFalse(self):
        self.setParameters(2)
        if self.value[0] == 0:
            self.instrPoint = self.value[1]
        else:
            self.instrPoint += 3

    def ifLessThan(self):
        self.setParameters(3, 2)
        if self.value[0] < self.value[1]:
            self.compMem[self.value[2]] = 1
        else:
            self.compMem[self.value[2]] = 0
        self.instrPoint += 4

    def ifEquals(self):
        self.setParameters(3, 2)
        if self.value[0] == self.value[1]:
            self.compMem[self.value[2]] = 1
        else:
            self.compMem[self.value[2]] = 0
        self.instrPoint += 4

    def setBasePointer(self):
        self.setParameters(1)
        self.basePointer += self.value[0]
        self.instrPoint += 2

    def __repr__(self):
        return "OpCode: {}".format(self.opcode)
