**Problem:**
Given a list of strings, return a new list where the strings are sorted based on the 
highest number of adjacent consonants a string contains. If two strings contain the 
same highest number of adjacent consonants, they should retain their original order 
in relation to each other. Consonants are considered adjacent if they are next to 
each other in the same word or if there is a space between two consonants in adjacent 
words.

**Input:** list of strings

**Output:** New sorted list

Rules:
- Explicit:
  - If two strings contain the same highest count of adjacent consonants, they must be in their original order relative 
    to each other 
  - consonants separated by spaces still count as consecutive
  - Sort descending
  - Strings with no consonants have a count of 0
  - strings with no consecutive consonants have a count of 0
  - Case is irrelevant


Input: \[str\]

Output: \[str\]

**Algorithm:**
- For each string in the input list, get the consonant_adjacency_count

- sort by that count, descending order.
- return the sorted list







