import matplotlib.pyplot as plt
import numpy as np

def takeData(src):
    x, y = [], []
    with open(src, 'r') as fin:
        for line in fin:
            x.append(float(line.split()[0]))
            y.append(float(line.split()[1]))
    return x, y

def createGraph(i, colorPoint, colorLine):
    x, y = takeData(f'data_{i}.txt')

    ax.plot(x, y, colorPoint, ms=5)

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