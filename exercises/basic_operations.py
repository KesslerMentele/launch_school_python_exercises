
def basic_ops_exercise1():
    first_name = 'Kessler'
    last_name =  'Mentele'
    print('Basic Operations Exercise 1:')
    print("# Concatenate two strings, one with your first name and one with your last,\n"
          "# to create a new string with your full name as its value.\n"
          "# For example, if your name is John Doe,\n"
          "# you should combine 'John' and 'Doe' to get 'John Doe'. \n")
    print(first_name + " " + last_name + '\n')


def basic_ops_exercise2():
    print('Basic Operations Exercise 2:')
    print(
        '# Use the REPL and the arithmetic operators to extract the individual digits of 4936:\n'
        '# One place is 6.\n'
        '# Tens place is 3.\n'
        '# Hundreds place is 9.\n'
        '# Thousands place is 4.\n'
        '# Each digit may require multiple Python statements.\n'
        '# number = 4936\n'
        '>>> num = 4936\n'
        '>>> ones = 4936 % 10\n'
        '>>> tens = (4936 // 10) % 10\n'
        '>>> hundreds = (4936 // 100) % 10\n'
        '>>> thousands = (4936 // 1000) % 10\n'
        '>>> num\n'
        '4936\n'
        '>>> ones\n'
        '6\n'
        '>>> tens\n'
        '3\n'
        '>>> hundreds\n'
        '9\n'
        '>>> thousands\n'
          '4 \n'
          )


def basic_ops_exercise_3_4():
    print('Basic Operations Exercise 3 and 4: ')
    print("print('5' + '10')")
    print('This line prints \'510\' because both values are stings,' +
          'it uses string concatenation to append them together ')
    print(int('5') + int('10'), '\n')


def basic_ops_exercise_5():
    print('Basic Operations Exercise 5:')
    print("# Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:")
    print("# foo = ['a', 'b', 'c']")
    print("# print(foo[3])      # will this result in an error?\n")
    print("Yes, the given example will raise an error, " +
          "because you cant access an index that is out of range.\n")


def basic_ops_exercise_6():
    print('Basic Operations Exercise 6: ')
    print('# To what value does the following expression evaluate? ')
    print('# \'foo\' == \'Foo\' \n')
    print('The expression "\'foo\' == \'Foo\'" evaluates to False because ' +
          'the strings are not equal, as capitalization matters. \n' )


def basic_ops_exercise_7():
    print('Basic Operations Exercise 7:')
    print('# What will the following code do? Why? ')
    print('# int(\'3.1415\') \n')
    print('The code "int(\'3.1415\')" will raise an error, as \'3.1415\'' +
          ' is not a valid integer \n' )


def basic_ops_exercise_8():
    print('Basic Operations Exercise 8:')
    print('# To what value does the following expression evaluate?')
    print('# \'12\' < \'9\'\n')
    print('The expression will evaluate to true, because it will compare the ' +
          'two values as strings, and 1 is less than 9. \n')

def main():
    basic_ops_exercise1()
    basic_ops_exercise2()
    basic_ops_exercise_3_4()
    basic_ops_exercise_5()
    basic_ops_exercise_6()
    basic_ops_exercise_7()
    basic_ops_exercise_8()



if __name__ == "__main__":
    main()
