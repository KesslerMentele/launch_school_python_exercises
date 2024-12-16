import random
import string

class Robot:
    used_names = []


    def __init__(self):
        self.name = self.__class__.get_name()

    def reset(self):
        self.name = self.__class__.get_name()


    @classmethod
    def get_name(cls)->str:
        name = ''
        name += "".join(random.choices(string.ascii_uppercase, k=2))
        name += "".join(random.choices(string.digits, k=3))
        while name in cls.used_names:
            name = ''
            name += "".join(random.choices(string.ascii_uppercase, k=2))
            name += "".join(random.choices(string.digits, k=3))
        cls.used_names.append(name)

        return name
