
### A function that returns the sum of two numbers:

```pseudocode
START

GET number_1
GET number_2

SET output = int(number_1) + int(number_2)

PRINT output

END
```

### A function that takes a list of strings, and returns a string that is all those strings concatenated together:

```pseudocode
START

# given a list of strings called 'strings'

SET output = ''

FOR string IN strings
    SET output += string

PRINT output

END
```



### A function that takes a list of integers, and returns a new list with every other element from the original list,starting with the first element. 
**For instance:**

```
every_other([1,4,7,2,5]) # => [1,7,5]
```

```pseudocode
START

# Given a list of integers called 'numbers'
SET output = []

FOR number IN numbers, stepping through 2 at a time
    SET output to include number

PRINT output

END
```




### A function that determines the index of the 3rd occurrence of a given character in a string. 
**For instance, if the given character is `'x'` and the string is `'axbxcdxex'`, the function should return 6 (the index of the 3rd `'x'`). 
If the given character does not occur at least 3 times, return `None`.**

```pseudocode
START

# Given a string called 'string_to_search'
# Given a single character string to search for called 'item'

SET index = 0
SET count = 0

WHILE index <= length of string_to_search
    IF string_to_search at index is item
        SET count += 1
    IF count == 3
        PRINT index and break the loop
    SET index += 1
IF count < 3
    PRINT None

END
```

### A function that takes two lists of numbers and returns the result of merging the lists. 
**The elements of the first list should become the elements at the even indexes of the returned list, while the elements 
of the second list should become the elements at the odd indexes. For instance:**

```
merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
```
**You may assume that both list arguments have the same number of elements.**

```pseudocode
START

# Given two lists, 'list_1' and 'list_2'

SET output_list = []

SET index = 0
WHILE index in list_1
    SET output_list to include list_1 at index and then list_2 at index
    SET index += 1

PRINT output_list

END
```

### A function that takes a list of strings, and determines the minimum number of characters required to uniquely identify each string

```pseudocode
START

# Given a list of strings 'strings'

SET identifiers = []
SET index = 0

WHILE index in len(strings)
    SET char_index = 0
    SET identifier = ''
    
    WHILE char_index in len(strings[index])
    
        indetifier += strings[index][char_index]
        
        IF strings[index][char_index] NOT IN IDENTIFIERS
            SET identifiers[index] = identifier
            break
            
        SET char_index += 1
    SET index += 1

PRINT identifiers

END
```