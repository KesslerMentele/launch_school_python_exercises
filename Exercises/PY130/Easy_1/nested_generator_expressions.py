
orig_list = [[1,2,3],[4,5,6],[7,8,9]]

new_list = list((number for sublist in orig_list for number in sublist))
print(new_list)