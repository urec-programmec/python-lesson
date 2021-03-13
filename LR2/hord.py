import math
from function import function

def hord(interval, err, number):
    middle = interval[0] - function(interval[0], number) / (function(interval[1], number) - function(interval[0], number)) * (interval[1] - interval[0])
    value = function(middle, number)
    count = 1
    while math.fabs(value) > err:
        if value < 0:
            interval[1] = middle
        else:
            interval[0] = middle
        middle = interval[0] - function(interval[0], number) / (function(interval[1], number) - function(interval[0], number)) * (interval[1] - interval[0])
        value = function(middle, number)
        count += 1

    return [middle, count, math.fabs(value)]
