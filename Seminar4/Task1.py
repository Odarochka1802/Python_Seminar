# 1. Напишите функцию для транспонирования матрицы
from pprint import pprint
from random import randint

n = 4
matrix = [[randint(1, 10) for j in range(n)] for i in range(n)]
print(f"Our first matrix: {matrix}")
for row in matrix:
    print(*row, sep=', ')


def transpose_matrix(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def transpose_with_zip(matrix):
    return [list(row) for row in zip(*matrix)]


def transpose_with_list_generator(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


print(f'Our new matrix: {transpose_matrix(matrix)}')
for row in transpose_matrix(matrix):
    print(*row, sep=', ')
print(f'Our new matrix with method ZIP: {transpose_with_zip(matrix)}')
for row in transpose_with_zip(matrix):
    print(*row, sep=', ')
print(f'Our new matrix with list generation: {transpose_with_list_generator(matrix)}')
for row in transpose_with_list_generator(matrix):
    print(*row, sep=', ')
