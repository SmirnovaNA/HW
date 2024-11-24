class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}' )

    def get_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        print(self.get_model, self.get_horsepower, self.get_color, 'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        self.new_color = new_color
        if new_color.upper() in self.__COLOR_VARIANTS:
            _color = new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')

class Sedan(Vehicle):
    pass

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()