from functools import reduce

orig_list = [1,2,3,4,5,6]


product = reduce(lambda x, y: y * x, orig_list )
print(product)