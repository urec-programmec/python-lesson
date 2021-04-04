from math import sqrt, fabs
from function import function

def gold(xy, int, e):
    interval = int.copy()

    new_e = interval[1] - interval[0]
    # prev =

    while fabs(new_e) > e:
        a = interval[0]
        b = interval[1]
        d = ((sqrt(5) + 1) / 2 - 1)
        delta = (b - a) * d
        x2 = a + delta
        x1 = b - delta

        xy1 = xy.copy()
        xy1[xy.index("x")] = x1

        xy2 = xy.copy()
        xy2[xy.index("x")] = x2

        if function(xy2) == function(xy1):
            xy2[xy.index("x")] += e

        f_x1 = function(xy1)
        f_x2 = function(xy2)

        if f_x1 > f_x2:
            interval[0] = x1
            interval[1] = b

        elif f_x1 < f_x2:
            interval[0] = a
            interval[1] = x2

        else:
            interval[0] = min(x1, x2)
            interval[1] = max(x1, x2)

        new_e = interval[1] - interval[0]

    return (interval[1] + interval[0]) / 2
