from lib.matrix import create_matrix, show_matrix


def zero_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def zero_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


def set_zeros(matrix):
    first_row_has_zero = False
    first_column_has_zero = False

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_column_has_zero = True
            break

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            zero_row(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            zero_column(matrix, j)

    if first_row_has_zero:
        zero_row(matrix, 0)

    if first_column_has_zero:
        zero_column(matrix, 0)


if __name__ == '__main__':
    mat = create_matrix(4, 5, random=True)
    show_matrix(mat)
    print('---')
    set_zeros(mat)
    show_matrix(mat)
