def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

get_matrix(2,2,10)
get_matrix(3,5,42)
get_matrix(4,2,13)


# n = int(input('Количество строк: '))
# m = int(input('Количество столбцов: '))
# value = int(input('Значение матрицы: '))
#
# get_matrix(n, m, value)
