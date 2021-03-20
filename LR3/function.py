import math
def function(xy):
    return (math.cos(0.4 * xy[1] + xy[0] ** 2) + xy[0] ** 2 + xy[1] ** 2 - 1.6) + \
        (1.5 * xy[0] ** 2 - 0.33 * xy[1] ** 2 - 1)

def func1(xy):
    return (math.cos(0.4 * xy[1] + xy[0] ** 2) + xy[0] ** 2 + xy[1] ** 2 - 1.6)

def func2(xy):
    return (1.5 * xy[0] ** 2 - 0.33 * xy[1] ** 2 - 1)
