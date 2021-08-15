import numpy as np
def printMatrix(matrix):
    for line in matrix:
        print(*line)
    print('\n')

''' Дано нечётное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."
(каждый элемент массива является строкой из одного символа). Затем заполните символами "∗" среднюю
строку массива, средний столбец массива, главную диагональ и побочную диагональ.
Для этого не нужно использовать вложенные циклы.'''

def program1():
    n = int(input())
    mat = [['*' if i == j or i + j == n - 1 or i == n // 2 or j == n // 2 else '.' for i in range(n)] for j in range(n)]
    for i in mat:
        print(*i)

'''На шахматной доске стоит конь. Отметьте положение коня на доске и все клетки, 
которые он бьет. Клетку, где стоит конь, отметьте английской буквой “K”. Клетки, которые он бьёт, 
отметьте символами “*”. Остальные клетки заполните точками.'''

def chessKnight():
    # Первая реализация
    dictColum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    posK = input('Введите поле, на котором стоит конь (в правильной шахматной нотации): ')
    columnK = dictColum[posK[0].lower()]
    rowK = 8 - int(posK[-1])

    chessBoard = [['.' for i in range(8)] for j in range(8)]
    chessBoard[rowK][columnK] = 'K'

    if rowK - 1 >= 0 and columnK - 2 >= 0:
        chessBoard[rowK - 1][columnK - 2] = '*'

    if rowK - 2 >= 0 and columnK - 1 >= 0:
        chessBoard[rowK - 2][columnK - 1] = '*'

    if rowK - 2 >= 0 and columnK + 1 < 8:
        chessBoard[rowK - 2][columnK + 1] = '*'

    if rowK - 1 >= 0 and columnK + 2 < 8:
        chessBoard[rowK - 1][columnK + 2] = '*'

    if rowK + 1 < 8 and columnK + 2 < 8:
        chessBoard[rowK + 1][columnK + 2] = '*'

    if rowK + 2 < 8 and columnK + 1 < 8:
        chessBoard[rowK + 2][columnK + 1] = '*'

    if rowK + 2 < 8 and columnK - 1 >= 0:
        chessBoard[rowK + 2][columnK - 1] = '*'

    if rowK + 1 < 8 and columnK - 2 >= 0:
        chessBoard[rowK + 1][columnK - 2] = '*'

    printMatrix(chessBoard)

    # Вторая реализация
    chessBoard = [['.' for i in range(8)] for j in range(8)]
    chessBoard[rowK][columnK] = 'K'
    for i in range(rowK - 1, rowK + 2, 2):
        if i >= 0 and i < 8:
            for j in range(columnK - 2, columnK + 3, 4):
                if j >= 0 and j < 8:
                    chessBoard[i][j] = '*'

    for i in range(rowK - 2, rowK + 3, 4):
        if i >= 0 and i < 8:
            for j in range(columnK - 1, columnK + 2, 2):
                if j >= 0 and j < 8:
                    chessBoard[i][j] = '*'

    print()
    printMatrix(chessBoard)

'''На шахматной доске стоит слон. Отметьте положение слона на доске и все клетки, 
которые он бьет. Клетку, где стоит слон, отметьте английской буквой “С”. Клетки, которые он бьёт, 
отметьте символами “*”. Остальные клетки заполните точками.'''

def chessBishop():
    dictColum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    posK = input('Введите поле, на котором стоит слон (в правильной шахматной нотации): ')
    columnK = dictColum[posK[0].lower()]
    rowK = 8 - int(posK[-1])

    chessBoard = [['.' for i in range(8)] for j in range(8)]
    chessBoard[rowK][columnK] = 'С'

    i = rowK - 1
    j = columnK + 1
    while i >= 0 and j < 8:
        chessBoard[i][j] = '*'
        i -= 1
        j += 1

    i = rowK - 1
    j = columnK - 1
    while i >= 0 and j >= 0:
        chessBoard[i][j] = '*'
        i -= 1
        j -= 1

    i = rowK + 1
    j = columnK - 1
    while i < 8 and j >= 0:
        chessBoard[i][j] = '*'
        i += 1
        j -= 1

    i = rowK + 1
    j = columnK + 1
    while i < 8 and j < 8:
        chessBoard[i][j] = '*'
        i += 1
        j += 1

    printMatrix(chessBoard)

'''На шахматной доске стоит ладья. Отметьте положение ладьи на доске и все клетки, 
которые она бьет. Клетку, где стоит ладья, отметьте русской буквой “Л”. Клетки, которые онф бьёт, 
отметьте символами “*”. Остальные клетки заполните точками.'''

def chessRook():
    dictColum = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    posK = input('Введите поле, на котором стоит ладья (в правильной шахматной нотации): ')
    columnK = dictColum[posK[0].lower()]
    rowK = 8 - int(posK[-1])

    chessBoard = [['.' for i in range(8)] for j in range(8)]

    for i in range(8):
        for j in range(8):
            if (i == rowK or j == columnK):
                chessBoard[i][j] = '*'
    chessBoard[rowK][columnK] = 'Л'
    printMatrix(chessBoard)

'''В файле дана квадратная матрица. Требуется змейкой переставить ее элементы,те первый столбец 
вниз, второй вверх, третий вниз и тд. Последний элемент становится первым'''

def verticalSnake():
    with open('in1.txt', 'r') as fin, open('out.txt', 'w') as fout:
        matrix = []
        for line in fin:
            matrix.append(list(line.split()))
        printMatrix(matrix)
        x = 1
        for j in range(len(matrix)):
            if j % 2 == 0:
                for i in range(len(matrix) - 1):
                    if i == 0 and j != 0:
                        matrix[i][j], elem = elem, matrix[i][j]
                    matrix[i + 1][j], elem = matrix[i][j] if i == 0 and j == 0 else elem, matrix[i + 1][j]
            else:
                for i in range(-1,-len(matrix), -1):
                    matrix[i][j], elem = elem, matrix[i][j]

        matrix[0][0] = elem
        printMatrix(matrix)

'''В файле дана квадратная матрица. Требуется змейкой переставить ее элементы,те первую строку 
влево, второй вправо, третий влево и тд. Последний элемент становится первым'''

def horisontalSnake():
    def getLine(f):
        return f.readline().split()

    with open('in1.txt', 'r') as fin, open('out.txt', 'w') as fout:
        newLine = getLine(fin)
        while newLine:
            lastEl = newLine[-1]
            newLine = getLine(fin)
        fin.seek(0)
        newLine = getLine(fin)
        i = 0
        while newLine:
            if i % 2 == 0:
                for j in range(len(newLine) - 1):
                    if j == 0 and i != 0:
                        elem, newLine[j] = newLine[j], elem
                    else:
                        elem, newLine[j + 1] = newLine[j + 1], (elem if j != 0 and i != 0 else newLine[j])
            else:
                for j in range(-1, -len(newLine) + 1, -1):
                    if j == -1:
                        elem, newLine[j] = newLine[j], elem
                    else:
                        elem, newLine[j - 1] = newLine[j - 1], elem
            if i == 0: newLine[0] = lastEl
            print(*newLine)
            newLine = getLine(fin)
            i += 1

'''Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j.'''
def swapColumn():
    def getLine(f):
        return f.readline().split()

    def printLine(line, f):
        f.write(' '.join(line) + '\n')

    with open('in1.txt', 'r') as fin, open('out.txt', 'w') as fout:
        first = int(input('Введите номер первого столбца: '))
        last = int(input('Введите номер второго столбца: '))
        newLine = getLine(fin)
        while newLine:
            newLine[first], newLine[last] = newLine[last], newLine[first]
            printLine(newLine, fout)
            newLine = getLine(fin)

'''Дано число n и массив размером n×n. Проверьте, является ли этот массив симметричным относительно главной диагонали'''
def symmetricMatrix():
    with open('in1.txt', 'r') as fin:
        matrix = []
        for line in fin:
            matrix.append(list(line.split()))

        flag = True
        for i in range(len(matrix)):
            for j in range(i):
                if matrix[i][j] != matrix[j][i]:
                    flag = False
                    break
            if not flag:
                break
        print(flag)

'''Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны,
то тот, у которого меньше номер столбца.'''

def minElem():
    def getLine(f):
        return list(map(float, f.readline().split()))

    with open('in1.txt', 'r') as fin:
        newLine = getLine(fin)
        minEl = newLine[0]
        minStroke = 0
        minStolbes = 0
        stroke = 0
        while newLine:
            for ind, elem in enumerate(newLine):
                if elem < minEl or elem == minEl and (stroke < minStroke or stroke == minStroke and ind < minStolbes):
                    minEl = elem
                    minStroke = stroke
                    minStolbes = ind
            newLine = getLine(fin)
            stroke += 1
    print(minEl, minStroke, minStolbes)

'''Дан квадратный массив. Поменяйте местами в каждом столбце элементы, стоящие на главной и побочной диагонали.'''
def swapDiagonals():
    with open('in1.txt', 'r') as fin, open('out.txt', 'w') as fout:
        matrix = []
        for line in fin:
            matrix.append(list(line.split()))

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    matrix[i][j], matrix[len(matrix) - 1 - i][i] = matrix[len(matrix) - 1 - i][i], matrix[i][j]
        for i in matrix:
            print(' '.join(i), file = fout)

'''Дан двумерный массив размером n×n. Транспонируйте его и результат запишите в этот же массив. 
Вспомогательный массив использовать нельзя.'''

def transposeMatrix():
    with open('in1.txt', 'r') as fin:
        matrix = []
        for line in fin:
            matrix.append(list(line.split()))

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in matrix:
            print(*i)


'''Даны два числа n и m. Создайте массив n×m и заполните его по следующим правилам:
Числа, стоящие в строке 0 или в столбце 0 равны 1 (A[0][j] = 1, A[i][0] = 1).
Для всех остальных элементов массива A[i][j] = A[i-1][j] + A[i][j-1],
то есть каждый элемент равен сумме двух элементов, стоящих слева и сверху от него.'''

def trianglePascal():
    m, n = map(int, input('Введите два числа m и n: ').split())
    matrix = [[1 for i in range(n)] for j in range(m)]
    print(matrix)
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    printMatrix(matrix)

'''В кинотеатре n рядов по m мест в каждом. В двумерном массиве хранится информация о проданных билетах,
число 1 означает, что билет на данное место уже продан, число 0 означает, что место свободно.
Поступил запрос на продажу k билетов на соседние места в одном ряду. Определите, можно ли выполнить такой запрос.'''

def cinemaPlace():
    def getLine(f):
        return f.readline().replace(' ', '')
    with open('in1.txt', 'r') as fin:
        k = int(input('Введите количество мест: '))
        newLine = getLine(fin)
        row = 1
        while newLine:
            if '0' * k in newLine:
                print(row)
                break
            newLine = getLine(fin)
            row += 1
        else:
            print(0)

'''Мудрец ходит по комнате размера n×m клеток. В каждой клетке комнаты лежит заданное количество золота. 
Проходя по клетке мудрец забирает всё золото с неё. Зная план комнаты и маршрут мудреца, 
посчитайте сколько золота он собрал. В задаче не гарантируется, что мудрец не проходил
по одной и той же клетке более одного раза.'''

def goldInRoom():
    def getLine(f):
        return tuple(f.readline().split())

    def getLineByNumber(n, f):
        f.seek(0)
        line = getLine(f)
        cnt = 0
        while cnt != n:
            line = getLine(f)
            cnt += 1
        return line

    with open('in1.txt', 'r') as fin1, open('in2.txt', 'r') as fin2:
        newCell = getLine(fin2)
        allCell = set()
        countGold = 0
        while newCell:
            if newCell not in allCell:
                allCell.add(newCell)
                rowCell = int(newCell[0]) - 1
                colCell = int(newCell[1]) - 1
                line = getLineByNumber(rowCell, fin1)
                countGold += int(line[colCell])
            newCell = getLine(fin2)
        print(countGold)

'''Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях — числа 2 и т.д.'''
def diagonals():
    matrix = [[abs(i - j) for j in range(4)] for i in range(4)]
    printMatrix(matrix)

'''По данным числам n и m заполните двумерный массив размером n×m числами от 1 до n×m “змейкой”,
как показано в примере.'''

def snake():
    m, n = map(int, input().split())
    matrix = [[j + 1 + i * n for j in range(n)] for i in range(m)]
    for i in range(1, len(matrix), 2):
        matrix[i] = matrix[i][::-1]
    printMatrix(matrix)

'''Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами 1 и 0 в шахматном порядке. 
В левом верхнем углу должна стоять единица'''

def simpleChessBoard():
    row, col = map(int, input(). split())
    mat = [[1 if (i + j) % 2 == 0 else 0 for i in range(col)] for j in range(row)]
    printMatrix(mat)

'''Последовательно заполнить матрицу горизонтально, начиная с 0'''
def fillMatrixH():
    row, col = map(int, input().split())
    mat = [[j + i * col for j in range(col)] for i in range(row)]
    printMatrix(mat)

'''Последовательно заполнить матрицу вертикально, начиная с 0'''
def fillMatrixV():
    row, col = map(int, input().split())
    mat = [[i + j * row for j in range(col)] for i in range(row)]
    printMatrix(mat)

'''Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной и побочных диагоналях стоят нули, эти диагонали делят массив на четыре части. 
В верхней части записаны единицы, в правой записаны двойки, в нижней записаны тройки, в левой записаны четверки.'''
def diffMat():
    row, col = map(int, input().split())
    mat = [[0 if i == j or i + j == row - 1 else
            1 if i < j and i + j < row - 1 else
            2 if i < j and i + j > row - 1 else
            3 if i > j and i + j > row - 1 else
            4 for j in range(col)] for i in range(row)]
    printMatrix(mat)

'''В прямоугольной таблице N×M вначале игрок находится в левой верхней клетке. 
За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз. 
Посчитайте, сколько есть способов у игрока попасть в правую нижнюю клетку.'''
def countSteps():
    row, col = map(int, input().split())
    mat = [[1 for j in range(col)] for i in range(row)]
    for i in range(1, row):
        for j in range(1, col):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    print(mat[-1][-1])

'''В каждой клетке прямоугольной таблицы N×M записано некоторое число. 
Изначально игрок находится в левой верхней клетке. За один ход ему разрешается перемещаться в 
соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). 
При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке 
(еду берут также за первую и последнюю клетки его пути).
Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.'''

def cheapWay():
    def getLine(f):
        return f.readline().split()

    with open('in1.txt', 'r') as fin:
        firstLine = getLine(fin)
        secondLine = getLine(fin)
        for i in range(1, len(firstLine)):
            firstLine[i] += firstLine[i - 1]

        while secondLine:
            for i in range(len(secondLine)):
                secondLine[i] = secondLine[i] + min(secondLine[i - 1] + firstLine[i]) if i > 0 else secondLine[i] + firstLine[i]
            firstLine = secondLine
            secondLine = getLine(fin)
        print(firstLine[-1])

'''На шахматной доске (8×8) стоит одна белая шашка. Сколькими способами она может пройти в дамки?'''
def checkers():
    cell = input('Введите клетку, на которой строит шашка: ')
    allCell = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    col, row = allCell[cell[0].lower()], 8 - int(cell[1])
    mat = [[0 for i in range(8)] for j in range(8)]
    mat[row][col] = 1
    printMatrix(mat)
    for i in range(row, 0, -1):
        for j in range(8):
            if mat[i][j] == 1 and j > 0:
                mat[i - 1][j - 1] = 1
            if mat[i][j] == 1 and j < 7:
                mat[i - 1][j + 1] = 1
            printMatrix(mat)
    print(sum(mat[0]))

'''В левом верхнем углу прямоугольной таблицы размером N×M находится черепашка. В каждой клетке таблицы записано 
некоторое число. Черепашка может перемещаться вправо или вниз, при этом маршрут черепашки заканчивается в правом нижнем
углу таблицы. Подсчитаем сумму чисел, записанных в клетках, через которую проползла черепашка 
(включая начальную и конечную клетку). Найдите наибольшее возможное значение этой суммы и маршрут,
на котором достигается эта сумма.'''

def expensiveWay():
    def getLine(f):
        return list(map(int, f.readline().split()))

    with open('in1.txt', 'r') as fin:
        mat = []

        firstLine = getLine(fin)
        for i in range(1, len(firstLine)):
            firstLine[i] += firstLine[i - 1]

        secondLine = getLine(fin)
        while secondLine:
            for i in range(len(secondLine)):
                secondLine[i] += max(secondLine[i - 1], firstLine[i]) if i != 0 else firstLine[i]
            mat.append(firstLine)
            firstLine = secondLine
            secondLine = getLine(fin)
        mat.append(firstLine)
        printMatrix(mat)
        print('Максимальная стоимость: ', firstLine[-1])
        result = ''
        i = len(mat) - 1
        j = len(mat) - 1
        while i != 0 or j != 0:
            if i == 0:
                j -= 1
                result += ' R'
            elif j == 0:
                i -= 1
                result += ' D'
            else:
                if mat[i - 1][j] > mat[i][j - 1]:
                    i -= 1
                    result += ' D'
                else:
                    j -= 1
                    result += ' R'
        print(result[::-1])

'''Количество столбцов в матрице, в которых элементы расположены по убыванию'''
def countCol():
    with open('in1.txt', 'r') as fin:
        matrix = []
        for line in fin:
            matrix.append(list(map(int, line.split())))
    result = 0
    for i in range(len(matrix)):
        coll = [matrix[j][i] for j in range(len(matrix))]
        if coll == sorted(coll,reverse = True):
            result += 1
    print(result)

'''Перед первым столбцом, содержащим только положительные элементы, вставить столбец из единиц. 
Если требуемых столбцов нет, то вывести матрицу без изменений.'''
def positiveCol():
    with open('in1.txt', 'r') as fin:
        matrix = []
        for line in fin:
            matrix.append(list(map(int, line.split())))

    for i in range(len(matrix)):
        coll = [matrix[j][i] for j in range(len(matrix))]
        if sum(coll) == sum([abs(i) for i in coll]) and 0 not in coll:
            index_coll = i
            for i in matrix:
                i.insert(index_coll,1)
            break
    printMatrix(matrix)

'''Дана квадратная матрица порядка М. Обнулить элементы матрицы, лежащие одновременно выше главной диагонали и ниже
побочной диагонали. Условный оператор не использовать.'''
def nullInMatrix():
    with open('in1.txt', 'r') as fin:
        matrix = []
        for line in fin:
            matrix.append(list(map(int, line.split())))

        M = len(matrix)
        for i in range(1, len(matrix) - 1):
            for j in range(int(abs(i - 0.5 * (M - 1)) + 0.5 * (M + 1)), M):
                matrix[i][j] = 0

    printMatrix(matrix)

'''Считает произведение строки на столбец для матрицы'''
def sumTwoLists(list1, list2):
    return sum([list1[i] * list2[i] for i in range(len(list2))])

'''Транспонирует матрицу произвольного размера'''
def transopeMat(list1):
    newList = []
    for i in range(len(list1[0])):
        stroke = []
        for j in range(len(list1)):
            stroke.append(list1[j][i])
        newList.append(stroke)
    return newList

'''Перемножает две матрицы заданные как list'''
def no_numpy_mult(first, second):
    secondT = transopeMat(second)
    result = []
    for i in range(len(first)):
        new = []
        for j in range(len(secondT)):
            sum = sumTwoLists(first[i], secondT[j])
            new.append(sum)
        result.append(new)
    return result

'''Перемножает две матрицы заданные как массив numpy'''
def numpy_mult(first, second):
    return np.dot(first, second)


'''Функция, которая последовательно читает из файла столбцы'''
def lenFirstStroke(f):
    ans = len(f.readline().replace('\n', ''))
    f.seek(0)
    return ans

def getColumn(n, f):
    res = []
    for line in f:
        res.append(line[n])
    f.seek(0)
    return res

with open('in1.txt', 'r') as fin, open('out.txt', 'w') as fout:
    for i in range(lenFirstStroke(fin)):
        fout.write(''.join(getColumn(i, fin)) + '\n')
