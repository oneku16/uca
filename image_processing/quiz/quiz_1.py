from random import randint
from copy import deepcopy

N, M = 3, 3
LOW, UP = 0, 255
L = 255


def min_matrix(matrix: list[list[float, ...], ...]) -> float:
    min_value = next(iter(next(iter(matrix))))
    for row in matrix:
        min_value = min(min(row), min_value)
    return min_value


def max_matrix(matrix: list[list[float, ...], ...]) -> float:
    max_value = next(iter(next(iter(matrix))))
    for row in matrix:
        max_value = max(max(row), max_value)
    return max_value


def question_1(_matrix: list[list[float, ...], ...]) -> list[list[float, ...], ...]:
    mm = deepcopy(_matrix)
    R_MIN = min_matrix(matrix=mm)
    R_MAX = max_matrix(matrix=mm)

    def T(r):
        return (r - R_MIN) * (L / (R_MAX - R_MIN))

    for i in range(N):
        for j in range(M):
            mm[i][j] = T(mm[i][j])

    return mm


def question_2(_matrix: list[list[float, ...], ...]) -> list[list[float, ...], ...]:
    mm = deepcopy(_matrix)
    R_MIN = min_matrix(matrix=mm)
    R_MAX = max_matrix(matrix=mm)

    def S(r):
        return ((r - R_MIN) / (R_MAX - R_MIN)) * L

    for i in range(N):
        for j in range(M):
            mm[i][j] = S(mm[i][j])

    return mm


def print_matrix(matrix):
    print()
    for row in matrix:
        print(row)

    print()


def main(*args, **kwargs):
    matrix = [[60, 60, 55], [40, 45, 42], [35, 30, 38]]
    # matrix = [[randint(LOW, UP) for _ in range(M)] for _ in range(N)]
    matrix_1 = question_1(matrix)
    matrix_2 = question_2(matrix)
    print_matrix(matrix)
    print_matrix(matrix_1)
    print_matrix(matrix_2)



if __name__ == '__main__':
    main()
