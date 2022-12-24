from .builder import AnimalBuilder
from .animal import Animal

class AnimalDirector():
    def __init__(self):
        self.builder = AnimalBuilder()

        self.animal_recipe = {
            "cat":self.build_cat,
            "dog":self.build_dog,
            "bird":self.build_bird,
            "fish":self.build_fish,
        }

    def  create_animal(self, type:str):
        if type in self.animal_recipe.keys():
            return self.animal_recipe[type]()
        else:
            raise Exception(f'animal with {type} type not supported!')

    def build_cat(self) -> Animal:
        self.builder.reset()
        self.builder.set_species("Cat")
        self.builder.set_sound("Meow")
        self.builder.set_breath("Air")
        self.builder.set_legs(4)
        self.builder.set_favorite_food("Fish")
        return self.builder.get_animal()

    def build_dog(self) -> Animal:
        self.builder.reset()
        self.builder.set_species("Dog")
        self.builder.set_sound("Wouf")
        self.builder.set_breath("Air")
        self.builder.set_legs(4)
        self.builder.set_favorite_food("Meat")
        return self.builder.get_animal()

    def build_bird(self) -> Animal:
        self.builder.reset()
        self.builder.set_species("Bird")
        self.builder.set_sound("Tweet tweet")
        self.builder.set_breath("Air")
        self.builder.set_legs(2)
        self.builder.set_favorite_food("Seeds")
        return self.builder.get_animal()

    def build_fish(self) -> Animal:
        self.builder.reset()
        self.builder.set_species("Fish")
        self.builder.set_sound("...")
        self.builder.set_breath("Water")
        self.builder.set_legs(0)
        self.builder.set_favorite_food("Plankton")
        return self.builder.get_animal()
    