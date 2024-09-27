# Hard 1

### Question 1:
**Will the following functions return the same results?**

```
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())
```

**Answer:**

No


---
### Question 2:
**What does the last line in the following code output?**

```
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
```

**Answer:**

```
{'first':[1,2]}
```

---
### Question 3:
**Given the following similar sets of code, what will each code snippet print?**

**A)**
```
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```
**B)**
```
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```
**C)**
```
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

**Answer:**

**A)**
```
one is: ["one"]
two is: ["two"]
three is: ["three"]
```
**B)**
```
one is: ["one"]
two is: ["two"]
three is: ["three"]
```
**C)**
```
one is: ["two"]
two is: ["three"]
three is: ["one"]
```
---
### Question 4:
**Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 
dot-separated numbers, e.g., `10.4.5.11`.**

**Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 
0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:**

```
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True
```

Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false 
condition, and you're not handling the case when the input string has more or less than 4 components, e.g., `4.5.5` or 
`1.2.3.4.5`: both those values should be invalid."

**Help Ben fix his code.**

**Answer:**

```
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True
```

---
### Question 5:
**What do you expect to happen when the greeting variable is referenced in the last line of the code below?**

```
if False:
    greeting = "hello world"

print(greeting)
```

**Answer:**

NameError
