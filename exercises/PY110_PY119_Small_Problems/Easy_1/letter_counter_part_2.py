# Letter Counter (Part 2)

def word_sizes(string):
    words = string.split()
    counts = {}
    for word in words:
        stripped_string = ''
        for char in word:
            stripped_string += char.lower() if char.isalnum() else ''
        length =len(stripped_string)
        if counts.get(length) :
            counts[length] += 1
        else:
            counts[length] = 1
    return counts

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})