def get_matrix(n = 0, m = 0, value = 0):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tmp = matrix[i][j]
            print(tmp, end = ' ')
        print()

print(get_matrix())

