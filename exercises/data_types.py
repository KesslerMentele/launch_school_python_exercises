def data_types_exercise1():
    data = """
    | Value          | Data Type |
    |----------------|-----------|
    | 'True'         | string    |
    | False          | boolean   |
    | (1, 2, 3)      | tuple     |
    | 1.5            | float     |
    | [1, 2, 3]      | list      |
    | 2              | int       |
    | range(5)       | range     |
    | {1, 2, 3}      | set       |
    | None           | noneType  |
    | {'foo': 'bar'} | dict      |
    """
    print(f'Data Types Exercise 1: {data}')
    print('\n')


def data_types_exercise2():
    pets = {
        'Asta': 'dog',
        'Butterscotch': 'cat',
        'Pudding': 'cat',
        'Neptune': 'fish',
        'Darwin': 'lizard',
    }
    print(f'Data Types Exercise 2: \n {pets}')
    print('\n')


def main():
    data_types_exercise1()
    data_types_exercise2()

if __name__ == "__main__":
    main()