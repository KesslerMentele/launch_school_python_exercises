class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name


bob = Person('Bob')
print(bob.name)
bob.name = 'Joe'
print(bob.name)



class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class SmartLamp:
    def __init__(self, color, brightness):
        self.color = color
        self.brightness = brightness

    def glow(self):
        return (f'The lamp glows {self.color} with brightness {self.brightness}%.')

    @property
    def color(self):                    # Getter for _color
        return self._color

    @color.setter
    def color(self, color):             # Setter for _color
        if not isinstance(color, str):
            raise TypeError('Color must be a color name.')

        self._color = color
    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        if not isinstance(brightness, int):
            raise TypeError('Brightness must be an integer')
        if not (100 >= brightness >= 0):
            raise ValueError('Brightness must be between 0 and 100')
        self._brightness = brightness


lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.