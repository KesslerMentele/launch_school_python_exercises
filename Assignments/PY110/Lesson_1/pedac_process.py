

def change_me(original_string:str)->str:
    if not original_string:
        return ''
    words = original_string.split()
    for index,word in enumerate(words):
        if word == word[::-1]:
            words[index] = word.upper()
    return ' '.join(words)

#print(change_me("We will meet at noon") )      # "We will meet at NOON"
#print(change_me("No palindromes here"))       # "No palindromes here"
#print(change_me(""))                          # ""
#print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"



'''
input: string
output: list
rules:
    - Every palindromic substring must be included, including overlapping
    - Palindromes are case-sensitive

Algorithm:
    - Create a result list
    - Create a list of every substring >= 2 characters **Hardest part**
        - **Write get_substrings(string) Function** 
    - Iterate through the list of substrings
        - For each palindromic substring, add it to the result list
    - Return the result list

get_substrings Algorithm:
    - create result list
    - loop through 0 to length(string) - 1 (call it index_begin)
        - loop through index_begin + 2 to to length(string) (call it index_end)
            - add string[index_begin:index_end] to result list

'''

def get_substrings(s:str)->[str]:
    result = []
    index_begin = 0
    while index_begin < len(s) :
        index_end = index_begin + 2
        while index_end <= len(s):
            result.append(s[index_begin:index_end])
            index_end += 1
        index_begin += 1
    return result




def is_palindrome(s:str)->bool:
    if s == s[::-1]:
        return True
    return False


def palindrome_substrings(s:str)->[str]:
    if not s:
        return []
    result = []
    substrings_list = get_substrings(s)
    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)
    return result

print(palindrome_substrings("abcddcbA"))                            # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome"))                          # []
print(palindrome_substrings(""))                                    # []
print(palindrome_substrings("repaper"))                             # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious"))  # ["ili"]

