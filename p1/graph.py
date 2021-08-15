# Гурова Наталия ИУ7-14Б

# Вычислить таблицу значений функций. Результаты оформить в виде таблицы с зоголовком.
# Пользователь вводит начало, шаг, конец интервала для x и количество засечек на графике

import math
import matplotlib.pyplot as pltplot
from prettytable import PrettyTable

# Ввод данных
start = float(input('Введите начало интервала: '))
step = float(input('Введите шаг: '))
stop = float(input('Введите конец интервала: '))
k_zasechek = int(input('Введите количество засечек на графике (целое число от 4 до 8): '))

# Проверка корректности введенных данных
while step == 0 or (start < stop and step < 0 ) or (start > stop and step > 0) or k_zasechek < 4 or k_zasechek > 8:
    print('Данные введены некорректно')
    print('Возможные ошибки: шаг равен 0, начало интервала < (>) конца интервала, а шаг отрицательный (положительный) \
          неверно введено количество засечек')
    print('Повторите ввод с корректными значениями')
    start = float(input('Введите начало интервала: '))
    step = float(input('Введите шаг: '))
    stop = float(input('Введите конец интервала: '))
    k_zasechek = int(input('Введите количество засечек на графике (целое число от 4 до 8): '))

#Инициализация данных
a = []
y = []
x = start

#Заголовок таблицы
pr = ' '*5
print('|' + pr + 'x' + pr + '|' + pr + 'y1' + pr + '|' + pr + 'y2' + pr + '|' + pr + 'y3' + pr + '|' + '\n' + '-'*52)

while (x <= stop and start < stop) or (x >= stop and start > stop):
    y1 = -(x**3 - 5.57*x**2 - 193*x - 633.1 )    # Первая функция
    min_y = y1 if x == start else min(min_y, y1)
    max_y = y1 if x == start else max(max_y, y1)
    flag = True
    if x != 1 and x > 0:
        y2 = x * math.log(x, math.e) - 52   # Вторая функция
        y3 = (y1 ** 3 - y2 ** 3) / 1000     # Третья функция
    else:
        y2 = 'НЗ'                           # НЗ - невозможно найти значение
        y3 = 'НЗ'
    a.append(x)                             # Добавление точек в массив для последующего построения графика
    y.append(y1)
    ans_y2 = str('|' + "%12.6g" % y2) if y2 != 'НЗ' else '|          НЗ'
    ans_y3 = str("%12.6g" % y3) if y3 != 'НЗ' else '          НЗ'
    print('|' + str("%11.6g" % x) + '|' + str("%12.6g" % y1) + ans_y2 + '|' + ans_y3 + '|')
    x += step                               # Изменение счетчика

# Построение графика
print('\n' + '\n')
zena_del = (max_y - min_y) / (80 + k_zasechek)
n = 1
y_pr = 0

if min_y >= 0:
    print('     ', end = '')
    # Отсечки по оси Oy
    while n <= k_zasechek:
        nomer_zasechri = min_y + n * zena_del * (80 // k_zasechek + 1)
        dl_zas = len(str("%3.3g" % nomer_zasechri))
        if dl_zas % 2 == 1:
            print((80 // k_zasechek - dl_zas // 2 - y_pr) * ' ' + str("%3.3g" % nomer_zasechri), end = '')
            y_pr = dl_zas // 2
        else:
            print((80 // k_zasechek - y_pr)*' ' + str("%3.3g" % nomer_zasechri), end = '')
            y_pr = dl_zas - 1
        n += 1

    # Ось OY
    print('\n' + ' x   ' + ((80 // k_zasechek) * '-' + '|') * k_zasechek + (80 % k_zasechek) * '-' + '> y')

    # Построение точек
    x = start
    for y1 in y:
        print(str("{:3.4g}".format(x)) + (5 - len(str("{:3.4g}".format(x)))) * ' ' + int((y1 - min_y) / zena_del - 1) * ' ' + '*')
        x += step

elif max_y <= 0:
    #Отсечки по оси Oy
    while n <= k_zasechek:
        nomer_zasechri = min_y + n * zena_del * (80 // k_zasechek + 1)
        dl_zas = len(str("%3.3g" % nomer_zasechri))
        if dl_zas % 2 == 1:
            print((80 // k_zasechek - dl_zas // 2 - y_pr) * ' ' + str("%3.3g" % nomer_zasechri), end = '')
            y_pr = dl_zas // 2
        else:
            print((80 // k_zasechek - y_pr)*' ' + str("%3.3g" % nomer_zasechri), end = '')
            y_pr = dl_zas - 1
        n += 1

    # Ось OY
    print('\n' + ((80 // k_zasechek) * '-' + '|') * k_zasechek + (80 % k_zasechek) * '-' + '> y' + '  x ')

    # Построение точек
    x = start
    for y1 in y:
        print(int((y1 - min_y) / zena_del - 1) * ' ' + '*' + (83 + k_zasechek - int((y1 - min_y) / zena_del - 1) - 1)*' ' + "{:3.4g}".format(x))
        x += step

else:
    # Отсечки по оси OY
    print('     ', end='')
    while n <= k_zasechek:
        nomer_zasechri = min_y + n * zena_del * (80 // k_zasechek + 1)
        dl_zas = len(str("%3.3g" % nomer_zasechri))
        if dl_zas % 2 == 1:
            print((80 // k_zasechek - dl_zas // 2 - y_pr) * ' ' + str("%3.3g" % nomer_zasechri), end='')
            y_pr = dl_zas // 2
        else:
            print((80 // k_zasechek - y_pr) * ' ' + str("%3.3g" % nomer_zasechri), end='')
            y_pr = dl_zas - 1
        n += 1

    # Ось OY
    print('\n' + ' x   ' + ((80 // k_zasechek) * '-' + '|') * k_zasechek + (80 % k_zasechek) * '-' + '> y')

    # Построение точек
    x = start
    for y1 in y:
        print(str("{:3.4g}".format(x)) + (5 - len(str("{:3.4g}".format(x)))) * ' ', end = '')       # Точка х
        if int(y1 - min_y) == 0:
            print('*' + int(math.fabs(min_y) / zena_del - 2) * ' ' + '|')
        else:
            if int(math.fabs(min_y - y1) / zena_del) < int(math.fabs(min_y) / zena_del):
                if x == 0:
                    kol_prob = int(math.fabs(min_y) / zena_del) - int((y1 - min_y) / zena_del - 1) - 3
                else:
                    kol_prob = int(math.fabs(min_y) / zena_del) - int((y1 - min_y) / zena_del - 1) - 2
                print(int((y1 - min_y) / zena_del - 1) * ' ' + '*' + kol_prob * ' ' + '|')
            elif int(math.fabs(min_y - y1) / zena_del) > int(math.fabs(min_y) / zena_del):
                print(int(math.fabs(min_y) / zena_del - 1)*' ' + '|' +int(y1 / zena_del - 1)*' ' + '*')
            else:
                print(int((y1 - min_y) / zena_del - 1) * ' ' + '*')
        x += step

# #Построение графика
# fig = pltplot.figure()                                                          # Создание рабочей области
# fig.set_facecolor('mintcream')                                                  # Цвет рабочей области
# ax_1 = fig.add_subplot(111)                                                     # Создание графика
# ax_1.set_facecolor('whitesmoke')
# ax_1.set_title('График функции', color = 'blue')                                # Название графика
# ax_1.set_xlabel('Ось Х')                                                        # Названия осей
# ax_1.set_ylabel('Ось Y')
# ax_1.plot(a, y, color = 'blue')                                                 # График линией
# ax_1.scatter(a, y, color = 'darkblue', marker = '*', linewidths = 3)            # График точками
# pltplot.show()