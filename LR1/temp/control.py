import math

def control(answers, x, y, e):
    size = len(y)

    for i in range(size):
        temp = 0
        for j in range(size):
            temp += x[i][j] * answers[j]
        if math.fabs(y[i] - temp) >= e:
            return False

    return True
