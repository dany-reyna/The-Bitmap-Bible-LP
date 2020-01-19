from lib.matrix import create_matrix, show_matrix


def rotate(matrix):
    if len(matrix) == 0:
        return

    n = len(matrix)

    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]

            # top = left
            matrix[first][i] = matrix[last - offset][first]

            # left = bottom
            matrix[last - offset][first] = matrix[last][last - offset]

            # bottom = right
            matrix[last][last - offset] = matrix[i][last]

            # right = top
            matrix[i][last] = top


if __name__ == '__main__':
    mat = create_matrix(4, sequential=True)
    show_matrix(mat)
    print('---')
    rotate(mat)
    show_matrix(mat)
