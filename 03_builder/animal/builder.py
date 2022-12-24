from .animal import Animal

class AnimalBuilder():
    def __init__(self):
        self.reset()

    def reset(self):
        self.animal = Animal()
    
    def set_species(self, species:str):
        self.animal.species = species
    
    def set_sound(self, sound:str):
        self.animal.sound = sound
    
    def set_breath(self, breath:str):
        self.animal.breath = breath
    
    def set_legs(self, legs:int):
        self.animal.legs = legs

    def set_favorite_food(self, favorite_food:str):
        self.animal.favorite_food = favorite_food
    
    def get_animal(self) -> Animal:
        return self.animal
