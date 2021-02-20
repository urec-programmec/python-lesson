from function import function
import matplotlib.pyplot as plt

# x1 = "Это моя строка и пошли нафиг"
# x2 = [1, 2, 4, 5, 4434534, "xdfsdfsdf", []]

xs = [i / 1000 for i in range(10000)]

ys = []
for i in xs:
    ys.append(function(i))

# ys = [function(i) for i in xs]

# print(xs)
# print(ys)

plt.plot(xs, ys, color='blue', marker='o', linewidth=1, markersize=1.5)
plt.show()

# for i in x2:
# for i in x1:
# for i in range(10, 30, 3):
# for i in range(10, 20):
# for i in range(10):

# while True:
#     if 1 == 1:
#         print("t")
#         break


