# Exercise 1:
**To what values do the following expressions evaluate?**
```python
False or (True and False)
True or (1 + 2)
(1 + 2) or True
True and (1 + 2)
False and (1 + 2)
(1 + 2) and True
(32 * 4) >= 129
False != (not True)
True == 4
False == (847 == '847')
```
| Expression                | Value |
|---------------------------|-------|
| False or (True and False) | False |
| True or (1 + 2)           | True  |
| (1 + 2) or True           | 3     |
| True and (1 + 2)          | 3     |
| False and (1 + 2)         | False |
| (1 + 2) and True          | True  |
| (32 * 4) >= 129           | False |
| False != (not True)       | False |
| True == 4                 | False |
| False == (847 == '847')   | True  |


# Exercise 2:
**Write a function, even_or_odd, that determines whether its argument is an even or odd number. 
If it's even, the function should print 'even'; otherwise, it should print 'odd'. 
Assume the argument is always an integer.**

```python
def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
```

# Exercise 3:
**Without running the following code, what does it print? Why?**

The code prints the following:
```
Product1
Product not found!
```

# Exercise 4:
**Refactor this statement to use a regular if statement instead.**

```python
return ('bar' if foo() else qux())
```

Answer:

```python
if foo():
    return 'bar'
else:
    return qux()
```

# Exercise 5:
**What does this code output, and why?**

```python
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])
```

The code outputs the following:
```
Empty
```

# Exercise 6:
**Write a function that takes a string as an argument and returns an all-caps version of the string when the string is 
longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 
'HELLO WORLD', but don't change 'goodbye'.**

```python
def is_long_string(string_to_test):
    if len(string_to_test) > 10:
        print(string_to_test.upper())
    else:
        print(string_to_test)
```

# Exercise 7:
**Write a function that takes a single integer argument and prints a message that describes whether:**

- the value is between 0 and 50 (inclusive)
- the value is between 51 and 100 (inclusive)
- the value is greater than 100
- the value is less than 0

```python
def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')
```

