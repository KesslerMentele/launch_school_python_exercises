class Foo:
    def __init__(self, name):
        self.name = name

one = Foo("uno")
two = Foo("dos")

print(f'I am a {type(one).__name__} object')
print(f'I am a {one.__class__.__name__} object')