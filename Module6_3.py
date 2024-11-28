class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _coords = [0, 0, 0]

    def __init__(self, _speed):
        self._speed = _speed

    def move(self, dx, dy, dz):
        x_new = dx*self._speed
        y_new = dy*self._speed
        z_new = dz*self._speed
        if z_new < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[0] = x_new
            self._coords[1] = y_new
            self._coords[2] = z_new

        self.dx = dx*self._speed
        self.dy = dy*self._speed
        self.dz = dz*self._speed

    def get_cords(self):
        print(f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
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
        self._coords[2] = self._coords[2] - (abs(dz)*(self._speed/2))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
