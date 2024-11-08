class Car:

    def __init__(self, model: str, year: int, color: str):
        self._model: str = model
        self._year: int = year
        self._color: str = color
        self._speed: int = 0
        self._running = False

    def __str__(self):
        return f'{self.color} {self.year} {self.model}'

    def __repr__(self):
        return f'Car({repr(self.model)}, {repr(self.year)}, {repr(self.color)})'

    @classmethod
    def mileage(cls, gallons, miles):
        mileage = miles / gallons
        print(f'Mileage: {mileage}mpg')

    @property
    def speed(self):
        return self._speed

    @property
    def running(self):
        return self._running

    @running.setter
    def running(self, state):
        if self.running == state:
            print(f"Engine is already {"off" if not self.running else "on"}")
        else:
            self._running = state
            print(f"Engine is now {"not " if not self.running else ""}running")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('The color must be a string')
        self._color = color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    def engine_on(self):
        self.running = True

    def engine_off(self):
        self.running = False

    def accelerate(self):
        if self.running:
            self._speed += 1
            print(f'Speed is now {self.speed}mph')
        else:
            print("Can't accelerate if the engine is off!")

    def spray_paint(self, color):
        self.color = color
        print(f'You spray painted your car {color}? If it works, I guess.')

    def brake(self):
        if self.speed > 0:
            self._speed -= 1
        elif self.speed < 0:
            self._speed += 1
        else:
            return
        print(f'Speed is now {self.speed}mph')

hank = Car('Ford F-150', 1967, "White")
print(hank)
print(repr(hank))
hank.spray_paint('Green')
hank.engine_off()
hank.engine_on()
hank.engine_off()
hank.engine_on()
hank.accelerate()
hank.engine_off()
hank.brake()
hank.brake()
hank.brake()