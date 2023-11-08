#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    no_rows = len(matrix)
    no_col = len(matrix[0]) if no_rows > 0 else 0

    matrix_result = [[0] * no_col for _ in range(no_rows)]

    for i in range(no_rows):
        for j in range(no_col):
            matrix_result[i][j] = matrix[i][j] ** 2

    return matrix_result
