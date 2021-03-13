import matplotlib.pyplot as plt
from function import function
from half import half
from hord import hord
from kasatel import kasatel

number = 4


def xprint(array):
    for i in range(len(array)):
        print("X" + str(i) + ": " + str(array[i][0]) + " " * (max([len(str(array[k][0])) for k in range(len(array))]) - len(str(array[i][0]))) +
              "\t|\tCount of iterations: " + str(array[i][1]) + " " * (max([len(str(array[k][1])) for k in range(len(array))]) - len(str(array[i][1]))) +
              "\t|\tDifference from 0: " + str(array[i][2]))
    print("\n")


a = -10
b = 10
h = 0.1
e = 0.0001
prev = function(a, number)
current = 1
intervals = []
answersKasatel = []
answersHord = []
answersHalf = []

for i in range(int(a * (1 / h) + 1), int(b * (1 / h) + 1)):
    current = function(i * h, number)
    if current * prev <= 0:
        intervals.append([(i * h if function(i * h, number) <= 0 else (i - 1) * h), ((i - 1) * h if function(i * h, number) <= 0 else (i * h))])
    prev = current


for i in range(len(intervals)):
    answersHalf.append(half(intervals[i], e, number))

for i in range(len(intervals)):
    answersHord.append(hord(intervals[i], e, number))

for i in range(len(intervals)):
    answersKasatel.append(kasatel(intervals[i], e, number))


print("Метод половинного деления")
xprint(answersHalf)

print("Метод хорд")
xprint(answersHord)

print("Метод касательных")
xprint(answersKasatel)

area = 2000

xs = [i / 100.0 for i in range(-1 * area, area)]
ys = [function(xs[i], number) for i in range(len(xs))]

x0 = [xs[i] for i in range(len(xs))]
y0 = [0 for i in range(len(xs))]

plt.plot(xs, ys, color="green", linewidth=2)
plt.plot(x0, y0, color="black", linewidth=1)

plt.show()
