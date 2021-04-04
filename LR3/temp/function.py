import math


def function(xy):
    return (2 * xy[0] ** 3 - xy[1] ** 2 - 1) + (xy[0] * (xy[1] ** 3) - xy[1] - 4)

    # return (math.cos(0.4 * xy[1] + xy[0] ** 2) + xy[0] ** 2 + xy[1] ** 2 - 1.6) + (1.5 * xy[0] ** 2 - 0.33 * xy[1] ** 2 - 1)

    # return (math.tan(xy[0] ** 3 + 5) - xy[0] ** 2) + (0.5 * xy[0] ** 2 + 2 * xy[1] ** 2 - 1)



    # return 5 * xy[0] ** 2 + 5 * xy[1] ** 2 - 4 * xy[0] * xy[1] - xy[0] - xy[1]

    # return xy[0] ** 2 - xy[1] ** 2

#
# x = lambda xys: 0.4 * xys[0] ** 2 - 0.2 * xys[0] * xys[1] + 0.2
# y = lambda xys: math.sqrt(xys[0] + 3 * math.log10(xys[0]))
# yakobi = lambda xys: [[0.8 * xys[0] - 0.2 * xys[1], -0.2 * xys[0]], [(3 / (math.log(math.e, 10) * xys[0] + 1)) / (2 * math.sqrt(xys[0] + 3 * math.log10(xys[0]))), 0]]

# x = lambda xys: xys[1] ** 2 + 3 * math.log10(xys[0])
# y = lambda xys: 2 * xys[0] - 5 + 1 / xys[0]
# yakobi = lambda xys: [[0.8 * xys[0] - 0.2 * xys[1], -0.2 * xys[0]], [(3 / (math.log(math.e, 10) * xys[0] + 1)) / (2 * math.sqrt(xys[0] + 3 * math.log10(xys[0]))), 0]]

#
