from function import *
def kasatel (interval , err):
    if d2function (interval [0]) * d1function (interval[0]) > 0:
        diff = interval [0]
    else:
        diff = interval [1]

    diffNext = diff * (function (diff) / d1function (diff))
    count = 1
    while math.fabs (diffNext - diff) > err:
        diff = diffNext
        diffNext = diff - (function (diff) / d1function (diff))
        count += 1
    return [diffNext , count , math.fabs (diffNext - diff)]