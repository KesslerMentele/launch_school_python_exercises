"""
input: a 2 dimensional array
output: a new 2 dimensional array, with the rows and columns inverted


"""

def transpose(orig_matrix:list)->list:
    transposed_matrix = []
    for idx, row in enumerate(orig_matrix):
        transposed_matrix.append([orig_matrix[in_idx][idx] for in_idx in range(len(row))])
    return transposed_matrix



matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True