"""
input: a 2-dimensional array
output: a new 2-dimensional array, with the rows and columns inverted


"""

def transpose(orig_matrix:list)->list:
    t_matrix = []
    for idx in range(len(orig_matrix[0])):
        t_matrix.append([orig_matrix[out_idx][idx]
                                  for out_idx in range(len(orig_matrix))])
    return t_matrix




# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)