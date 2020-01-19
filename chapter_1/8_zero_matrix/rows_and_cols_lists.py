from lib.matrix import create_matrix, show_matrix


def zero_rows(matrix, rows):
    for r in rows:
        matrix[r] = [0] * len(matrix[0])


def zero_cols(matrix, cols):
    for c in cols:
        for row in matrix:
            row[c] = 0


def set_zeros(matrix):
    rows = set()
    columns = set()

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                rows.add(i)
                columns.add(j)

    zero_rows(matrix, rows)
    zero_cols(matrix, columns)


if __name__ == '__main__':
    mat = create_matrix(4, 5, random=True)
    show_matrix(mat)
    print('---')
    set_zeros(mat)
    show_matrix(mat)
