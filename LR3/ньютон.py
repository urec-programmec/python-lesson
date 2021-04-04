import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def func1(xy):
    return 2 * xy[0] ** 3 - xy[1] ** 2 - 1


def func2(xy):
    return xy[0] * xy[1] ** 3 - xy[1] - 4

x0 = [[0.24], [0.72]]
maxx = 10
maxy = func1([maxx, maxx]) + func2([maxx, maxx]) / 2
interval = [-1 * maxx, maxx]


f1 = func1([x0[0][0], x0[1][0]])
f2 = func2([x0[0][0], x0[1][0]])

f0 = np.array([[f1], [f2]])
M = np.array([[6 * x0[0][0] ** 2, -2 * x0[1][0]], [x0[1][0] ** 3, 3 * x0[0][0] * x0[1][0] ** 2 - 1]])
w2 = np.linalg.det(M)
x = x0 - np.linalg.inv(M).dot(f0)
E = 0.0001

while (abs(x[0][0]-x0[0][0]) > E) and abs(x[1][0]-x0[1][0]) > E:
    x0[0][0] = x[0][0]
    x0[1][0] = x[1][0]
    f1 = func1([x0[0][0], x0[1][0]])
    f2 = func2([x0[0][0], x0[1][0]])
    f0 = np.array([[f1], [f2]])
    M = np.array([[6 * x0[0][0] ** 2, -2 * x0[1][0]], [x0[1][0] ** 3, 3 * x0[0][0] * x0[1][0] ** 2 - 1]])
    w2 = np.linalg.det(M)
    x = x0 - np.linalg.inv(M).dot(f0)

print("Ответ:\nX =", x[0][0], "\nY =", x[1][0])
print("Значения функций:\nFunc 1:", func1(x)[0], "\nFunc 2:", func2(x)[0])

xx = x[0]
yy = x[1]


fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')

xs = np.linspace(interval[0], interval[1], 200)
ys = np.linspace(interval[0], interval[1], 200)

x, y = np.meshgrid(xs, ys)

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
    alpha=0.5
)

ax.scatter(xx, yy, func1([xx, yy]) + func2([xx, yy]), color='red', s=20, zorder=3)
plt.title("Красным выделена точка нуля функции (" + str(xx[0]) + str(", ") + str(yy[0]) + ", " + str(func1([xx, yy])[0] + func2([xx, yy])[0]) + ")")

plt.show()
