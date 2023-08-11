import random


class Matrix:
    """Class matrix"""
    def __init__(self, matrix):
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")

        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix

        return False

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения размеры матриц должны совпадать")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)


if __name__ == "__main__":
    m1 = Matrix([[random.randint(1, 11) for j in range(5)] for i in range(5)])
    m2 = Matrix([[random.randint(1, 11) for j in range(5)] for i in range(5)])

    print(m1)
    print()
    print(m2)
    print()

    print(m1 + m2)
    print()

    print(m1 * m2)

    print(m1 == m2)

    print(Matrix.__doc__)

    print(m1.__doc__)
