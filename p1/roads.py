# Гурова Наталия ИУ7-14Б
# Написать программу, которая для массива NB(N, N), элементы которого имеют значения
# 1, если дорога существует
# 0, если нет
# определить номера городов, дороги между которыми составляют треугольники

# Проверка, является ли число целым
def isInteger(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

print('Задача про города и треугольники', '\n')

# Ввод количества точек и проверка, что введено натуральное число
n = input('Введите количество точек: ')
while isInteger(n) == False:
    print('Значение введено неверно. Необходимо натуральное число')
    n = input('Введите количество точек: ')
while int(n) <= 0:
    print('Значение введено неверно. Необходимо натуральное число')
    n = input('Введите количество точек: ')
n = int(n)

# Ввод таблицы дорог в виде матрицы
a = [list(map(str, input('Введите строку ' + str(i+1) + ': ').split())) for i in range(n)]

# Проверка, что все значения в матрице = 1 или 0 и замена неверных значений
for i in range(n):
    for j in range(n):
        while a[i][j] != '0' and a[i][j] != '1':
            print('Значение в строке', i+1, 'столбце', j+1, 'введено некорректно. Повторите ввод')
            a[i][j] = input('Введите значение в строке ' + str(i+1) + ' столбце ' + str(j+1) + ': ')

test = [['1', '1', '1', '1', '0', '1'], ['1', '1', '1', '1', '1', '0'], ['1', '1', '1', '0', '1', '0'], ['1', '1', '0', '1', '1', '0'], ['0', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '1', '1'],]
ans = []

# Нахождение пар трегольников, добавление их в матрицу ans
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == '1':
            for k in range(n):
                if k != i and k != j and a[j][k] == '1' and a[k][i] == '1':
                    b = [i + 1, j + 1, k + 1]
                    b.sort()
                    if b not in ans:
                        ans.append(b)

# Вывод матрицы дорог
print('Таблица дорог')
for row in a:
    print(' '.join(map(str, row)))

# Вывод матрицы треугольников
print()
print('Таблица треугольников')
max_len = 0
for i in range(len(ans)):
    for j in range(len(ans[i])):
        max_len = max(max_len, len(str(a[i][j])))
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], ' ' * (max_len - len(a[i][j])), end = '  ')
    print()
print()