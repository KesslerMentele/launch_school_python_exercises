from functools import reduce

orig_list = ['a','b','c']
new_string = reduce(lambda x,y: x + y, orig_list)
print(new_string)