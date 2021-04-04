from function import *

def kasatel(interval, err, number):
    if d2function(interval[0], number) * d1function(interval[0], number) > 0:
        diff = interval[0]
    else:
        diff = interval[1]

    diffNext = diff - (function(diff, number) / d1function(diff, number))
    count = 1
    while math.fabs(diffNext - diff) > err:
        diff = diffNext
        diffNext = diff - (function(diff, number) / d1function(diff, number))
        count += 1


    return [diffNext, count, math.fabs(diffNext - diff)]

