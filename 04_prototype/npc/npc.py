import time
from abc import ABC, abstractmethod

class NPC(ABC):
    def __init__(self):
        # Mock long process method
        time.sleep(2)
        
        self.height = None
        self.age = None
        self.health = None
        self.mana = None
    
    @abstractmethod
    def clone(self):
        pass