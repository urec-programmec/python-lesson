from function import function
from gold import gold
from math import fabs
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

xystart = [1, 1]
xystart1 = [1, 1]
interval = [-100, 100]
err = 0.001
count = 0
max_count = 100
lam = 0.1


prev_func = function(xystart) + err + 1
while fabs(function(xystart) - prev_func) > err:
    prev_func = function(xystart)
    count += 1
    for i in range(len(xystart)):
        xystart[i] = 'x'
        xystart[i] = gold(xystart, interval, err)


print("Покоординатный спуск:")
print("Полученное значение минимума:")
print(xystart)

print("Значение функции в точке минимума:")
print(function(xystart))

print("Количество итераций:")
print(count)


fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')

xval = np.linspace(interval[0], interval[1], 100)
yval = np.linspace(interval[0], interval[1], 100)
x, y = np.meshgrid(xval, yval)

z = []
for i in range(len(x)):
    z.append([])
    for j in range(len(x[i])):
        z[i].append(function([x[i][j], y[i][j]]))

z = np.array(z)

surf = ax.plot_surface(
# отмечаем аргументы и уравнение поверхности
x, y, z,
# шаг прорисовки сетки
# - чем меньше значение, тем плавнее
# - будет градиент на поверхности
rstride = 2,
cstride = 2,
# цветовая схема plasma
cmap = cm.magma,
zorder=1,
alpha = 1)


ax.scatter(xystart[0], xystart[1], function(xystart), color='red', s=20, zorder=3)

plt.show()

