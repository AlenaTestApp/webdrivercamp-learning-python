#!/usr/bin/python3
def compute_matrix(mtx):
    modified_matrix = []
    for i in mtx:
        res = map(lambda x: x**2, i)
        modified_matrix.append(list(res))
    return modified_matrix


matrix = [[9, 8, 7],[6, 5, 4],[3, 2, 1]
        ]
print(f"Original: {matrix}")
print(f"Modified: {compute_matrix(matrix)}")
