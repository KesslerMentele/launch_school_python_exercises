class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return 'Name not set!'


dog1 = Dog('Golden Retriever')
dog2 = Dog('Poodle')
print(dog1.get_breed())
print(dog2.get_breed())

cat1 = Cat()
print(cat1.get_name())


dog3 = Dog('test')
dog3._breed = 'Labrador'
print(dog3.get_breed())

class Student:
    school_name = 'Oxford'

    @classmethod
    def get_school(cls):
        return cls.school_name

    def __init__(self, name):
        self.name = name


student1 = Student('chris')
student2 = Student('amy')

print(student1.name)
print(student1.school_name)
print(student2.name)
print(student2.school_name)

print(Student.get_school())
print(Student.school_name)

class Car:
    manufacturer = 'Ford'

    def __init__(self):
        self.manufacturer = 'BMW'

    def show_manufacturer(self):
        print(self.manufacturer)
        print(Car.manufacturer)

car1 = Car()
car1.show_manufacturer()


class Bird:
    species = ''
class Sparrow(Bird):
    species = 'sparrow'

sparrow = Sparrow()
print(sparrow.species)



class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

john = Human()
print(john.legs)