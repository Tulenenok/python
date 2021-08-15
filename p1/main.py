import random
import math
# Сортировка выбором
def simpleChoise(list):
    for i in range(len(list) - 1):
        # minElem = min(list[i + 1:])
        # minInd = list[i + 1:].index(minElem) + i + 1
        # list[i], list[minInd] = (list[minInd], list[i]) if minElem < list[i] else (list[i], list[minInd])
        minInd = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minInd]:
                minInd = j
        list[i], list[minInd] = list[minInd], list[i]
    return list

# Пузырьковая сортировка
def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

# Пузырьковая сортировка с флагом
def bubbleSortWithFlag(list):
    for i in range(len(list) - 1):
        flag = False
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = True
        if not flag:
            break
    return list

# Шейкерная сортировка
def shakerSort(list):
    begin = 0
    end = len(list) - 1
    while begin < end:
        newEnd = begin
        for i in range(begin, end):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                newEnd = i
            end = newEnd
        newBegin = end
        for i in range(end, begin, -1):
            if list[i] < list[i - 1]:
                list[i], list[i - 1] = list[i - 1], list[i]
                newBegin = i
        begin = newBegin
    return list

# Сортировка расческой
def combSort(list):
    distance = len(list) - 1
    while distance > 1:
        for i in range(len(list)):
            if i + distance < len(list) and list[i] > list[i + distance]:
                list[i + distance], list[i] = list[i], list[i + distance]
        distance = int(distance / 1.24)

    flag = True
    while flag:
        flag = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                flag = True
    return list

# Сортировка простыми вставками
def simpleInsection(list):
    for i in range(1, len(list)):
        elem = list[i]
        indBefore = i - 1
        while indBefore >= 0 and elem < list[indBefore]:
            list[indBefore + 1] = list[indBefore]
            indBefore -= 1
        list[indBefore + 1] = elem
    return list

# Сортировка вставками с барьером
def insertionWithBarrier(list):
    list = [0] + list
    for i in range(1, len(list)):
        list[0] = list[i]
        j = i - 1
        while list[0] < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = list[0]
    return list[1:]

# Сортировка вставками с бинарным поиском
def insertionBinary(list):
    for i in range(1, len(list)):
        begin = 0
        end = i
        while begin != end:
            middle = (begin + end) // 2
            if list[i] < list[middle]:
                end = middle
            else:
                begin = middle + 1
        elem = list[i]
        for j in range(i, begin, -1):
            list[j] = list[j - 1]
        list[begin] = elem
    return list

# Сортировка Шелла
def ShellSort(list):
    step = len(list) // 2
    while step:
        for j, elem in enumerate(list):
            ind = j
            while ind >= step and list[ind - step] > elem:
                list[ind] = list[ind - step]
                ind -= step
            list[ind] = elem
        step = 1 if step == 2 else int(step * 5 / 11)
    return list

# Быстрая сортировка
def quickSort(list):
    if not list:
        return list
    elem = random.choice(list)
    leftPart = [x for x in list if x < elem]
    rigthPart = [x for x in list if x > elem]
    countElem = list.count(elem)
    return quickSort(leftPart) + [elem] * countElem + quickSort(rigthPart)

x = int(input("ВВедите целое число"))
print(bin(x))

