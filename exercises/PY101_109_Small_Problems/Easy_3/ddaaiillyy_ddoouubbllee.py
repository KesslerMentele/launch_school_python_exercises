# ddaaiillyy ddoouubbllee

def crunch(string):
    stretch = list(string)
    squish = ''
    last_letter = ''
    for letter in stretch:
        if letter != last_letter:
            squish = squish + letter
        last_letter = letter
    return squish

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')