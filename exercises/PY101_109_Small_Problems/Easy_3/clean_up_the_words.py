# Clean up the words

def clean_up(dirty):
    spread = list(dirty)
    clean = ''
    last_char = 'a' # set to an alphanumeric to add the first space
    for char in spread:
        if char.isalnum():
            clean = clean + char
        elif last_char.isalnum():
            clean = clean + ' '
        last_char = char
    return clean

print(clean_up("---what's my +*& line?") == " what s my line ")
# True