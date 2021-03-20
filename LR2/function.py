import math
def function(x):
    return x - 3 * math.cos (1.04 * x) ** 2
def d1function (x):
    h = 1e-5
    return (function (x+h) - function (x-h))/ (2*h)
def d2function (x):
    h = 1e-5
    return (d1function (x+h) - d1function (x-h))/ (2*h)