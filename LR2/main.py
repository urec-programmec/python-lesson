from function import  function
from kasatel import kasatel

a = 0
b = 5
h = 0.01
e = 0.0001
intervals = []
answers = []
answersKas = []

def xprint (array):
    for i in range (len (array)):
        print("x" + str(i) + " = " + str(array [i] [0])
              + "\t| \tКоличество интераций = " + str (array[i][1])
              + "\t| \tОтклонений от 0  = " + str(array[i][2]))
    print ("\n")


for i in range (int (a/h + 1) , int (b/h + 1), 1):
    if function((i - 1) * h) * function(i * h) < 0:
        if function((i - 1) * h) < function (i*h):
            intervals.append([(i - 1) * h , i * h])
        else:
            intervals.append([i * h , (i - 1) * h])
    elif function(i * h) == 0:
        answers.append (i * h)

intervalsKas = [intervals[i] for i in range (len (intervals))]
for i in range (len (intervals)):
    answersKas.append (kasatel (intervalsKas [i] , e))

print ("Метод Касательных")
xprint (answersKas)