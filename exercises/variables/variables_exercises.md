## Variable Exercises 1 and 2:

| Name         | Status        | Explanation                                            |
|--------------|---------------|--------------------------------------------------------|
| index        | idiomatic     |                                                        |
| CatName      | non-idiomatic | Variables should not be camel case.                    |
| lazy_dog     | idiomatic     |                                                        |
| quick_Fox    | non-idiomatic | Variables should be in snake_case.                     |
| 1stCharacter | illegal       | Variables cannot begin with a number.                  |
| operand2     | idiomatic     |                                                        |
| BIG_NUMBER   | non-idiomatic | SCREAMING_SNAKE_CASE should be reserved for constants. |
| π            | non-idiomatic | Not an ASCII character.                                |

Since variables and functions follow the same naming conventions, the same rules apply to both.

## Variable Exercise 3:

| Constant Name | Status        | Explanation                                  |
|---------------|---------------|----------------------------------------------|
| index         | non-idiomatic | Constants should be in SCREAMING_SNAKE_CASE. |
| CatName       | non-idiomatic | Constants should be in SCREAMING_SNAKE_CASE. |
| snake_case    | non-idiomatic | Constants should be in SCREAMING_SNAKE_CASE. |
| LAZY_DOG3     | idiomatic     |                                              |
| 1ST           | illegal       | Cannot start with a number.                  |
| operand2      | non-idiomatic | Constants should be in SCREAMING_SNAKE_CASE. |
| BIG_NUMBER    | idiomatic     |                                              |
| Π             | non-idiomatic | Not an ASCII character.                      |

## Variable Exercise 4:

| Class Name |    Status     | Explanation                                 |
|------------|---------------|---------------------------------------------|
| index      | non-idiomatic | Classes should be in CamelCase.             |
| CatName    |   idiomatic   |                                             |
| Lazy_Dog   | non-idiomatic | Classes should be in CamelCase.             |
| 1ST        |    illegal    | Cannot start with a number.                 |
| operand2   | non-idiomatic | Classes should be in CamelCase.             |
| BigNumber3 |   idiomatic   |                                             |
| Πi         | non-idiomatic | Not an ASCII character.                     |

Variable Exercise 5 and 6 are in the _greeter.py_ and _age.py_ files respectively.

## Variable Exercise 7:
 What happens when you run the following code? Why?
``` python
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)
```

The code will print the following:

    Good Morning, Victor
    Good Afternoon, Victor
    Good Evening, Victor
    Good Morning, Nina
    Good Afternoon, Nina
    Good Evening, Nina
    

Exercises 8 and 9 are in the _variables_exercises_8.py_ and _variables_exercises_9.py_ files respectively.

## Variable Exercise 10:

Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements 
reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? 
If necessary, you can read the documentation.

```python
obj = 'ABcd'
obj.upper()
obj = obj.lower()
print(len(obj))
obj = list(obj)
obj.pop()
obj[2] = 'X'
obj.sort()
set(obj)
obj = tuple(obj) 
```

Going line by line:
- ```obj = 'ABcd'```obj is reassigned to 'ABcd' in the first line. 
- ```obj.upper()```obj.upper() returns a new string with all characters in uppercase. obj is not reassigned or mutated.
- ```obj = obj.lower()``` obj.lower() returns a new string with all characters in lowercase. obj is reassigned to
the value obj.lower(), meaning it is now 'abcd'.
- ```print(len(obj))``` returns '4', the length of the string 'abcd'. It does not mutate or reassign obj.
- ```obj = list(obj)``` obj is reassigned the value of list(obj), which is ['a', 'b', 'c', 'd'].
- ```obj.pop()``` mutates obj by removing the last element of the list, 'd'.
- ```obj[2] = 'X'``` mutates obj by replacing the third element 'c' with 'X'.
- ```obj.sort()``` mutates obj by sorting the list in place. obj is now ['X', 'a', 'b'].
- ```set(obj)``` returns a set of the elements in obj. It does not mutate or reassign obj.
- ```obj = tuple(obj)``` obj is reassigned to the value of tuple(obj), which is ('X', 'a', 'b').

