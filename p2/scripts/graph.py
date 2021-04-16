# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import UnivariateSpline
#
# def oneLine():
#     x, y = [], []
#     for j in [10, 50, 100, 500, 1000, 5000, 10000]:
#         with open(f'time_{j}_{i}_avg.txt', 'r') as fin:
#             x.append(j)
#             y.append(float(fin.read().strip()))
#     return x, y
#
# for i in range(1, 4):
#     x, y = oneLine()
#     plt.plot(x, y, 'ro', ms = 5)
#
# plt.plot(x, y, 'ro', ms = 5)
#
# spl = UnivariateSpline(x, y)
# xs = np.linspace(-3, 3, 1000)
# plt.plot(xs, spl(xs), 'g', lw = 3)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

def takeData(src):
    x, y = [], []
    with open(src, 'r') as fin:
        for line in fin:
            x.append(float(line.split()[0]))
            y.append(float(line.split()[1]))
    return x, y

def createGraph(i, colorPoint, colorLine):
    x, y = takeData(f'data_{i}.txt')
    spl = UnivariateSpline(x, y)

    ax.plot(x, y, colorPoint, ms=5)
    ax.plot(x, spl(x), colorLine, lw=1)

fig, ax = plt.subplots()
createGraph(1, 'yo', 'g')
createGraph(2, 'ro', 'm')
createGraph(3, 'bo', 'k')
ax.legend(['a[i]', 'interpol(a[i])', '*(a + i)', 'interpol(*(a + i))',
           '*pa', 'interpol(*pa)'], loc=0)
plt.xlabel('Количество элементов в массиве')
plt.ylabel('Время, затраченное на обработку массива')
plt.title('Зависимость времени от способа обращения к элементам массива',)
ax.grid(True)
fig.savefig('graph.svg')