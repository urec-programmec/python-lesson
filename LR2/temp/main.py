from function import function
import matplotlib.pyplot as plt
from half import half
from hord import hord

a = 0
b = 5
h = 0.01
e = 0.0001
intervals = []
answers = []
answersHalf = []
answersHord = []
answersKas = []

def xprint(array):
    for i in range(len(array)):
        print("X" + str(i) + " = " + str(array[i][0])
              + "\t|\tКоличество итераций = " + str(array[i][1])
              + "\t|\tОтклонение от 0 = " + str(array[i][2]))
    print("\n")

for i in range(int(a / h + 1), int(b / h + 1), 1):
    if function((i - 1) * h) * function(i * h) < 0:
        if function((i - 1) * h) < function(i * h):
            intervals.append([(i - 1) * h, i * h])
        else:
            intervals.append([i * h, (i - 1) * h])

    elif function(i * h) == 0:
        answers.append(i * h)


intervalsHalf = [intervals[i] for i in range(len(intervals))]
intervalsHord = [intervals[i] for i in range(len(intervals))]
intervalsKas = [intervals[i] for i in range(len(intervals))]


for i in range(len(intervals)):
    answersHalf.append(half(intervalsHalf[i], e))

print("Метод половинного деления")
xprint(answersHalf)


for i in range(len(intervals)):
    answersHord.append(hord(intervalsHord[i], e))

print("Метод хорд")
xprint(answersHord)




# tochnost = 0.1
#
# xs = [(i * tochnost) for i in range(int(a / tochnost), int(b / tochnost))]
# ys = [function(xs[i]) for i in range(len(xs))]
#
# x0 = [xs[i] for i in range(len(xs))]
# y0 = [0 for i in range(len(xs))]
#
# plt.plot(xs, ys, color="green", linewidth=2)
# plt.plot(x0, y0, color="black", linewidth=1)
# plt.show()

