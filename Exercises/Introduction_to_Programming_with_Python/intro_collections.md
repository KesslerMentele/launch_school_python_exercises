# Exercise 1:
**If you have a list named people, how can you determine the number of entries in that list?**

```python
len(people)
```

# Exercise 2:
**Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?**
```python
stuff = ('hello', 'world', 'bye', 'now')
```

Answer:
```python
stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
```

# Exercise 3:
**Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.**

Lists are mutable, Tuples are not
Lists are created with square brackets, Tuples are created with parentheses
Both are iterable
Both are heterogeneous

# Exercise 4:
**Why can we treat strings as sequences?**

Because they are sufficiently similar to collections. They are iterable and have a length.

# Exercise 5:
**How do the set types differ from the sequence types?**

Sets are unordered. They are not indexed. They do not support things like slicing.
They do not allow duplicates.

# Exercise 6:
**Assuming you have the following assignment:**
```python
pi = 3.141592
```

**Write some code that converts the value of pi to a string and assigns it to a variable named str_pi**

```python
pi = 3.141592
str_pi = str(pi)
```
# Exercise 7:
**Without running the following code, identify the numbers that are included in each of the following ranges:**
```
range(7)
range(1, 6)
range(3, 15, 4)
range(3, 8, -1)
range(8, 3, -1)
```

- `range(7)` -> [0, 1, 2, 3, 4, 5, 6]
- `range(1,6)` -> [1, 2, 3, 4, 5]
- `range(3, 15, 4)` -> [3, 7, 11]
- `range(3, 8, -1)` -> []
- `range(8, 3, -1)` -> [8, 7, 6, 5, 4]

# Exercise 8:
**How would you print all the numbers in the following range?**
```
range(3,17,4
```

```python
for i in range(3, 17, 4):
    print(i)
```

# Exercise 9:
```python
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
```
**Given the above code, answer the following questions and explain your answers:**
1. **Are the lists assigned to my_list and another_list equal?**
    
    Yes, they are equal.

2. **Are the lists assigned to my_list and another_list the same object?**

    No, they are not the same object, the list constructor returns a new object.

3. **Are the nested lists at index 3 of my_list and another_list equal?**

    Yes, they are equal.

4. **Are the nested lists at index 3 of my_list and another_list the same object?**

    Yes, they are the same object.

# Exercise 10:
**Bob expects the following code to print the names in alphabetical order. Without running the code, 
can you say whether it will? Explain your answer.**

```
names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
```

No, the names will not be printed in alphabetical order. This is because `names` is a set, and is therefore unordered.

# Exercise 11:
**Consider the data in the following table:**

| Name      | Country |
|-----------|---------|
| Alice     | USA     |
| Francois  | Canada  |
| Inti      | Peru    |
| Monika    | Germany |
| Sanyu     | Uganda  |
| Yoshitaka | Japan   |

**You need to write some Python code to determine the country name associated with one of the listed names. 
Your code should include the data structure(s) you need and at least one test case to ensure the code works.**

```python
data = {
   'Alice':     'USA',
   'Francois':  'Canada',
   'Inti':      'Peru',
   'Monika':    'Germany',
   'Sanyu':     'Uganda',
   'Yoshitaka': 'Japan',
}

print(data['Sanyu'])
```
