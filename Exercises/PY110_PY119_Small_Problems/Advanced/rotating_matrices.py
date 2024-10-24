"""

new matrix is:

2,0  1,0  0,0
2,1  1,1  0,1
2,2  1,2  0,2


so length of row == new col count
and length of martix == new row count


iterate through range(len(matrix), -1, -1) (length to zero stepping backwards)




"""


def rotate90(orig_matrix:list)->list:
    t_matrix = []
    for in_idx in range(len(orig_matrix[0])):
        t_matrix.append([orig_matrix[out_idx][in_idx]
                         for out_idx in range(len(orig_matrix) - 1 , -1, -1)])
    return t_matrix


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)