import math

def function(x, number):

    if number == 1:
        return x - 3 * math.cos(1.04 * x) ** 2
    elif number == 2:
        return math.sqrt(x) - math.cos(0.387 * x)
    elif number == 3:
        return 1 / x - math.pi * math.cos(math.pi * x)
    elif number == 4:
        return x ** 3 - 4 * x + 2
    elif number == 5:
        return x ** 5 - x - 0.2
    elif number == 6:
        return math.log(x, math.e) - 1 / x
    elif number == 7:
        return 2 * math.log(x, math.e) - x / 2 + 1
    elif number == 8:
        return math.log(x, math.e) - 1 / (x ** 2)
    elif number == 9:
        return math.e ** x + x ** 3 - 2
    elif number == 10:
        return 2 ** x - 2 * x ** 3 - 1


def d1function(x, number):
    h = 1e-5
    return (function(x + h, number) - function(x - h, number)) / (2 * h)


def d2function(x, number):
    h = 1e-5
    return (d1function(x + h, number) - d1function(x - h, number)) / (2 * h)
