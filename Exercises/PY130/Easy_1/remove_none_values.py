orig_list = [None, 2, 4, 5, None, 6, None, None]

new_list = list(filter(lambda x: x is not None, orig_list))
print(new_list)