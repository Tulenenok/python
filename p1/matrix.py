n = int(input('Введите размер матрицы: '))
i1, j1 = map(int, input('Введите i1, j1: ').split())
i2, j2 = map(int, input('Введите i2, j2: ').split())

matrix = [list(map(int, input('Введите строку матрицы №' + str(i + 1) + ' ').split())) for i in range(n)]

# Чтобы индексы совпадали с реальными индексами матрицы
i1 -= 1
j1 -= 1
i2 -= 1
j2 -= 1

# Построение прямой через эти две точки i = kj + b
k = (i1 - i2) / (j1 - j2)
b = i1 - k * j1

a = []                  # Вспомогательная матрица, чтобы видеть какие элементы он берет
average = 0             # Счетчик среднего
counter = 0             # Счетчик количества

for i in range(n):
    h = []
    for j in range(n):
        if i > k * j + b:
            h.append('*')
            average += matrix[i][j]
            counter += 1
        elif i == k * j + b:
            h.append('|')
            average += matrix[i][j]
            counter += 1
        else:
            h.append('0')
    a.append(h)

# Вывод вспомогательной матрицы
for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()

average /= counter

# Перемещение в одномерный массив
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] < average:
            ans.append(matrix[i][j])

print('Среднее арифметическое = ', average)
print('Одномерный массив = ', ans)


counter = 0                 # Счетчик количества таких последовательностей
i = 0
k = 1                       # Счетчик длины последовательности
flag = False                # Счетчик окончания последовательности
while i < len(ans) - 1:
    if ans[i+1] >= ans[i]:
        flag = True
        k += 1
    else:
        flag = False
        if k > 1:
            counter += 1
            k = 1
    i += 1
if flag and k > 1:
    counter += 1

print(counter)
