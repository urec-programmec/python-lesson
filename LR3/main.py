from function import *
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


interval = [-10, 10]
xystart = [1, 1]
e = 0.001

fun0 = np.array([[func1(xystart)], [func2(xystart)]])
M = np.array([[0.2 * xystart[0] + 1, 0.4 * xystart[1]], [0.4 * xystart[0] - 0.1 * xystart[1], 1 - 0.1 * xystart[0]]])

W = np.linalg.det(M)

x = xystart - np.linalg.inv(M).dot(fun0)

 # print(x)


while (abs(x[0][0] - xystart[0]) > e) and (abs(x[1][0] - xystart[1])> e):
xystart[0] = x[0][0]
xystart[1] = x[1][0]



fun0 = np.array([[func1(xystart)], [func2(xystart)]])

M = np.array([[0.2*x0[0][0]+1, 0.4*x0[1][0]], [0.4*x0[0][0]-0.1*x0[1][0],
1-0.1*x0[0][0]]])
#вычисление определителя матрицы Якоби
w2=numpy.linalg.det(M)
#вычисление новых значение х после первой итерации
x = x0 - numpy.linalg.inv(M).dot(f0)
# fig = plt.figure(figsize=(15, 10))
# ax = fig.add_subplot(1, 1, 1, projection='3d')
#
# xs = np.linspace(interval[0], interval[1], 200)
# ys = np.linspace(interval[0], interval[1], 200)
#
# x, y = np.meshgrid(xs, ys)
# z = []
#
# for i in range(len(x)):
#     z.append([])
#     for j in range(len(x[i])):
#         z[i].append(function([x[i][j], y[i][j]]))
#
# z = np.array(z)
#
# vl = ax.plot_surface(
#     x, y, z,
#     rstride=5,
#     cstride=5,
#     cmap=cm.plasma,
#     alpha=1
# )
#
# plt.show()