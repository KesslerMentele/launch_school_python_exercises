def gen_func():
    word = ''
    while word != 'stop':
        word = input('Say Something')
        yield word


for string in gen_func():
    print(string)