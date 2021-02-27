from gaus import gaus
from control import control
from X import X
from Y import Y

x = X()
y = Y()
e = 0.00001

answers = gaus(x, y)
if not control(answers, x, y, e):
    print('Решение не удовлетворяет заданной точности')

for i in range(len(answers)):
    print('Переменная ' + str(i + 1) + ' равна ' + str(answers[i]))


