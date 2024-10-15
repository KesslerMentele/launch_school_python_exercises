# Easy 1

### Question 1:
**Will the code below raise an error?**
```
numbers = [1, 2, 3]
numbers[6] = 5
```

**Answer:**
yes

---
### Question 2:
**How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or 
False depending on whether the string ends with an exclamation mark.**

```
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
```
**Answer:**
```
print(str1[-1] == '!')
print(str2[-1] == '!')
```
---
### Question 3:
**Starting with the string:**

```
famous_words = "seven years ago..."
```

**Show two different ways to create a new string with "Four score and " prepended to the front of the string.**

**Answer:**
```
famous_words = "seven years ago..."
new_string = "Four score and " + famous_words
```

or

```
famous_words = "seven years ago..."
new_string = f'Four score and {famous_words}'
```

---
### Question 4:
**Using the following string, print a string that contains the same value, but using all lowercase letters except for 
the first character, which should be capitalized.**

```
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
```

**Answer:**
```
munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.capitalize())
```

---
### Question 5:
**Starting with the string:**

```
munsters_description = "The Munsters are creepy and spooky."
```
**print the string with the case of all letters swapped:**

```
"tHE mUNSTERS ARE CREEPY AND SPOOKY."
```
**Answer:**

```
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())
```

### Question 6:
**Determine whether the name `Dino` appears in the strings below -- check each string separately:**

```
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
```

**Answer:**
```
print('Dino' in str1)
print('Dino' in str2)
```

---
### Question 7:
**How can we add the family pet, `"Dino"`, to the following list?**

```
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
```

**Answer:**
```
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
```
---
### Question 8:
**In the previous problem, our first answer added `'Dino'` to the list like this:**

```
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
```

**How can we add multiple items to our list (e.g., `'Dino'` and `'Hoppy'`)? Replace the call to append with another method 
invocation.**

**Answer:**
```
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(['Dino', 'Hoppy'])
```
---
### Question 9:
**Print a new version of the sentence given by advice that ends just before the word house. Don't worry about spaces or 
punctuation: remove everything starting from the beginning of house to the end of the sentence.**

```
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
```

**Answer:**
```
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.split('house')[0])
```
---
### Question 10:
**Print the following string with the word `important` replaced by `urgent`:**

```
advice = "Few things in life are as important as house training your pet dinosaur."
```

**Answer:**
```
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important", "urgent"))
```


# Easy 2

### Question 1:
**Write two distinct ways of reversing the list without mutating the original list.**

```
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
```

**Answer:**

```
numbers = [1, 2, 3, 4, 5]
reversed_list_1 = numbers[::-1]
reversed_list_2 = list(numbers.reversed())
```

---
### Question 2:
**Given a number and a list, determine whether the number is included in the list.**

```
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
```

**Answer:**

```
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

number1 in numbers
number2 in numbers
```

---
### Question 3:
**Programmatically determine whether `42` lies between `10` and `100`, inclusive. Do the same for the values `100` and 
`101`.**

**Answer:**

```
42 >= 10 and 42 <= 100
100 >= 10 and 100 <= 100
101 >= 10 and 101 <= 100
```
---
### Question 4:
**Given a list of numbers `[1, 2, 3, 4, 5]`, mutate the list by removing the number at index 2, so that the list 
becomes `[1, 2, 4, 5]`.**

**Answer:**

```
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
```
---
### Question 5:
**How would you verify whether the data structures assigned to the variables `numbers` and `table` are of type `list`?**

```
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
```

**Answer:**

```
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
isinstance(numbers, list)
isinstance(table, list)
```

### Question 6:
**Back in the stone age (before CSS), we used spaces to align things on the screen. If we have a 40-character wide table 
of Flintstone family members, how can we center the following title above the table with spaces?**

```
title = "Flintstone Family Members"
```

**Answer:**

```
title = "Flintstone Family Members"
title.center(40)
```
---
### Question 7:
**Write a one-liner to count the number of lower-case `t` characters in each of the following strings:**

```
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
```

**Answer:**
```
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
count = statement1.count('t') + statement2.count('t')
```
---
### Question 8:
**Determine whether the following dictionary of people and their age contains an entry for `'Spot'`:**

```
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
```

**Answer:**

```
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
"Spot" in ages
```
---
### Question 9:
**We have most of the Munster family in our ages dictionary:**

```
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
```

**Add entries for Marilyn and Spot to the dictionary:**

```
additional_ages = {'Marilyn': 22, 'Spot': 237}
```

**Answer:**

```
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
```

# Easy 3



---
### Question 1:
**Write two different ways to remove all of the elements from the following list:**

```
numbers = [1, 2, 3, 4]
```

**Answer:**

```
while numbers:
    numbers.pop(0)
```
and

```
numbers.clear()
```

---
### Question 2:
**What will the following code output?**

```
print([1, 2, 3] + [4, 5])
```

**Answer:**
```
[1,2,3,4,5]
```
---
### Question 3:
**What will the following code output?**

```
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
```

**Answer:**

```
hello there
```


---
### Question 4:
**What will the following code output?**

```
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
```

**Answer:**

```
[{'first':42},{'second': 'value2'},3,4,5]
```
my_list2 is a shallow copy

---
### Question 5:
**The following function unnecessarily uses two `return` statements to return boolean values. Can you rewrite this 
function so it only has one `return` statement and does not explicitly use either `True` or `False`?**

```
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
```

**Answer:**
```
def is_color_valid(color):
    return color == 'blue' or color == 'green'
```