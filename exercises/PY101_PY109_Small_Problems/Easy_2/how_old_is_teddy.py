# How Old is Teddy?

from random import randint

def teddy_is():
    # randint is inclusive of its end points
    print(f'Teddy is {randint(20,100)} years old!')

for i in range(1,50):
    teddy_is()
    i +=1