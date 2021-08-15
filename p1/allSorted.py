import random

# Сорторовка простым выбором
# Последовательно идем от начала списка до предпоследнего элемента
# В оставшемся справа массиве находим минимум, если нужно меняем их местами
def simpleChoise(list):
    for i in range(len(list) - 1):                      # Последовательно перебираем все позиции, куда будем класть min
        minEl = min(list[i + 1:])                       # Находим минимальный элемент среди оставшихся справа
        minInd = list[i + 1:].index(minEl) + i + 1      # Находим индекс этого минимального элемента, i + 1, чтобы индекс был для всего массива
        if minEl < list[i]:                             # Если найденный минимум меньше, то меняем их
            list[i], list[minInd] = minEl, list[i]
    return list
# Можно вместо срезов использовать доп.цикл
# minInd = i                                    # Считаем, что самый маленький элемент уже в нужном месте
# for j in range(i + 1, len(list)):             # Проходим по всей правой части
#     if list[j] < list[minInd]:                # Если находим меньший элемент меняем индекс
#         minInd = j
# list[i], list[minInd] = list[minInd], list[i] # Меняем местами. Если i останется равным minInd,то ничего не произойдет





# Простая сортировка пузырьком
def bubbleSort(list):
    for i in range(len(list) - 1):              # Количество перестановок, которого нам точно хватит
        for j in range(len(list) - 1 - i):      # Перебираем все элементы, можно и без -i, но проходов будем больше
            if list[j] > list[j + 1]:           # Меняем, если нужно
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

# Сортировка пузырьком с флагом
# Идем по массиву слева направо. Если текущий элемент больше следующего, меняем их местами. Делаем так, пока массив
# не будет отсортирован. Ассимптотика О(n**2) в худшем случае
def bubbleSortFlag(list):
    flag = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            flag = True
    if flag:
        list = bubbleSortFlag(list[:len(list) - 1]) + [list[len(list) - 1]]
    return list

# Простая реализация пузырьковой сортироки с флагом (без рекурсии)
def simpleBubbleSortFlag(list):
    for i in range(len(list) - 1):          # Проходов цикла в худшем случае будет len(list) - 1
        flag = False                        # Перестановок не было
        for j in range(len(list) - i - 1):  # Внутренние проходы по циклу, len(list) - i - 1 -- идем до отсортированных элементов
            if list[j] > list[j + 1]:       # Если порядок не соблюден, то меняем элементы
                list[j + 1], list[j] = list[j], list[j + 1]
                flag = True                 # Перестановка была
        if not flag:
            break
    return list





# Шейкерная сортировка
# Идем по массиву в обе стороны. Сначала слева направо - получаем самый большой элемент на последней позиции.
# Потом не возвращаемся в конец, а идем в обратную сторону - получаем min элемент на первом месте. И т.д.
# Ассимптотика такая же, как и у пузырька, но работает быстрее
def shakerSort(list):
    flag = True
    begin = 0
    end = len(list) - 1
    while flag:
        flag = False
        for i in range(begin, end):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                flag = True
        for j in range(end, begin, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                flag = True
        begin += 1
        end -= 1
    return list

# Улучшенный шейкер
def improveShakerSort(list):
    begin = 0
    end = len(list) - 1
    while begin < end:                  # Они сойдутся, когда не будет больше ни одной перестановки
        newEnd = begin
        for i in range(begin, end):     # Идем вправо
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                newEnd = i
        end = newEnd                    # Справа от нового end все элементы уже отсортированы, не имеет смысла проходить их еще раз
        newBegin = end
        for j in range(end, begin, -1): # Идем влево
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                newBegin = j
        begin = newBegin                # Слева элементы тоже точно отсортированы, тк там не было перестановок
    return list



# Сортировка расческой
# Для ускорения пузырька сначала берется расстояние между элементами равное не 1, а длине массива.
# Далее, после каждой итерации оно делится на 1.2473 и округляется до ближайщего целого. Когда становится < 1
# в ход вступает обычный пузырек. Ассимптотика в лучшем случае О(nlogn), в худшем O(n**2)
def combSort(list):
    distance = len(list) - 1
    flag = True
    while distance > 1:
        i = 0
        while i + distance < len(list):
            if list[i] > list[i + distance]:
                list[i], list[i + distance] = list[i + distance], list[i]
            i += 1
        distance = int(distance / 1.2473)

    flag = True
    while flag:
        flag = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                flag = True
    return list




# Сортировка вставками (наглядная реализация, но с двумя массивами)
# Есть отсортированный массив (изначально состоит только из первого элемента) и еще не отсортированный массив (все ост)
# Мы начинаем по одному перекладывать элементы из неотсорт в отсор. После каждого добавления перстановками добиваемся
# постановки элемента на правильное место в отсортированном массиве. Так делаем, пока не добавим все элементы
def insertionSort(list):
    finalList = [list[0]]
    originalList = list[1:]
    while len(finalList) != len(list):
        finalList.append(originalList[0])
        originalList = originalList[1:]
        i = len(finalList) - 2
        j = len(finalList) - 1
        while finalList[j] < finalList[i] and i != -1:
            finalList[j], finalList[i] = finalList[i], finalList[j]
            i -= 1
            j -= 1
    return finalList

# Нормальная сортировка вставками
def improveInsertionSort(list):
    for i in range(1, len(list)):   # Перебираем все элементы, начиная с 1
        indEl = i                   # Индекс текущего элемента, он меняется, поэтому запоминаем в отдельную переменную
        # Идем по массиву влево, пока есть, что переставлять, и пока элемент не дошел до конца(ищем позицию)
        while indEl - 1 >= 0 and list[indEl] < list[indEl - 1]:
            list[indEl - 1], list[indEl] = list[indEl], list[indEl - 1]
            indEl -= 1
    return list

# Другая нормальная реалицая сортировки вставками (это писать внутри for)
# elem = list[i]                    # Текущий элемент, которому мы ищем место
# indBefore = i - 1                 # Индекс первого элемента слево от него
# while indBefore >= 0 and elem < list[indBefore]:   # Перебираем все элементы слева
#     list[indBefore + 1] = list[indBefore]          # *Сдвигаем элементы на один вправо*
#     indBefore -= 1                                 # Проверяем следующий элемент
# list[indBefore + 1] = elem                         # Ставим элемент на найденную позицию

# Сортировка с барьером
# Чтобы избавится от условия indBefore >= 0 добавим в наш список на первое место 0 элемент
# В эту позицию при каждом проходе будем класть элемент, который двигаем и перемещать левые элементы вправо до тех пор,
# пока не найдем элемент не меньший, чем тот с которым мы сравниваем. Вернем наш элемент на эту позицию
def insertionSortWithBarierr(list):
    list = [0] + list                     # Увеличение размера массива на один элемент
    for indEl in range(1, len(list)):     # Пройдем по всем элементам массива
        list[0] = list[indEl]             # Кладем элемент, место которого мы ищем на нулевую позицию
        indBefore = indEl - 1             # Переберем все элементы левее нашего
        while list[0] < list[indBefore]:  # Делаем так, пока наш бездомный элемент меньше "левого" элемента
            list[indBefore + 1] = list[indBefore]
            indBefore -= 1
        list[indBefore + 1] = list[0]
    return list[1:]

# Сортировка с бинарным поиском
# Есть верхняя и нижняя границы. Сравнивается элемент с серединным и отправляется дальше в нужную часть списка
def insertionSortBinary(list):
    for i in range(1, len(list)):           # Перебираем все элементы начиная с 1 (нулевой уже отсортирован)
        lowerBorder = 0                     # Изначальная нижняя граница
        upperBorder = i                     # Изначальная верхняя граница
        while lowerBorder != upperBorder:   # Пока они не сошлись на одном значении
            middle = (lowerBorder + upperBorder) // 2
            if list[i] > list[middle]:
                upperBorder = middle        # Если нужно искать в левой части
            else:
                lowerBorder = middle + 1    # Если нужно искать в правой части
        elem = list[i]                      # Запомнили наш элемент
        for j in range(i, lowerBorder, -1):
            list[j] = list[j - 1]           # Передвинули необходимые элементы вправо
        list[lowerBorder] = elem            # Поселили элемент в нужное место
    return list



# Сортировка Шелла
# Та же сортировка вставками, но с определенным шагом. Изначально он равен длинна // 2, потом умножаем его на 5/11
def shellSort(list):
    step = len(list) // 2                                   # Первоначальный шаг
    while step:                                             # Идем, пока шаг не равен 0
        for i, elem in enumerate(list):                     # Пары индекс элемент из списка
            while i >= step and list[i - step] > elem:      # Пока есть, что двигать, двигаем
                list[i] = list[i - step]
                i -= step
            list[i] = elem                                  # Кладем наш элемент на освободившееся место
        step = 1 if step == 2 else int(step * 5 / 11)       # Меняем шаг
    return list


# Быстрая сортировка
def quickSort(list):
    if len(list) == 0:
        return list
    randInd = random.randint(0, len(list) - 1)              # Рандомно выбранный индекс элемента
    randElem = list[randInd]                                # Сам элемент
    leftPart = [x for x in list if x < randElem]            # Массив элементов, меньших выбранного
    rightPart = [x for x in list if x > randElem]           # Массив элементов, больших выбранного
    countElem = list.count(randElem)                        # Количество элементов, схожих с выбранным (иначе они удалятся,тк не входят ни в левую часть, ни в правую)
    return quickSort(leftPart) + [randElem] * countElem + quickSort(rightPart)      # Собираем новый массив по кусочкам




list = [0, 6, 3, 7, 0, 9, 12, 2, 12, 4, 90]
print(simpleBubbleSortFlag(list))