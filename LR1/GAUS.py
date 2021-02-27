def GAUS (x, y):
    matrix = []
    size = len(y)

    for i in range(size):
        matrix.append ([])
        for j in range(size):
            matrix[-1].append(x[i][j])

        matrix[-1].append(y[i])

    for i in range(size):
        koeff = matrix [i][i]
        for j in range(i, size + 1):
            matrix[i][j] /=koeff

        for ii in range (i + 1, size):
            koeff = matrix [ii][i]
            for j in range(i, size + 1):
                matrix[ii][j] -= matrix[i][j] * koeff

    answer = [0] * size
    answer [-1] = matrix[size -1][size]

    for i in range(size - 2, -1, -1):
        temp = 0
        for j in range(i + 1, size):
            temp += matrix[i][j] * answer[j]

        answer[i] = matrix[i][size] - temp

    # for i in range(size):
    #     temp = 0
    #     for j in range(size):
    #         temp += x[i][j] * answer[j]
    #     print(str(i) + ' строка')
    #     print(temp)
    #     print(y[i])

    return answer
