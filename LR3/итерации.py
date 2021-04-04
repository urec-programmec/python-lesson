import math

xyz = [0, 0, 0]
e = 0.0001

x = lambda xyz: -1 * xyz[0] ** 2 + 2 * xyz[1] * xyz[2] + 0.1
y = lambda xyz: xyz[1] ** 2 - 3 * xyz[0] * xyz[2] - 0.2
z = lambda xyz: -1 * xyz[2] ** 2 - 2 * xyz[0] * xyz[1] + 0.3
yakobi = lambda xyz: [
    [-2 * xyz[0], 2 * xyz[2], 2 * xyz[1]],
    [-3 * xyz[2], 2 * xyz[1], -3 * xyz[0]],
    [-2 * xyz[1], -2 * xyz[0], -2 * xyz[2]]]

if abs(yakobi(xyz)[0][0]) + abs(yakobi(xyz)[1][0]) + abs(yakobi(xyz)[2][0]) < 1 and \
    abs(yakobi(xyz)[0][1]) + abs(yakobi(xyz)[1][1]) + abs(yakobi(xyz)[2][1]) < 1 and \
    abs(yakobi(xyz)[0][2]) + abs(yakobi(xyz)[1][2]) + abs(yakobi(xyz)[2][2]) < 1:

    newX = x(xyz)
    newY = y(xyz)
    newZ = z(xyz)

    while abs(xyz[0] - newX) > e and abs(xyz[1] - newY) > e and abs(xyz[2] - newZ) > e:
        xyz[0] = newX
        xyz[1] = newY
        xyz[2] = newZ
        newX = x(xyz)
        newY = y(xyz)
        newZ = z(xyz)

    xyz[0] = newX
    xyz[1] = newY
    xyz[2] = newZ

    print("Решение системы уравнений:\nX = ", newX, "\nY = ", newY, "\nZ = ", newZ)
    print("Отклонение от ответа: ", abs(x(xyz) + y(xyz) + z(xyz) - sum(xyz)))
else:
    print("Решение системы уравнений не сходится при решении методом итераций")



