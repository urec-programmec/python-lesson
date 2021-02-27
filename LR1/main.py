from GAUS import GAUS
from CONTROL import CONTROL
from x1 import X
from y1 import Y

x = X()

y = Y()

e = 0.000001

answers = GAUS(x, y)
if not CONTROL (answers, x, y, e):
    print ('Решения не удовлетворяет заданной точности')


for i in range(len(answers)):
    print ('Переменная ' + str(i + 1) + ' = ' + str(answers [i]))

# print ('X = ' , X)
# print ('Y = ' , Y)
# print ('Z = ' , Z)
