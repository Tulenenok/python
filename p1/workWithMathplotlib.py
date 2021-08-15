import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy import linalg

# Построение нескольких графиков в одном листе, легенды
def severalGraths():
    x1 = np.linspace(-10, 10, 100)   # массив абсцисс для графиков синуса, косинуса и экспоненты
    x4 = np.linspace(-2, 2, 10)      # массив абсцисс для графика модуля
    y1 = np.sin(x1)
    y2 = np.cos(x1)
    y3 = x1**2 * np.exp(-x1**2)
    y4 = abs(x4)

    plt.plot(x1, y1, '--', label = 'sin(x)')               # штриховая линия
    #plt.plot(x1, y1, label = 'cos(x)')
    #plt.plot(x1, y3, '-.', label = 'x**2 * exp(-x**2)')    # штрих-пунктир
    plt.plot(x1, y3, '-.', label = '$x^2(exp(-x^2)$')
    plt.plot(x4, y4, ':', linewidth = 5, label = '|x|')    # пунктирная, толщиной 5
    plt.title('4 graphs')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc = 'best')
    plt.grid()
    plt.show()


# Как нарисовать два графика в разных листах (использование figure)
def twoUndependGraths():
    # Рисуем график синуса
    plt.figure(1)
    x1 = np.linspace(0, 6, 100)
    plt.plot(x1, np.sin(x1))
    plt.grid(True)
    plt.title('$sin(x)$')

    # Рисуем график х**2
    plt.figure(2)
    x2 = np.linspace(-6, 10, 100)
    plt.plot(x2, x2*x2)
    plt.grid(True)
    plt.title('$x^2$')

    plt.show()

# Как нарисовать несколько независимых графиков на одной фигур
def severalGrathsInOneList():
    plt.subplot(221)      # 2 - число строк, 2 - число столбцов, 1 - номер графика

    x1 = np.linspace(0, 6, 100)
    plt.plot(x1, np.sin(x1))
    plt.axis('equal')
    plt.grid(True)
    plt.title('$sin(x)$')

    x2 = np.linspace(-6, 10, 100)
    plt.subplot(222)
    plt.plot(x2, x2*x2, 'g')
    plt.grid(True)
    plt.title('$x^2$')

    x3 = np.linspace(-10, 10, 100)
    t = np.arange(-10, 11, 1)
    plt.subplot(223)
    plt.plot(x3, x3**2, 'orange', t, abs(t), 'mo')  # в одной области сразу два графика
    plt.title('$x^2$ и $|x|$')

    x4 = np.linspace(-10, 10, 100)
    plt.subplot(224)
    plt.plot(x4, -x4, 'y')
    plt.subplot(224).spines['left'].set_position('center')
    plt.subplot(224).spines['bottom'].set_position('center')
    plt.title('$x$')

    plt.show()

# Создание гистограммы
def createHist():
    x = np.random.rand(100)
    plt.hist(x, 10, color = 'orange')
    plt.show()


# Создание стобцевой диаграммы
def createBar():
    h1 = 10 * np.random.rand(6)
    h2 = 10 * np.random.rand(6)
    h3 = 10 * np.random.rand(6)

    pos = np.arange(1, len(h1) + 1)    # Массив с коорд левых точек первого столбца
    wide = 0.3                         # Ширина столбцов
    plt.bar(pos, h1, width = wide)     # Создание диаграммы заданной толщины
    plt.bar(pos + wide, h3, width = wide, color = 'y')
    plt.bar(pos + 2*wide, h2, width = wide, color = 'green')
    plt.xticks(pos + wide*1.5, pos)    # Изменение положения засечек на оси х
    plt.show()

# Создание круговой диаграммы
def createPie():
    x = [6, 12, 20, 7, 5, 5]
    languages = ['Matlab', 'Java', 'Python', 'C', 'C++', 'Other']

    plt.figure(figsize = (5, 5))
    explode = [0, 0, 0, 0.1, 0, 0]
    plt.pie(x, labels = languages, explode = explode, autopct = '%1.1f%%', shadow = False)
    plt.title('Circle diagram')
    plt.show()

# Арифметический масштаб (логарифмический график)
def createSemilogy():
    x = np.linspace(0, 10, 100)
    y = np.exp(-x*x)

    plt.subplot(121)
    plt.semilogy(x, y)

    plt.subplot(122)
    plt.plot(x, y, color = 'orange')
    plt.show()

# Вычисление интегралла
def strangeIntegral():
    def f(x):
        return x*x        # np.exp(-4*x) * np.sin(4*np.pi * x)

    a = 0
    b = 3
    m = 129

    x = np.zeros((m), float)
    y = np.zeros((m), float)
    y1 = np.zeros((m), float)

    for i in range(m):
        x[i] = a + (b - a) * i / (m - 1)
        y[i] = integrate.quad(f, 0, x[i])[0]

    plt.plot(x, f(x), color = 'r', label = '$f(x)$')
    plt.plot(x, y, label = '$\int_0^x t^2 dt$')

    i0 = integrate.quad(f, a, b)[0]
    i1 = integrate.trapz(y1, x)
    i2 = integrate.simps(y1, x)

    print('int(quad): ', i0)
    print('int(trapz): ', i1)
    print('int(simps): ', i2)

    plt.legend(loc = 0)
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

# Метод наименьшего квадрата
def smallestSquare():
    def f(x):
        return np.sin(x) * x * x + np.cos(x) / (x + 0.1)
    m = 20; n = 3; h = 1/m
    A = np.mat(np.zeros((m + 1, n + 1), float)) # mat - получить матрицу
    x = np.zeros((m + 1), float)
    y = np.zeros((m + 1), float)
    y1 = np.zeros((m+ 1), float)

    for i in range(m + 1):
        x[i] = i * h
        y[i] = f(x[i])
        for k in range(n):
            A[i, k] = x[i] ** k

    a, resid, rank, sigma = linalg.lstsq(A, y)

    for i in range(0, m + 1):
        xx = i
        sum = 0
        for k in range(0, n):
            sum += a[k] *xx**k
        y1[i] = sum

    plt.plot(x, y, '-', label = 'exact')
    plt.plot(x, y1, '*', label = 'polinom')
    plt.show()

def workWithAxis():
    x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
    y = np.sin(3 * x) / x
    y2 = np.sin(2 * x) / x
    y3 = np.sin(x) / x
    plt.plot(x, y, 'b')
    plt.plot(x, y2, 'g')
    plt.plot(x, y3, color = 'y')
    plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
               [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
    plt.yticks([-1, 0, 1, 2, 3], ['-1','0', '1', '2', '3'])


    # Работа с осями
    ax = plt.gca()                                  # Получаем объект axes
    ax.spines['right'].set_color('none')            # Убрать правую ось
    ax.spines['top'].set_color('none')              # Убрать верхнюю ось
    ax.xaxis.set_ticks_position('bottom')           # Сделать нижнюю ось осью x
    ax.spines['bottom'].set_position(('data', 0))   # Переместить нижнюю ось на 0
    ax.yaxis.set_ticks_position('left')             # Сделать левую ось осью y
    ax.spines['left'].set_position(('data', 0))     # Переместить левую ось на 0


    # Отметить какую-то точку указателем
    plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x} = 1$', xy = [0, 1], xycoords = 'data',
                xytext = [30, 30], fontsize = 16, textcoords = 'offset points', arrowprops = dict(arrowstyle="->",
                 connectionstyle="arc3,rad=.2"))
    plt.show()