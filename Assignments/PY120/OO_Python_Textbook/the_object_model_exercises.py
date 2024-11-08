class Person:

    @classmethod
    def validate_name(cls,name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not name.isalpha():
            raise ValueError('Name must only include alphabetic characters')


    def __init__(self, firstname:str, lastname:str):
        Person.validate_name(firstname)
        Person.validate_name(lastname)

        self._full_name = (firstname.capitalize(), lastname.capitalize())

    @property
    def name(self):
        return self._full_name[0] + " " + self._full_name[1]

    @name.setter
    def name(self, fullname:tuple):
        print(fullname)
        firstname, lastname = fullname
        Person.validate_name(firstname)
        Person.validate_name(lastname)

        self._full_name = (firstname.capitalize(), lastname.capitalize())


