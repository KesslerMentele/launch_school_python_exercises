class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width




rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True