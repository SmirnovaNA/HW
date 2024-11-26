class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _coords = [0, 0, 0]
    _speed = ()
    def move(self, dx, dy, dz):
        self.dx = dx*_speed
        self.dy = dy
        self.dz = dz

    def get_cords(self):
        return (f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        if super._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        from random import randint
        print(f'Here are(is)', randint (1,4), 'eggs for you"')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.dz = dz
        return super._coords.appens(self.dz)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Animal, Bird, AquaticAnimal):
    sound = "Click-click-click"