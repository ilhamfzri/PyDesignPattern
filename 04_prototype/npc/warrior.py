import copy
from .npc import NPC

class Warrior(NPC):
    def __init__(self, height:int, age:int, sword_name:str, sword_power:int):
        super().__init__()
        self.height = height
        self.age = age
        self.sword_name = sword_name
        self.sword_power = sword_power

    def sword_attack(self):
        print(f'Attack with {self.sword_name} staff with {self.sword_power} damage')
    
    def clone(self):
        return copy.deepcopy(self)
