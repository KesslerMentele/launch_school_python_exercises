"""
The output string and the input are the same variable, so it is concatenating the whole forward string onto the end of
the output. to fix this we simply have the returned string be a new variable


"""

def reverse_string(string):
    result = ''
    for char in string:
        result = char + result

    return result

print(reverse_string("hello") == "olleh")