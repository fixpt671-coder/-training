def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

def get_matrix_2(n, m, value):
    matrix = [[value]*m]*n
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tmp = matrix[i][j]
            print(tmp, end = ' ')
        print()


print_matrix(get_matrix(3, 3, 11))
print()
print_matrix(get_matrix_2(3, 3, 12))

