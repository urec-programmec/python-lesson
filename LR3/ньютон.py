import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


# первое уравнение системы
def func1(xy):
    return 2 * xy[0] ** 3 - xy[1] ** 2 - 1


# второе уравнение системы
def func2(xy):
    return xy[0] * xy[1] ** 3 - xy[1] - 4


# первичные значения решения системы
x0 = [[0.24], [0.72]]

# ограничение X и Y по модулю
maxx = 10

# интервал возможных значений X и Y
interval = [-1 * maxx, maxx]

# первичное решение
f1 = func1([x0[0][0], x0[1][0]])
f2 = func2([x0[0][0], x0[1][0]])

# преобразование системы в массив
f0 = np.array([[f1], [f2]])

# вычисление матрицы Якоби
M = np.array([[6 * x0[0][0] ** 2, -2 * x0[1][0]], [x0[1][0] ** 3, 3 * x0[0][0] * x0[1][0] ** 2 - 1]])

# коррекция значений X и Y
w2 = np.linalg.det(M)
x = x0 - np.linalg.inv(M).dot(f0)

# уровень точности решения
E = 0.0001

# цикл итераций до достижния нужного уровня точности
while (abs(x[0][0]-x0[0][0]) > E) and abs(x[1][0]-x0[1][0]) > E:
    # подмена значений
    x0[0][0] = x[0][0]
    x0[1][0] = x[1][0]

    # вторичные решения
    f1 = func1([x0[0][0], x0[1][0]])
    f2 = func2([x0[0][0], x0[1][0]])

    # преобразование в массив
    f0 = np.array([[f1], [f2]])

    # вычисление матрицы Якоби
    M = np.array([[6 * x0[0][0] ** 2, -2 * x0[1][0]], [x0[1][0] ** 3, 3 * x0[0][0] * x0[1][0] ** 2 - 1]])

    # коррекция значений X и Y
    w2 = np.linalg.det(M)
    x = x0 - np.linalg.inv(M).dot(f0)

# сохранение результата
xx = x[0]
yy = x[1]

# вывод результата
print("Ответ:\nX =", x[0][0], "\nY =", x[1][0])
print("Значения функций:\nFunc 1:", func1(x)[0], "\nFunc 2:", func2(x)[0])

# отрисовка результата
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
xs = np.linspace(interval[0], interval[1], 200)
ys = np.linspace(interval[0], interval[1], 200)
x, y = np.meshgrid(xs, ys)

# заполнение массива значениями функции
z = []
for i in range(len(x)):
    z.append([])
    for j in range(len(x[i])):
        z[i].append(func1([x[i][j], y[i][j]]) + func2([x[i][j], y[i][j]]))

z = np.array(z)
su = ax.plot_surface(
    x, y, z,
    rstride=5,
    cstride=5,
    cmap=cm.plasma,
    alpha=0.5)

# отметка точки решения
ax.scatter(xx, yy, func1([xx, yy]) + func2([xx, yy]), color='red', s=20, zorder=3)
plt.title("Красным выделена точка нуля функции (" + str(xx[0]) + str(", ") + str(yy[0]) + ", " + str(func1([xx, yy])[0] + func2([xx, yy])[0]) + ")")

plt.show()
