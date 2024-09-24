# The End Is Near But Not Here

def penultimate(string:str):
    word_list = string.split()
    return word_list[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")