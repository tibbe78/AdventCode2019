from dataclasses import dataclass
#from typing import Dict

@dataclass
class Score:
    ''' Class of the Segment Display '''
    def __init__(self):
        self.value = 0

    def UpdateScore(self, value):
        self.value = value
