from function import function
import math
def hord(interval, err):
    middle = interval[0] - function(interval[0]) / (function(interval[1]) - function(interval[0])) * (interval[1] - interval[0])
    value = function(middle)
    count = 1



    while math.fabs(value) > err:
        if value < 0:
            interval[1] = middle
        else:
            interval[0] = middle

        middle = interval[0] - function(interval[0]) / (function(interval[1]) - function(interval[0])) * (
                    interval[1] - interval[0])
        value = function(middle)
        count += 1

    return[middle, count, value]
