# Есть массив произвольных чисел. Нужно их отсортировать простым выбором

import time
import random
from sortResearch.sortError import Errors

# Сортировка простым выбором по возрастанию
def simpleSort(list):
    for i in range(len(list) - 1):
        minInd = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minInd]:
                minInd = j
        list[minInd], list[i] = list[i], list[minInd]
    return list

def takeTime(list):
    start = time.process_time()
    list = simpleSort(list)
    end = time.process_time()
    return (end - start) * 1e6

# Проводит исследование для одного списка
def researchList(randomList):
    if not Errors.invalidList(randomList):
        return ['', '', '']

    randomList = [float(i) for i in randomList.split()]
    randomTime = takeTime(randomList)

    orderList = simpleSort(randomList)
    orderTime = takeTime(orderList)

    reverseList = orderList[::-1]
    reverseTime = takeTime(reverseList)

    return [randomTime, orderTime, reverseTime]

# Создает рандомный список, возвращает строку
def makeRandomList(count):
    randomList = []
    for i in range(count):
        randomList.append(str(random.randint(-500, 500)))
    return ' '.join(randomList)
