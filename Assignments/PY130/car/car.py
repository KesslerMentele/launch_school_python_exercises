class Car:
    def __init__(self):
        self._wheels = 4
        self._name = None

    @property
    def wheels(self):
        return self._wheels

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise ValueError("Name must be a string")
        self._name = val

    def __eq__(self, other):
        return isinstance(other, Car) and self.name == other.name