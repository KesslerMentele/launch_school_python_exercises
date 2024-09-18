# Exercise 1:
**In your own words, explain the difference between these two expressions.**
```
my_object1 == my_object2
my_object1 is my_object2
```

The first expression checks if the objects have an equivalent value
The second expression checks if they are the same object

# Exercise 2:
**Without running this code, what will it print? Why?**

```python
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)
```

{42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}

# Exercise 3:
**Without running this code, what will it print? Why?**

```python
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])
```
'The Life of Brian'


# Exercise 4:
**Without running this code, what will it print? Why?**

```python
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])
```
[1, 42, 3]


# Exercise 5:
**Write some code to create a deep copy of the dict1 object and assign it to dict2. 
You should only modify the code where indicated.**

```python
import copy# You may modify this line

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

```


# Exercise 6:
**The following program is nearly identical to that of the previous exercise. 
However, this time, it should create a shallow copy of dict1. 
Be careful: you're not allowed to use the copy module in this exercise.`**

**In addition, before you run this code, can you predict the output values?**

```python
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
```
