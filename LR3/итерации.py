# первичные значения решения системы
xyz = [0, 0, 0]
# уровень точности
e = 0.0001

# первое уравнение системы
x = lambda xyz: -1 * xyz[0] ** 2 + 2 * xyz[1] * xyz[2] + 0.1
# второе уравнение системы
y = lambda xyz: xyz[1] ** 2 - 3 * xyz[0] * xyz[2] - 0.2
# третье уравнение системы
z = lambda xyz: -1 * xyz[2] ** 2 - 2 * xyz[0] * xyz[1] + 0.3

# матрица Якоби
yakobi = lambda xyz: [
    [-2 * xyz[0], 2 * xyz[2], 2 * xyz[1]],
    [-3 * xyz[2], 2 * xyz[1], -3 * xyz[0]],
    [-2 * xyz[1], -2 * xyz[0], -2 * xyz[2]]]

# проверка сходимости метода
if abs(yakobi(xyz)[0][0]) + abs(yakobi(xyz)[1][0]) + abs(yakobi(xyz)[2][0]) < 1 and \
    abs(yakobi(xyz)[0][1]) + abs(yakobi(xyz)[1][1]) + abs(yakobi(xyz)[2][1]) < 1 and \
    abs(yakobi(xyz)[0][2]) + abs(yakobi(xyz)[1][2]) + abs(yakobi(xyz)[2][2]) < 1:

    # вычисление Xk+1, Yk+1, Zk+1
    newX = x(xyz)
    newY = y(xyz)
    newZ = z(xyz)

    # итерационный цикл решения до необходимого уровня точности
    while abs(xyz[0] - newX) > e and abs(xyz[1] - newY) > e and abs(xyz[2] - newZ) > e:
        xyz[0] = newX
        xyz[1] = newY
        xyz[2] = newZ
        newX = x(xyz)
        newY = y(xyz)
        newZ = z(xyz)

    # сохранение последнего найденного решения системы
    xyz[0] = newX
    xyz[1] = newY
    xyz[2] = newZ

    print("Решение системы уравнений:\nX = ", newX, "\nY = ", newY, "\nZ = ", newZ)
    print("Отклонение от ответа: ", abs(x(xyz) + y(xyz) + z(xyz) - sum(xyz)))
else:
    print("Решение системы уравнений не сходится при решении методом итераций")

