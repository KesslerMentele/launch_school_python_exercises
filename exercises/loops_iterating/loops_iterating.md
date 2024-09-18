# Exercise 1
**The following code causes an infinite loop (a loop that never stops iterating). Why?**

```python
counter = 0

while counter < 5:
    print(counter)
```

Because `counter` is never changed

# Exercise 2
**Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter.
The updated code should use a for loop to display the future ages.**

updated code in _age_2.py_

# Exercise 3
**Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.**

```python
my_list = [6, 3, 0, 11, 20, 4, 17]
```

```Expected Output
6
3
0
11
20
4
17
```

```python
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for item in my_list:
    print(item)
```

# Exercise 4
**Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.**

```python
my_list = [6, 3, 0, 11, 20, 4, 17]
```

```python
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index > len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1
        
for item in my_list:
    if item % 2 != 0:
        print(item)

```

# Exercise 5
**Print all of the even numbers in the following list of nested lists. Don't use any while loops.**
```python
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
```

```python
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
for sub_list in my_list:
    for item in sub_list:
        if item % 2 == 0:
            print(item)
```

# Exercise 6

**Let's try another variation on the even/odd-numbers theme.**

**We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that creates a 
new list with one element for each number in my_list. If the original number is an even, then the corresponding element 
in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.**

```python
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
```

```python
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for item in my_list:
    if item % 2 == 0:
        new_list += {'even'}
    else:
        new_list += {'odd'}

```


# Exercise 7
**Write a find_integers function that returns a list of all the integers from my_tuple:**

```python
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
```

```python
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(data):
    new_list = []
    for item in data:
        if type(item) is int:
            new_list.append(item)
    return new_list

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
```

# Exercise 8
**Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the 
corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of 
strings.**

```python
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}
```

```python
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {}

for item in my_set: 
    if len(item) % 2 != 0:
        my_dict[item] = len(item)

print(my_dict)

```


# Exercise 9
**Write a function that computes and returns the factorial of a number by using a for or while loop. 
The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, 
inclusive:**

| n! | Expansion         | Result |
|----|-------------------|--------|
| 1! | 1                 | 1      |
| 2! | 1 * 2             | 2      |
| 3! | 1 * 2 * 3         | 3      |
| 4! | 1 * 2 * 3 * 4     | 24     |
| 5! | 1 * 2 * 3 * 4 * 5 | 120    |

```python
def factorial(number):
    index = 1
    result = 1
    while index <= number:
        result *= index
        index += 1

    return result

```

# Exercise 10
**The following code uses the randrange function from Python's random library to obtain and print a random integer
within a given range. Using a while loop, it keeps running until it finds a random number that matches the last number 
in the range. Refactor the code so it doesn't require two different invocations of randrange.**

```python
import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
```

```python
import random

highest = 10
number = 0
while number != highest:
    number = random.randrange(highest + 1)
    print(number)
```


# Exercise 11
**Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.**

```python
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
```

```python
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
index = 0

while index < len(my_list):
    second_index = 0

    while second_index < len(my_list[index]):
        if my_list[index][second_index] % 2 == 0:
            print(my_list[index][second_index])
        second_index += 1
    index += 1
```
