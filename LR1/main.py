import matplotlib.pyplot as plt
from function import function
from slay import slay

xs = [1, 2, 3, 4, 5]


# ys = [15, 10, 15, 20, 25]
# ys = [function(i) for i in range(len(xs))]

x = [[1, -2], [10, 50]]
y = [[77], [88]]

print(slay(x, y, 0.001))



# plt.plot(xs, ys, color='blue', marker='x', linewidth=2.8, markersize=1.5)
# plt.show()
