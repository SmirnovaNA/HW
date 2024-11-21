class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal, Plant):

    def eat(self, food):
        if food abidle:
            print()

class Predator(Animal, Plant):
    abidle = True

class Flower(Plant, Animal):


class Fruit(Plant, Animal):


