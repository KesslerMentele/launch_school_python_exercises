class Pet:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def fetch(self):
        return 'fetching!'


class Dog(Pet):
    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

class Cat(Pet):
    pass

teddy = Bulldog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

