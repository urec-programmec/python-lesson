from function import function
import matplotlib.pyplot as plt
for i in range(10):
    print("i")
xs = [1, 2, 3, 4, 5]
ys = []
for i in xs:
    ys.append(function(i))
print(xs)
print(ys)
plt.plot(xs, ys)
plt.show()