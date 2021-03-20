from function import function
from hord import hord
import matplotlib.pyplot as plt

a = 1
b = 2
h = 0.01
intervals = []
answers = []
answershalf = []
answershord = []
answerskas = []
e = 0.0001

def xprint(array):
    for i in range(len(array)):
        print("x" + str(i) + " = " + str(array[i][0])
              + "\t | \t Количество итераций = " + str(array[i][1])
              + "\t | \t Отклонение от 0 = " + str(array[i][2]))
    print("\n")



for i in range(int(a / h + 1), int(b / h + 1), 1):
    if function((i - 1) * h) * function(i * h) < 0:
        if function((i - 1) * h) < function(i * h):
            intervals.append([(i - 1) * h, i * h])
        else:
            intervals.append([i * h, (i - 1) * h])

    elif function(i * h) == 0:
        answers.append(i * h)



intervalhord = [intervals[i] for i in range(len(intervals))]



for i in range(len(intervals)):
    answershord.append(hord(intervalhord[i], e))
print("Метод хорд")
xprint(answershord)



