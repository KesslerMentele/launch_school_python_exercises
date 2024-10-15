# Exercise 1:
**What happens when you run the following program? Why do we get that result?**
```python
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
```
foo raises an error because it is an unresolved reference. foo is a local variable inside the set_foo() function 
and is not available outside that function

# Exercise 2:
**Take a look at this code snippet:**
```python
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
```
**What does this program print? Why?**

The program prints 'bar' because the foo variable inside the set_foo() function is a local variable and not the global 
variable foo

# Exercise 3:
**Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter 
the two numbers, then output the numbers and result as a simple equation.**

answer in _multiply.py_

# Exercise 4:
**Consider this code:**
```python
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)
```

**Identify the following items in that code:**

| Item                  | Answer                                              |
|-----------------------|-----------------------------------------------------|
| function name         | multiply_numbers                                    |
| function arguments    | 2, 3, 4                                             |
| function definition   | the section from 'def' until after the return       |
| function body         | 'result = num1 * num2 * num3' and 'return result'   |
| function parameters   | num1, num1, num3                                    |
| function invocation   | the last line, where it is assigned to product      |
| function return value | result                                              |
| all identifiers       | multiply_numbers, num1, num2, num3, result, product |

# Exercise 5:
**What does the following code print?**
```python
def scream(words):
    return words + '!!!!'

scream('Yipeee')
```

The code does not print anything.

# Exercise 6:
**What does the following code print?**
```python
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
```

The code does not print anything.

# Exercise 7:
**Without running the following code, what do you think it will do?**
```python
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')
```

The code will raise an error because not enough arguments have been given to satisfy the functions' parameters.  

# Exercise 8:
**Without running the following code, what do you think it will do?**
```python
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
```
This code will raise an error because too many arguments have been given to the function.

# Exercise 9:
**Without running the following code, what do you think it will do?**
```python
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
```
This code will print:
```
42
3.141592
2.718
```
Even though the definition of the function provides default values for 'second' and 'third',
we have passed in values for all three, so our values will be used instead of the default values.

# Exercise 10:
**Without running the following code, what do you think it will do?**
```python

```
This code will print:
```
42
3.141592
2
```
We have passed in values for 'first' and 'second', but not for 'third'. Since 'third' has a default value of 2, that is 
what is printed.

# Exercise 11:
**Without running the following code, what do you think it will do?**
```python

```
This code will print:
```
42
3
2
```
We have passed a value for 'first', and let the default values for 'second' and 'third' be used.

# Exercise 12:
**Without running the following code, what do you think it will do?**
```python
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
```
This code will raise an error because the function is expecting a value for 'first', but none is given.

# Exercise 13:
**Without running the following code, what do you think it will do?**
```python
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
```
This code will raise an error because you cannot have an argument without a default value after an argument 
with a default value.

# Exercise 14:
**Identify all of the identifiers on each line of the following code.**
```
1.  def multiply(left, right):
2.       return left * right
3.
4.  def get_num(prompt):
5.       return float(input(prompt))
6.
7.  first_number = get_num('Enter the first number: ')
8.  second_number = get_num('Enter the second number: ')
9.  product = multiply(first_number, second_number)
10. print(f'{first_number} * {second_number} = {product}')
```
| Line | Identifiers                                    |
|------|------------------------------------------------|
| 1    | multiply, left, right                          |
| 2    | left, right                                    |
| 3    |                                                |
| 4    | get_num, prompt                                |
| 5    | prompt                                         |
| 6    |                                                |
| 7    | first_number, get_num                          |
| 8    | second_number, get_num                         |
| 9    | product, multiply, first_number, second_number |
| 10   | first_number, second_number, product           |

# Exercise 15:
**Using the code below, classify the identifiers as global, local, or built-in. For our purposes, 
you may assume this code is the entire program.**
```python
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
```

| Type     | Identifiers                                             |
|----------|---------------------------------------------------------|
| built-in | def, return, float, input, print                        |
| global   | multiply, get_num, first_number, second_number, product |
| local    | left, right, prompt                                     |


# Exercise 16
**In the code shown below, identify all of the function names and parameters present in the code. 
Include the line numbers for each item identified.**
```python
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
```


| Name     | Type       | Line Defined | Line(s) Used |
|----------|------------|--------------|--------------|
| input    | Function   | Built-in     | 5            |
| float    | Function   | Built-in     | 5            |
| print    | Function   | Built-in     | 10           |
| multiply | Function   | 1            | 9            |
| get_num  | Function   | 4            | 7, 8         |
| left     | Parameter  | 1            | 2            |
| right    | Parameter  | 1            | 2            |
| prompt   | Parameter  | 4            | 5            |

# Exercise 17:
**Which of the identifiers in the following program are function names? Which are method names? 
Which are built-in functions?**

```python
def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))
```

| Type     | Identifiers       |
|----------|-------------------|
| function | say               |
| Built-in | print, input, max |
| method   | upper, lower      |

# Exercise 18:
**The following function returns a list of the remainders of dividing the numbers in numbers by 3:**
```python
def remainders_3(numbers):
    return [number % 3 for number in numbers]
```
**Use this function to determine which of the following lists contains at least one number that is not evenly divisible 
by 3 (that is, the remainder is not 0):**

```
numbers_1 = [0,1,2,3,4,5,6]
numbers_2 = [1,2,4,5]
numbers_3 = [0,3,6]
numbers_4 = []
```

numbers_1 and numbers_2 contain numbers that are not evenly divisible by 3


# Exercise 19:
**The following function returns a list of the remainders of dividing the numbers in numbers by 5:**
```python
def remainders_5(numbers):
    return [number % 5 for number in numbers]
```
**Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:**

```
numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []
```
numbers_2 and numbers_4 do not contain any numbers that are divisible by 5
