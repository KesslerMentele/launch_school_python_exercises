#
# Program to determine whether a triangle is Equilateral, Isosceles, or Scalene
# Equilateral: All sides of equal length
# Isosceles: 2 sides of equal length
# Scalene: No sides with equal length
# Valid Triangles have:
#  - The sum of any 2 sides > the third side
#  - All sides must be > 0

# Traingle class must have property 'kind'
# Triangle class must be initialized with 3 numbers (int or float)
# If a Traingle is initialized with an Illegal value, raise a ValueError
# Traingle.kind must return on of the following strings:
# "scalene"
# "isosceles"
# "equilateral"

class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        if not all([isinstance(itm, int) or isinstance(itm, float) for itm in self.sides]):
            raise TypeError('All args must be numbers!')
        self.check_lengths()
        if any([side <=0 for side in self.sides]):
            raise ValueError('All sides must be greater than 0')



    @property
    def sides(self):
        return self._a, self._b, self._c


    @property
    def kind(self):
        if self._a == self._b == self._c:
            return "equilateral"
        elif any([self._a == self._b, self._b == self._c, self._a == self._c]):
            return "isosceles"
        else:
            return "scalene"

    def check_lengths(self):
        if not ((self._a + self._b) > self._c
                and (self._a + self._c) > self._b
                and (self._b + self._c) > self._a):
            raise ValueError

