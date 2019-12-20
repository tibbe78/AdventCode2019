from dataclasses import dataclass

@dataclass
class Plate:
    ''' Class of one plate of the hull '''
    def __init__(self,x,y, color=0):
        self.x = x
        self.y = y  
        self.timesTraversed = 1
        self.color = color
        self.name = "Plate_X:{}_Y:{}".format(self.x, self.y)
            
    def __repr__(self):
        return self.name