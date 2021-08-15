# Гурова Наташа ИУ7-14Б
# Метод трапеций и метод Уэддля

import prettytable
import typeCheck
import sympy

import math

# Функция
def function(x):
    return x**2

# Метод трапеций
def methodTrap(a, b, n):
    step = (b - a) / n
    x = a
    trapArea = 0
    while x + step <= b:
        trapArea += (function(x) + function(x + step)) / 2
        x += step
    return trapArea * step

# Метод Уэддля
def methodWeddle(a, b, n):
    step = (b - a) / n
    j = a
    z = step / 6
    weddleArea = 0
    while j + step <= max(a, b):
        weddleArea += function(j)
        i = 2
        while i < 8:
            y = j + z * (i - 1)
            if i == 2 or i == 6:
                weddleArea += 5 * function(y)
            elif i == 4:
                weddleArea += 6 * function(y)
            else:
                weddleArea += function(y)
            i += 1
        j += step
    weddleArea *= (3 * z / 10)
    return weddleArea

# Вычисление интеграла с необходимой точностью
def strictArea(a, b, e, method):
    n = 1
    while abs(abs(method(a, b, 2 * n)) - abs(method(a, b, n))) > e:
        n = 2 * n
    return n, method(a, b, n)

# Определение абсолютной и относительной ошибки для кол-ва разбиений n и более неточного метода
def trouble(trapArea, weddleArea, exact, n, a, b, e):
    flag = abs(trapArea - exact) > abs(weddleArea - exact)
    if flag:
        print('Для количества разбиений = ', n, ' более неточным оказался метод трапеций')
    else:
        print('Для количества разбиений = ', n, ' более неточным оказался метод weddle')

    k, I = strictArea(a, b, e, methodTrap) if flag else strictArea(a, b, e, methodWeddle)
    print('Значение интеграла с точностью', '%6.6g' % e, ' = ', '%2.6g' % I)
    print('Количество участков разбиений = ', k)

    # Абсолютная ошибка
    absoluteError = abs(I - trapArea) if flag else abs(I - weddleArea)
    print('Абсолютная ошибка при кол-ве разбиений =', n, ': ', '%6.6g' % absoluteError)

    # Относительная ошибка
    relativeError = absoluteError * 100 / trapArea if flag else absoluteError * 100 / weddleArea
    print('Относительная ошибка при кол-ве разбиений =', n, ': ', '%1.2g' % abs(relativeError), '%')
    print()


# Ввод данных
n1 = typeCheck.natRequest('Введите кол-во разбиений n1: ')
n2 = typeCheck.natRequest('Введиет кол-во разбиений n2: ')
a = typeCheck.floatRequest('Введите начало интервала: ')
b = typeCheck.floatRequest('Введите конец интервала: ')
e = typeCheck.natFloatRequest('Введите необходимую точность е: ')

while a == b:
    print('Данные введены некорректно. a не может быть = b. Повторите ввод')
    a = typeCheck.floatRequest('Введите начало интервала: ')
    b = typeCheck.floatRequest('Введите конец интервала: ')

# Точное значение интеграла
x = sympy.Symbol('x')
a, b = min(a, b), max(b, a)
exact = sympy.integrate(function(x), (x, a, b))
print('Точное значение интегралла: ', exact)
# print('Точное значение интеграла = ', "%6.6g" % exact)

trapArea1 = methodTrap(a, b, n1)        # Подсчет методом трапеций при кол-ве разбиений n1
trapArea2 = methodTrap(a, b, n2)        # Подсчет методом трапеций при кол-ве разбиений n2
weddleArea1 = methodWeddle(a, b, n1)    # Подсчет методом Уэддля при кол-ве разбиений n1
weddleArea2 = methodWeddle(a, b, n2)    # Подсчет методом Уэддля при кол-ве разбиений n2

# Построение таблицы результатов
table = prettytable.PrettyTable()
table.title = 'Результаты вычислений'
table.field_names = ['Методы', 'n1 = ' + str(n1), 'n2 = ' + str(n2)]
table.add_row(['Трапеций', "%6.6g" % trapArea1, "%6.6g" % trapArea2])
table.add_row(['Weddle', "%6.6g" % weddleArea1, "%6.6g" % weddleArea2])
print(table)

# print()
# print('Результаты вычислений')
# print('Методы    ', 'n1             ', '  n2      ')
# print('Трапеций  ', str("%2.7g" % trapArea1), ' '*(15 - len(str("%2.7g" % trapArea1))),  str("%2.7g" % trapArea2))
# print('Weddle    ', str("%2.7g" % weddleArea1),' '*(15 - len(str("%2.7g" % weddleArea1))),  str("%2.7g" % weddleArea2))

# Вычисление интеграла с точностью и абсолютных/относительных ошибок
trouble(trapArea1, weddleArea1, exact, n1, a, b, e)
trouble(trapArea2, weddleArea2, exact, n2, a, b, e)

# a - начало интервала, б - конец интервала
# if a > b:
#     a, b = b, a
# Вычисление интеграла с точностью и абсолютных/относительных ошибок
# helper = input(
#     'Вы хотите вычислить интеграл для наиболее неточного метода или для любого? 1 - неточный, 2 - по выбору: ')
# while True:
#     if helper != '1' and helper != '2':
#         print('Значение введено некорректно. Повторите ввод')
#         solve = input(
#             'Вы хотите вычислить интеграл для наиболее неточного метода или для любого? 1 - неточный, 2 - по выбору: ')
#     else:
#         break
# print()
#
# if helper == '1':
#     trouble(trapArea1, weddleArea1, exact, n1, a, b, e)
#     trouble(trapArea2, weddleArea2, exact, n2, a, b, e)
# else:
#     solve = input('Для какого метода Вы хотите вычислить интеграл с точностью E? 1 - Трапеций, 2 - Weddle: ')
#     while True:
#         if solve != '1' and solve != '2':
#             print('Значение введено некорректно. Повторите ввод')
#             solve = input('Для какого метода Вы хотите вычислить интеграл с точностью E? 1 - Трапеций, 2 - Weddle: ')
#         else:
#             break
#
#     # Подсчет интеграла с необходимой точностью
#     k, I = strictArea(a, b, e, methodTrap) if solve == '1' else strictArea(a, b, e, methodWeddle)
#     print('Значение интегралла с точностью', '%6.6g' % e, ' = ', '%2.6g' % I)
#     print('Количество участков разбиений = ', '%2.6g' % k)
#
#     # Абсолютная ошибка
#     absoluteError = min(abs(I - trapArea1), abs(I - trapArea2)) if solve == '1' \
#         else min(abs(I - weddleArea1), abs(I - weddleArea2))
#
#     # Относительная ошибка
#     if solve == '1':
#         relativeError = absoluteError * 100 / trapArea1 if abs(I - trapArea1) < abs(I - trapArea2) \
#             else absoluteError / trapArea2
#     else:
#         relativeError = absoluteError * 100 / weddleArea1 if abs(I - weddleArea1) < abs(I - weddleArea2) \
#             else absoluteError / weddleArea2
#
#     print('Абсолютная погрешность = ', '%2.2g' % absoluteError)
#     print('Относительная погрешность = ', '%2.2g' % relativeError, '%')


