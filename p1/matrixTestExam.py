'''В файле in.txt записана квадратная целочисленная матрица
в следующем формате: N строк по N чисел, разделённых пробелами.
Необходимо изменить матрицу по следующему правилу: числа,
образующие периметр матрицы (внешний квадрат) - сместить по часовой стрелке
на 1, затем следующий вложенный квадрат (образованный из 2-й строки,
предпоследнего столбца, предпоследней строки и 2-го столбца) - сместить
против часовой стрелки на 1, затем следующий вложенный - по часовой стрелке
на 1, и так далее до центра матрицы.
Затем в получившейся матрице требуется найти столбцы с наибольшим элементом
матрицы и удалить их.
Записать в файл out.txt матрицу после первого преобразования,
затем пустую строку, затем матрицу с удалённым столбцом.'''

import numpy as np


# Читает из файла матрицу
def readFromFile():
    fin = open('in1.txt', 'r', encoding='utf8')
    matrix = []
    for line in fin:
        matrix.append(list(line.strip('\n').split()))
    fin.close()
    return matrix


# Пишет в файл первую матрицу
def printInFileFirst(matrix):
    fout = open('out.txt', 'w', encoding='utf8')
    for row in matrix:
        fout.write(' '.join(row) + '\n')
    fout.write('\n')
    fout.close()


# Пишет в файл вторую матрицу с удаленными столбцами
def printInFileSecond(matrix):
    fout = open('out.txt', 'a', encoding='utf8')
    for row in matrix:
        fout.write(' '.join(map(str, row)) + '\n')
    fout.close()


# Вспомогательный вывод, чтобы выводить в консоль
def printMatrix(matrix):
    for row in matrix:
        print(*row)
    print()


# Поворот по часовой
def moveRigth(matrix, ind, n):
    j = ind  # Заменяем первую строку
    while j != n - 1 - ind:
        elem, matrix[ind][j + 1] = matrix[ind][j + 1], matrix[ind][j] if j == ind else elem
        j += 1
    i = ind + 1  # Заменяем последний столбец
    while i != n - ind:
        elem, matrix[i][n - 1 - ind] = matrix[i][n - 1 - ind], elem
        i += 1
    j = n - 2 - ind  # Заменяем последнюю строку
    while j != ind - 1:
        elem, matrix[n - 1 - ind][j] = matrix[n - 1 - ind][j], elem
        j -= 1
    i = n - 2 - ind  # Заменяем первый столбец
    while i != ind - 1:
        elem, matrix[i][ind] = matrix[i][ind], elem
        i -= 1
    return matrix


# Поворот против часовой стрелки
def moveLeft(matrix, ind, n):
    i = ind
    while i != n - 1 - ind:
        elem, matrix[i + 1][ind] = matrix[i + 1][ind], matrix[i][ind] if i == ind else elem
        i += 1
    j = ind
    while j != n - 1 - ind:
        elem, matrix[n - 1 - ind][j + 1] = matrix[n - 1 - ind][j + 1], elem
        j += 1
    i = n - 2 - ind
    while i != ind - 1:
        elem, matrix[i][n - 1 - ind] = matrix[i][n - 1 - ind], elem
        i -= 1
    j = n - 2 - ind  # Заменяем последнюю строку
    while j != ind - 1:
        elem, matrix[ind][j] = matrix[ind][j], elem
        j -= 1
    return matrix


# ind - индекс элемента на главной диагонали, с которого начинаем крутить
# n - размер матрицы
# Делает один круг
def moveOneCircle(matrix, ind, n):
    if n % 2 == 1 and ind == n // 2:
        return matrix
    elif ind % 2 == 0:  # Крутим по часовой стрелке
        matrix = moveRigth(matrix, ind, n)
    elif ind % 2 == 1:
        matrix = moveLeft(matrix, ind, n)
    return matrix


# Делает все перемещения
def allMove(matrix, n):
    if n == 1: return matrix
    for k in range(n // 2):
        matrix = moveOneCircle(matrix, k, n)
    return matrix


# Удаляет столбцы с наибольшим элементом
def delMaxElement(matrix, n):
    matrix = np.array(matrix, int)
    maxEl = matrix.max()

    # Ищем все столбцы, где есть наибольший элемент
    delColumn = set()
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[i, j] == maxEl:
                delColumn.add(j)
    # Заменяем элементы в столбцах, которые нужно удалить на '', чтобы потом было проще их удалять
    matrix = matrix.tolist()
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if j in delColumn:
                matrix[i][j] = ''
            j += 1
    # Удаляем '', уменьшаем j на 1, если удалили, чтобы не было list index out of range
    for i in matrix:
        j = 0
        while j < len(i):
            if i[j] == '':
                i.pop(j)
                j -= 1
            j += 1
    return matrix


matrix1 = readFromFile()  # Считали матрицу из файла
n = len(matrix1)  # Размер матрицы

matrix1 = allMove(matrix1, n)  # Повернули
printInFileFirst(matrix1)  # Записали повернутую матрицу в файл

matrix1 = delMaxElement(matrix1, n)  # Удалили столбцы с наибольшими элементами
printInFileSecond(matrix1)  # Записали полученную матрицу в файл