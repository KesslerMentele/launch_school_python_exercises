class Vehicle:

    def __init__(self, wheels:int = 4):
        if not isinstance(wheels, int) or wheels < 0:
            raise TypeError('Wheel count must be a positive integer')
        self._wheels = wheels
        print(f'I have {self._wheels} wheels.')

    @staticmethod
    def drive(self):
        print('I am driving')

class Car(Vehicle):
    def __init__(self):
        print('Made a car.')
        super().__init__(4)
    pass

class Truck(Vehicle):
    def __init__(self):
        print('Made a Truck.')
        super().__init__(18)
    pass

class Motorcycle(Vehicle):
    def __init__(self):
        print('Made a Motorcycle.')
        super().__init__(2)

    def drive(self):
        print('I am riding')

class Pet:
    def play(self):
        print('I am playing')

class Predator:
    def hunt(self):
        print('I am hunting')

class Cat(Pet, Predator):
    def purr(self):
        print('I am purring')

class Shape:
    def __init__(self, width:int | float, height:int | float):
        self.height = None
        self.width = None
        self.set_size(width, height)

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        my_area = self.width * self.height
        print(f'My area is {my_area}')

class Rectangle:
    def __init__(self, width, height):
        self._shape = Shape(width, height)

    def set_width(self, width):
        self._shape.set_size(width, self._shape.height)
    def set_height(self, height):
        self._shape.set_size(self._shape.width, height)
    def area(self):
        self._shape.area()

class Square:
    def __init__(self, size):
        self._shape = Shape(size, size)


    def set_size(self, size):
        self._shape.set_size(size, size)

    def area(self):
        self._shape.area()

class LandDwellingMixin:
    pass

class LanguageMixin:
    pass

class BipedalismMixin:
    pass

class Creature:
    pass

class Mammal(Creature):
    pass

class Primate(LandDwellingMixin, Mammal):
    pass

class Human(BipedalismMixin, LanguageMixin, Primate):
    pass

