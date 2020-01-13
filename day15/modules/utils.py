''' Utilites program '''

from dataclasses import dataclass

@dataclass
class Pointer():
    ''' Class to handle the instruction pointer and relative pointer '''
    instruction: int = 0
    relative: int = 0

    def __repr__(self):
        return f"i:{self.instruction}_r:{self.relative}"
