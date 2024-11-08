class Person:


    @classmethod
    def validate_name(cls, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')

    def __init__(self, name):
        Person.validate_name(name)
        self._first_name = name
        self._last_name = ''

    def __str__(self):
        return self.name


    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'

    @name.setter
    def name(self, name):
        Person.validate_name(name)
        names = name.split()
        if len(names) > 2:
            raise ValueError("Name can only be up to two words")
        self.first_name = names[0]
        if len(names) == 2:
            self.last_name = names[1]
        else:
            self.last_name = ''


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        Person.validate_name(first_name)
        self._first_name = first_name


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        Person.validate_name(last_name)
        self._last_name = last_name

bob = Person('Robert Smith')
rob = Person('Robert Smith')