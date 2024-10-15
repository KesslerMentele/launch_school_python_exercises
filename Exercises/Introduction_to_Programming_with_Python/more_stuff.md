# Exercise 1:
**What does the following function do? Be sure to identify the output value.**
```python
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
```

do_something gets the view of the dictionary parameters' keys, sorts them, then returns the second key in uppercase.

my_dict.keys() would return `dict_keys(['Karl', 'Clare', 'Karis', 'Trevor', 'Antonina', 'Chris'])`

then sorted would become `['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor']`

The value at position [1] is 'Chris', so .upper() would make is 'CHRIS'

The code will print 'CHRIS'

# Exercise 2:
**Use the sqrt function from the math library to write some code that outputs the square root of 37. 
Try to write the code in three different ways.**

```python
from math import sqrt

ans = sqrt(37)
print(ans)
```

```python
import math

ans = math.sqrt(37)
print(ans)
```
```python
import math as mat

ans = mat.sqrt(37)
print(ans)
```

# Exercise 3:
**Consider the following code:**
```python
def sum_of_squares(num1, num2):
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)
```

Write a nested function in sum_of_squares that will make this code work as shown.

```python
def sum_of_squares(num1, num2):
    def square(num):
        return num**2
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

```

# Exercise 4:
**Write a function called increment_counter that increments a counter variable every time it is called. 
You can test your code with the following:**

```python
print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
```

```python
counter = 0

def increment_counter():
    global counter
    counter += 1
```

# Exercise 5:
**On reflection, we've decided that we don't want to rely on using a global variable in the code we wrote in the 
previous example. To fix this, we're going to nest the code from the previous example into an outer function:**

```python
def all_actions():
    counter = 0

    def increment_counter():
        global counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()
```

Counter is not a global variable.