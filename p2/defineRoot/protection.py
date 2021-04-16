import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def function(x):
    return np.sin(x)

def firstDefiv(x):
    return np.cos(x)

class Graph:
    def __init__(self, begin, end, function, xRoot):
        self.__step = (end - begin) / 100
        self.__function = function
        self.__xRoot = xRoot
        self.__yRoot = [function(i) for i in xRoot]
        self.__x = []
        self.__y = []
        self.__generate(begin, end)
        self.__createGraph()
        self.putRoots('bo')

    def __generate(self, begin, end):
        while begin < end:
            self.__x.append(begin)
            self.__y.append(self.__function(begin))
            begin += self.__step

    def __createGraph(self):
        plt.title('График функции F(x) = sin(x)')
        plt.ylabel('F(x)')
        plt.xlabel('x')
        plt.plot(self.__x, self.__y, color='magenta')
        plt.legend(['sin(x)'], loc=0)
        plt.grid(True)
        ax = plt.gca()
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

    def putRoots(self, color):
        plt.plot(self.__xRoot, self.__yRoot, color, linewidth=3)

    def showGraph(self):
        plt.show()

def findRoot(begin, end, step, listRoot):
    while begin < end:
        if firstDefiv(begin) != 0:
            x = begin - function(begin) / firstDefiv(begin)
            if abs(function(x)) < eps and round(x, 5) not in listRoot and x >= begin and x <= end:
                listRoot.append(round(x, 5))
        begin += step
    return listRoot


def click():
    begin = float(beginEntry.get())
    end = float(endEntry.get())
    step = float(stepEntry.get())
    allRoot = findRoot(begin, end, step, [])
    j = 6
    for i in allRoot:
        lbl = Label(text=f'Корень >>> {i}', font=('Consolas', 12))
        lbl.grid(row=j, column=0)
        j += 1
    graph = Graph(begin, end, function, allRoot)
    graph.showGraph()

begin = -10
end = 10
step = 0.004
eps = 1e-8
allRoot = findRoot(begin, end, step, [])

print(allRoot)

window = Tk()
window.title('Уточнение корней')
window.geometry('300x300')

beginLabel = Label(window, text=' Начало  >>>  ', font=('Consolas', 12))
beginEntry = Entry(window, width=25)
endLabel = Label(window, text=' Конец   >>>  ', font=('Consolas', 12))
endEntry = Entry(window, width=25)

stepLabel = Label(window, text=' Шаг     >>>  ', font=('Consolas', 12))
stepEntry = Entry(window, width=25)

lbl = Label(window, text=' ')
btn = Button(text='Посчитать', padx=15, pady=10, font=('Consolas', 15), command=click)

beginLabel.grid(row=0, column=0)
beginEntry.grid(row=0, column=1)
endLabel.grid(row=1, column=0)
endEntry.grid(row=1, column=1)
stepLabel.grid(row=2, column=0)
stepEntry.grid(row=2, column=1)
lbl.grid(row=3, column=0)
btn.grid(row=4, column=0, columnspan=2)
lbl.grid(row=5, column=0)


window.mainloop()

