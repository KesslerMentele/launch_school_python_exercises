# Exercise 1:
**Write Python code to print the seventh number of range(0, 25, 3).**
```python
data = range(0,25,3)
print(data[6])
```

# Exercise 2:
**Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.**

```python
data = 'Launch School'
print(data[4,10])
```

# Exercise 3:
**Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the 
original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).**

```python
data = (1,2,3,4,5)
data_list = list(data)
data_list.reverse()
sliced_data = data_list[1:4]
result = tuple(sliced_data)
print(result)
```

# Exercise 4:
**This is a 3-part question. Consider the following dictionary:**
```
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
```
- **Part 1: Write some code to print Bark by accessing the element associated with the key Dog.**

```python
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])

```


- **Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.**


```python
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

if 'Lizard' not in pets.keys():
    print('None')
```

 -**Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.**

```python
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets.get('Lizard', '<silence>'))
```

# Exercise 5:
**Which of the following values can't be used as a key in a dict object, and why?**


`'cat'`  Can be used

`(3, 1, 4, 1, 5, 9, 2)` Can be used

`['a', 'b']` Cannot be used, mutable

`{'a': 1, 'b': 2}` Cannot be used, mutable

`range(5)` Can be used

`{1, 4, 9, 16, 25}` Cannot be used, mutable

`3` Can be used

`0.0` Can be used

`frozenset({1, 4, 9, 16, 25})` Can be used

# Exercise 6:
**What will the following code print?**

```python
1. print('abc-def'.isalpha())
2. print('abc_def'.isalpha())
3. print('abc def'.isalpha())
4. print('abc def'.isalpha() and
5.      'abc def'.isspace())
6. print('abc def'.isalpha() or
7.      'abc def'.isspace())
8. print('abcdef'.isalpha())
9. print('31415'.isdigit())
10. print('-31415'.isdigit())
11. print('31_415'.isdigit())
12. print('3.1415'.isdigit())
13. print(''.isspace())
```
```
False
False
False
False
False
True
True
False
False
False
False
```

# Exercise 7:
**Write Python code to replace all the : characters in the string below with +.**
```python
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
```

```python
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info = info.replace(":","+")

```

# Exercise 8:
**Explain why the code below prints different values on lines 3 and 4.**

```python
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29
```

The first print uses slicing to return a substring from index 21 to index 35; 'for the fjords' and uses reverse find to find 
the first occurrence of 'f' from right to left. It returns 8 because it finds the f in 'fjords' and returns its index.

The second print function passes rfind the whole string, with the parameters defined to search between indexes 21 and 35. 
It finds the same 'f' in 'fjords' but instead of return the index of its location in a slice, it returns its index in the original 
string.

# Exercise 9:
**Write some code to replace the value 6 in the following nested list with 606:**

```python
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
```

```python
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
```

# Exercise 
**Consider the following nested collection:**

```python
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}
```

**Write one line of code to print the activities that Cocoa enjoys.**

```python
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])
```

# Exercise 11:
**Without running the following code, determine what each line should print.**

```python
print('johnson' in 'Joe Johnson')       # False
print('sen' not in 'Joe Johnson')       # True
print('Joe J' in 'Joe Johnson')         # True
print(5 in range(5))                    # False
print(5 in range(6))                    # True
print(5 not in range(5, 10))            # False
print(0 in range(10, 0, -1))            # False
print(4 in {6, 5, 4, 3, 2, 1})          # True
print({1, 2, 3} in {1, 2, 3})           # False
print({3, 2} in {1, frozenset({2, 3})}) # True
```

# Exercise 12:
**Write some code that determines and prints whether the number 3 appears inside each of these lists:**

```python
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
```
```python
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)
```

# Exercise 13:
**Without running the following code, determine what each print statement should print.**

```python
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)       # True
print('Butter' in cats)             # False
print('Butter' in cats[3])          # True
print('cheddar' in cats)            # False
```


# Exercise 14:
**Assume you have the following sequences:**

```python
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)
```
**Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each 
sequence. Print the final result so you can see all the values, which should look like this:**

```
[('a', 'Alpha', None, 10),
 ('b', 'Bravo', True, 20),
 ('c', 'Charlie', False, 30)]
```

```python
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

my_zip = zip(my_str, my_list, my_tuple, my_range)

print(list(my_zip))
```


# Exercise 15:
**Without running the following code, what values will be printed by line 10?**

```python
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()          # keys = dict_keys(['Cat', 'Dog', 'Bird'])
del pets['Dog']             # keys = dict_keys(['Cat', 'Bird'])
pets['Snake'] = 'Sssss'     # keys = dict_keys(['Cat', 'Bird', 'Snake'])
print(keys)                 # dict_keys(['Cat', 'Bird', 'Snake'])
```
