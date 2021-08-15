from math import exp, sqrt, sin
from random import *

# Пример расчета таблицы значений
# Для того чтобы избежать ошибок округления, к конечному значению прибавляем шаг/2
def tableOfValuesExample():
    start, stop, step = map(float, input('Введите начало, конец и шаг через пробел: ').split())
    x = start
    print('  x           y')
    while x < stop + step / 2:
        y = exp(-x) * sqrt(x)
        print('{:7.2f} {:9.4f}'.format(x, y))
        x += step

# Метод итерации, задача - найти сумму бесконечного ряда
# Общая формула - (x**i) / i!
def sumInfinitySeries():
    eps = float(input('Введите необходимую точность: '))
    x = float(input('Введите х, для которого хотите посчитать ряд: '))
    fact = 0
    elem = 1
    sum = 1
    while abs(elem) > eps:
        fact += 1
        elem = elem * x / fact
        sum += elem
    print('x =', x, 'sum =', '{:3.3f}'.format(sum))

# Уточнение корней уравнения методом итерации
# Уравнение имеет вид sin(x) = x/2, его преобр к виду x = 2sin(x)
def clarificationOfRoots():
    eps = 1e-5
    x0 = -1.0
    x1 = 2 * sin(x0)
    while abs(x0 - x1) > eps:
        x0 = x1
        x1 = 2 * sin(x0)
    print(x1)

# Метод Монте-Карло (для определения площади)
def MonteKarloMethod():
    # Считает площадь под графиком у = x**2 при x принадлежащих от 0 до 1
    n = 3000000   # Количество точек, которые мы проверим
    pts = 0       # Количество точек, которые лежат в нужной нам площади
    i = 0
    while i <= n:
        x = random()  # Случайное число от 0 до 1
        y = random()
        if y <= x**2: # Если точка лежит под графиком, те принадлежит искомой площади
            pts += 1
        i += 1
    s = pts / n       # Отношение правильных точек к общему количеству
    print(s)


# Находит НОД и НОК двух чисел
def NOKandNOD():
    # m >= n, m > 0, n > 0
    n, m = map(int, input('Введите два числа m и n через пробел: ').split())
    r = m * n
    while n != 0:
        m, n = n, m % n     # Меньшее из чисел оставляем, другое делаем остатком от деления
    print('НОД =', m)
    print('НОК =', r // m)  # НОК - это произведение чисел делить на НОД