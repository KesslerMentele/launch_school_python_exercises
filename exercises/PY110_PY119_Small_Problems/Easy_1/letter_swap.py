# Letter Swap

def swap(string):
    words = string.split()
    swapped = []
    for word in words:
        if len(word) > 1:
            slice_middle = word[1:-1]
            slice_end = word[-1:]
            slice_begin = word[0]
            new_order = ''.join([slice_end, slice_middle, slice_begin])
            swapped.append(new_order)
        else:
            swapped.append(word)
    return ' '.join(swapped)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

