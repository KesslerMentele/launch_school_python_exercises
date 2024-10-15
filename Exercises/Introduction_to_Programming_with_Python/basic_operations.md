## Basic Operations Exercise 1:

Concatenate two strings, one with your first name and one with your last,
to create a new string with your full name as its value.
For example, if your name is John Doe,
you should combine 'John' and 'Doe' to get 'John Doe'.

```python
first_name = 'Kessler'
last_name =  'Mentele'
print(first_name + " " + last_name + '\n')
```

## Basic Operations Exercise 2:

Use the REPL and the arithmetic operators to extract the individual digits of 4936:
 One place is 6.
 Tens place is 3.
 Hundreds place is 9.
 Thousands place is 4.
 Each digit may require multiple Python statements.
```
number = 4936
>>> num = 4936
>>> ones = 4936 % 10
>>> tens = (4936 // 10) % 10
>>> hundreds = (4936 // 100) % 10
>>> thousands = (4936 // 1000) % 10
>>> num
4936
>>> ones
6
>>> tens
3
>>> hundreds
9
>>> thousands
4
```
## Basic Operations Exercise 3 and 4:

```python
print('5' + '10')
```

The above line prints '510' because both values are stings,it uses string concatenation to append them together

```python
print(int('5') + int('10'))
```

The above is the corrected version.

## Basic Operations Exercise 5:

 Will an error occur if you try to access a list element with an index greater than or equal to the list's length? 
 
For example:
```python
foo = ['a', 'b', 'c']
print(foo[3])
```
Will this result in an error?

Yes, the given example will raise an error, because you cant access an index that is out of range.

## Basic Operations Exercise 6:

 To what value does the following expression evaluate?
```python 
'foo' == 'Foo'
```

The expression "'foo' == 'Foo'" evaluates to False because the strings are not equal, as capitalization matters.

## Basic Operations Exercise 7:

What will the following code do? Why?
```python
int('3.1415')
```
The above code will raise an error, as '3.1415' is not a valid integer

## Basic Operations Exercise 8:

To what value does the following expression evaluate?
```python
'12' < '9'
```
The expression will evaluate to true, because it will compare the two values as strings, and 1 is less than 9. 

