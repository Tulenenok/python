# Гурова Наталия ИУ7-14Б
# Сформировать вектор Z из ненулевых элементов целочисленной матрицы В(9,11), которую рассматривать по столбцам.
# В полученном векторе третий положительный элемент заменить произведением предшествующих двух полож элементов.
# Напечатать матрицу и вектор

import typeCheck
import numpy

# Ввод количества строк и проверка, что введено натуральное число
print('Задача про вектор и матрицу' + '\n')
srk = input('Введите количество строк в матрице: ')
while typeCheck.isInteger(srk) == False:
    srk = input('Значение введено некорректно. Введите количество строк в матрице: ')
while int(srk) <= 0:
    srk = input('Значение введено некорректно. Введите количество строк в матрице: ')
srk = int(srk)

# Ввод количества строк и проверка, что введено натуральное число
stb = input('Введите количество столбцов в матрице: ')
while typeCheck.isInteger(stb) == False:
    stb = input('Значение введено некорректно. Введите количество столбцов в матрице: ')
while int(stb) <= 0:
    stb = input('Значение введено некорректно. Введите количество столбцов в матрице: ')
stb = int(stb)

# Ввод матрицы
a = [list(input('Введите строку матрицы №' + str(i + 1) + ': ').split()) for i in range(srk)]

print()


max_len = 0
for i in range(srk):
    for j in range(stb):
        max_len = max(max_len, len(str(a[i][j])))

for i in range(srk):
    for j in range(stb):
        print(a[i][j] + ' ' * (max_len - len(a[i][j])), end = '  ')
    print()
print()

ans = numpy.zeros(srk*stb)
k = 0
j = 0
i = 0
pol = []
while i < stb:
    j = 0
    while j < srk:
        if a[j][i] != '0' and typeCheck.isInteger(a[j][i]):
            if int(a[j][i]) > 0 and len(pol) < 3:
                if len(pol) < 2:
                    pol.append(int(a[j][i]))
                    ans[k] = int(a[j][i])
                else:
                    pol.append(int(a[j][i]))
                    ans[k] = pol[0]*pol[1]
            else:
                ans[k] = int(a[j][i])
            k += 1
        j += 1
    i += 1

ans = ans[:k]
print('Вектор')
for i in ans:
    print(int(i), end = ' ')
if len(pol) < 3:
    print('В векторе нет трех положительных элементов. Замена не была произведена')