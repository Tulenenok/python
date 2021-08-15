# Гурова Наталия ИУ7-14Б

# Вычислить сумму заданного бесконечного ряда с точностью eps.
# Вывести таблицу промежуточных значений с заданным шагом step.
# Контролировать максимальное число итераций max_i

import math

# Ввод данных
x = float(input('Введите x: '))
eps = float(input('Введите необходимую точность eps: '))
max_i = int(input('Введите максимальное число итераций: '))
step = int(input('Введите шаг для вывода таблицы: '))

# Проверка корректности введенных данных
while eps > 1:
    print('Точность слишком большая, значение может быть вычесленно неверно. Вы уверены, что хотите продолжить?')
    a = input('Введите "да" или "нет"')
    if a == 'нет' or a == 'Нет':
        eps = float(input('Введите необходимую точность eps: '))
    else:
        break

# Инициализация начальных переменных
sn = 1
n = 3
kol_i = 1
new = - x**2 / 2
n_i = []
last_item = []
sum_now = []

# Вычисление суммы
while True:
    if kol_i > max_i:
        print('Число итераций превышено, вычислить значение невозможно')
        break
    sn += new
    if kol_i % step == 1 or step ==1:
        n_i.append(kol_i)
        last_item.append(new)
        sum_now.append(sn)

    new = - new * x * x / (n * (n + 1))

    if math.fabs(new) < eps:
        print('Сумма бесконечного ряда = ', "%10.6g" % sn)
        break

    n += 2
    kol_i += 1

# Вывод таблицы
if kol_i <= max_i:
    print('|      n        |      t        |      s        |')
    for i in range(len(n_i)):
        print('|' + str("%15.6g" % n_i[i]) + '|' + str("%15.6g" % last_item[i]) + '|' + str("%15.6g" % sum_now[i]) + '|')

