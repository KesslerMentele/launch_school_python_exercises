class Cat:
    count = 0

    def __init__(self):
        Cat.count += 1

    @classmethod
    def total(cls):
        return cls.count



print(Cat.total())         # 0

kitty1 = Cat()
print(Cat.total())         # 1

kitty2 = Cat()
print(Cat.total())         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
print(Cat.total() )        # 3