#!/usr/bin/env python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(mtx):

    for row in matrix:
        for el in row:
            print(el, end = ' ')
        print()

print_matrix(matrix)
