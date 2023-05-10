from typing import List, Tuple, Any

MIN = 1.0e-18


def get_matrix_size(matrix: List[List[float]]) -> Tuple[int, int]:
    return len(matrix), len(matrix[0])


def zero_matrix(rows: int, cols: int) -> list[list[float]]:
    assert isinstance(rows, int) and isinstance(cols, int)
    return [[.0] * cols for _ in range(rows)]


def transpose(matrix: List[List[float] | float]) -> List[List[float]]:
    if not isinstance(matrix[0], list):
        matrix = [matrix]

    rows, cols = get_matrix_size(matrix)

    result = zero_matrix(cols, rows)
    for row in range(rows):
        for col in range(cols):
            result[col][row] = matrix[row][col]

    return result


def matrix_addition(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    rows_a, cols_a = get_matrix_size(matrix_a)
    rows_b, cols_b = get_matrix_size(matrix_b)

    if rows_a != rows_b or cols_a != cols_b:
        raise ArithmeticError('size of matrices must be same')

    result = zero_matrix(rows_a, cols_b)

    for row in range(rows_a):
        for col in range(cols_b):
            result[row][col] = matrix_a[row][col] + matrix_b[row][col]

    return result


def matrix_multiplication(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    rows_a, cols_a = get_matrix_size(matrix_a)
    rows_b, cols_b = get_matrix_size(matrix_b)

    if cols_a != rows_b:
        raise ArithmeticError('Number of matrix_a columns must equal number of matrix_b rows')

    result = zero_matrix(rows_a, cols_b)

    for row in range(rows_a):
        for col in range(cols_b):
            result[row][col] = sum([matrix_a[row][index] * matrix_b[index][col] for index in range(cols_a)])

    return result


def get_identity_matrix(N: int) -> List[List[float]]:
    result = zero_matrix(N, N)

    for index in range(N):
        result[index][index] = 1.0

    return result


def copy_matrix(matrix: List[List[float]]) -> List[List[float]]:
    rows, cols = get_matrix_size(matrix)
    result = zero_matrix(rows, cols)

    for row in range(rows):
        for col in range(cols):
            result[row][col] = matrix[row][col]

    return result


def determinant(matrix: List[List[float]]) -> float:
    N = len(matrix)

    for main_diag in range(N):
        if not matrix[main_diag][main_diag]:
            matrix[main_diag][main_diag] = MIN

        for i in range(main_diag + 1, N):
            curr_row = matrix[i][main_diag] / matrix[main_diag][main_diag]
            for j in range(N):
                matrix[i][j] -= curr_row * matrix[main_diag][j]

    result = 1.0

    for index in range(N):
        result *= matrix[index][index]

    return result


def matrix_non_singular_checker(matrix: List[List[float]]):
    det = determinant(matrix)

    if det:
        return det
    raise ArithmeticError('matrix must be singular')


def matrix_equality_checker(matrix_a: List[List[float]], matrix_b: List[List[float]], tolerance=None) -> bool:
    rows_a, cols_a = get_matrix_size(matrix_a)
    rows_b, cols_b = get_matrix_size(matrix_b)

    if rows_a != rows_b or cols_a != cols_b:
        raise ArithmeticError('matrix must square matrix')

    for row in range(rows_a):
        for col in range(cols_b):
            if tolerance is None:
                if matrix_a[row][col] != matrix_b[row][col]:
                    return False
            else:
                if round(matrix_a[row][col], tolerance) != round(matrix_b[row][col], tolerance):
                    return False

    return True


def matrix_square_checker(matrix: List[List[float]]) -> bool:
    rows, cols = get_matrix_size(matrix)
    return rows == cols


def insert_at_nth_column_of_matrix(column_vector: List[List[int]] | Any, matrix: List[List[float]], column_num: int):
    rows, cols = get_matrix_size(matrix)

    if not isinstance(column_vector, list):
        column_value = column_vector
        column_vector = [[column_value] for _ in range(rows)]

    if rows != len(column_vector):
        raise ArithmeticError('column and Matrix rows do NOT match.')

    for i in range(rows):
        matrix[i].insert(column_num, column_vector[i][0])

    return matrix


def replace_nth_column_of_matrix(column_vector: List[List[int]] | Any, matrix: List[List[float]], column_num: int):
    rows, cols = get_matrix_size(matrix)

    if not isinstance(column_vector, list):
        column_value = column_vector
        column_vector = [[column_value] for _ in range(rows)]

    if rows != len(column_vector):
        raise ArithmeticError('column and Matrix rows do NOT match.')

    for i in range(rows):
        matrix[i][column_num] = column_vector[i][0]

    return matrix


def equation_solver(matrix_a, matrix_b, tol=None):
    matrix_square_checker(matrix_a)
    matrix_non_singular_checker(matrix_a)

    N = len(matrix_a)
    matrix_AC = copy_matrix(matrix_a)
    matrix_BC = copy_matrix(matrix_b)

    indices = list(range(N))
    for main_diag in range(N):
        if not matrix_AC[main_diag][main_diag]:
            matrix_AC[main_diag][main_diag] = MIN
        fdScaler = 1.0 / matrix_AC[main_diag][main_diag]

        for index in range(N):
            matrix_AC[main_diag][index] *= fdScaler

        matrix_BC[main_diag][0] *= fdScaler

        for i in indices[0:main_diag] + indices[main_diag + 1:]:
            crScaler = matrix_AC[i][main_diag]

            for j in range(N):
                matrix_AC[i][j] = matrix_AC[i][j] - crScaler * matrix_AC[main_diag][j]

            matrix_BC[i][0] = matrix_BC[i][0] - crScaler * matrix_BC[main_diag][0]

    if matrix_equality_checker(matrix_b, matrix_multiplication(matrix_a, matrix_BC), tol):
        return matrix_BC
    else:
        raise ArithmeticError("solution for X out of tolerance.")


def least_squares(matrix_X, matrix_Y, tolerance=3):
    if not isinstance(matrix_X[0], list):
        matrix_X = [matrix_X]
    if not isinstance(type(matrix_Y[0]), list):
        matrix_Y = [matrix_Y]

    rows_X, cols_X = get_matrix_size(matrix_X)
    rows_Y, cols_Y = get_matrix_size(matrix_Y)

    if rows_X < cols_X:
        matrix_X = transpose(matrix_X)
    if rows_Y < cols_Y:
        matrix_Y = transpose(matrix_Y)

    for i in range(len(matrix_X)):
        matrix_X[i].append(1)

    matrix_transpose = transpose(matrix_X)

    return equation_solver(matrix_multiplication(matrix_transpose, matrix_X), matrix_multiplication(matrix_transpose, matrix_Y), tolerance)
