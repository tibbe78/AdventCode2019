from dataclasses import dataclass
#from typing import Dict

@dataclass
class Output:
    ''' Class of the Ball '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = 0
        self.state = 0

    def Update(self,data):
        if self.state == 0:
            self.state += 1
            self.x = data
        elif self.state == 1:
            self.state += 1
            self.y = data
        elif self.state == 2:
            self.state = 0
            self.type = data

