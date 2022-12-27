import copy
from .npc import NPC

class Mage(NPC):
    def __init__(self, height:int, age:int, staff_name:str, staff_power:int):
        super().__init__()
        self.height = height
        self.age = age
        self.staff_name = staff_name
        self.staff_power = staff_power

    def staff_attack(self):
        print(f'Attack with {self.staff_name} staff with {self.staff_power} damage')
    
    def clone(self):
        return copy.deepcopy(self)