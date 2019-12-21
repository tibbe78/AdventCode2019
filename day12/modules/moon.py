from dataclasses import dataclass
from typing import List

@dataclass
class Moon:
    ''' class for each moon '''
    def __init__(self, id , name : str, x, y, z):
        self.name = name
        self.id = id
        # 3D Position x,y,z
        self.position = list()
        self.position.append(x)
        self.position.append(y)
        self.position.append(z)
        # 3D Velocity x,y,z
        self.velocity = list()
        self.velocity.append(0)
        self.velocity.append(0)
        self.velocity.append(0)
        self.potential = 0
        self.kinetic = 0
        self.totalEnergy = 0

    def CalcEnergy(self) -> int:
        self.potential = 0
        self.kinetic = 0
        for i in range(3):
            self.potential += abs(self.position[i])
            self.kinetic += abs(self.velocity[i])
        self.totalEnergy = self.potential * self.kinetic
        return self.totalEnergy

    def CalcGravity(self, moonlist: List['Moon']):
        for moon2 in moonlist:
            if self.id != moon2.id:
                for i in range(3):
                    if self.position[i] < moon2.position[i]:
                        self.velocity[i] += 1
                    if self.position[i] > moon2.position[i]:
                        self.velocity[i] -= 1

    def CalcPosition(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def __repr__(self):
        return self.name