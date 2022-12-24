from animal.director import AnimalDirector

def main():
    animalDirector = AnimalDirector()
    cat = animalDirector.create_animal("cat")
    dog = animalDirector.create_animal("dog")
    bird = animalDirector.create_animal("bird")
    fish = animalDirector.create_animal("fish")

    for animal in [cat, dog, bird, fish]:
        print(f"\nSpecies : {animal.species}")
        print(f"Sound : {animal.sound}")
        print(f"Breath : {animal.breath}")
        print(f"Legs : {animal.legs}")
        print(f"Favorite Food : {animal.favorite_food}")



if __name__ == '__main__':
    main()