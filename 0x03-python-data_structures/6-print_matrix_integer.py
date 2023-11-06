#!/usr/bin/pyhton3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(numbers)for numbers in row))
