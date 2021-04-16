import matplotlib.pyplot as plt

class Graph:
    def __init__(self, begin, end, step, function):
        self.step = abs(begin - end) / 1000
        self.x = []
        self.y = []
        self.generateX(begin, end, self.step)
        self.generateY(begin, end, self.step, function)
        self.createGraph()

    def generateX(self, begin, end, step):
        while begin < end:
            self.x.append(begin)
            begin += step

    def generateY(self, begin, end, step, function):
        self.y = []
        while begin < end:
            self.y.append(function(begin))
            begin += step

    def putRoots(self, tableRoot, color):
        xRoot = tableRoot['root'].values
        yRoot = tableRoot['F(root)'].values
        plt.plot(xRoot, yRoot, color, linewidth=3)

    def createGraph(self):
        plt.title('График функции')
        plt.xlabel('X')
        plt.ylabel('Function(x)')
        plt.plot(self.x, self.y, color='green')
        ax = plt.gca()
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        plt.grid(True)

    def addRoot(self, tableRoot, color):
        self.putRoots(tableRoot, color)

    def showGraph(self):
        plt.legend(['function', 'root', 'extreme', 'inflection'], loc=0)
        plt.show()



