def gen_func():
    for i in range(1,6):
        yield i

for number in gen_func():
    print(number)