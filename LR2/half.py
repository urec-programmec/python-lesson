import  math
from function import function


def half(interval , err):
    middle = (interval[0] + interval [1]) / 2
    value = function (middle)
    count = 1

    while math.fabs (value) > err:
        if value < 0:
            interval [0] = middle
        else:
            interval [1] = middle

        middle = (interval[0] + interval [1]) / 2
        value = function (middle)
        count += 1

    return [middle , count , value]