# Лабораторная работа №10
# Гурова Наталия ИУ7-14Б
import typeCheck

# Функция создает из файла массив строк
def createList(fl):
    fin = open(fl, 'r', encoding='utf8')
    newTextList = []
    maxLen = 0
    for line in fin:
        newTextList.append(line.replace('\n', '').strip())
        maxLen = max(len(line.replace('\n', '').strip()), maxLen)
    fin.close()
    return newTextList, maxLen

# Выравнивание текста по левому краю (пункт меню 1)
def alignLeft(textList, maxLen, fl):
    fout = open(fl, 'w', encoding='utf8')
    for elem in textList:
        elem = deleteSpace(elem)
        elem = elem.strip()
        fout.write(elem + '\n')
    fout.close()
    return textList

# Удаляет лишние пробелы в строке
def deleteSpace(stroke):
    i = 0; flag = True; newStroke = ''
    for i in range(len(stroke)):
        if stroke[i] != ' ':
            newStroke += stroke[i]
        elif stroke[i] == ' ' and stroke[i - 1] != ' ':
            newStroke += stroke[i]
    return newStroke

# Выравнивание по правому краю (пункт меню 2)
def alignRight(textList, maxLen, fl):
    fout = open(fl, 'w', encoding='utf8')
    for elem in textList:
        elem = deleteSpace(elem)
        elem = ' ' * (maxLen - len(elem)) + elem[:]
        fout.write(elem + '\n')
    fout.close()
    return textList

def alignWidth(textList, maxLen, fl):
    fout = open(fl, 'w', encoding='utf8')
    for elem in textList:
        if len(elem) != maxLen:
            margin = maxLen - len(elem)
            countSpace = elem.count(' ')
            newSpace = margin // countSpace + 1
            elem = elem.replace(' ', ' ' * newSpace)
            ind = elem.rfind(' ' * newSpace)
            elem = elem[:ind] + ' ' * (margin % countSpace) + elem[ind:]
        fout.write(elem + '\n')
    fout.close()
    return textList


# Удалить слово из текста (пункт 4)
def deleteWord(textList, fl):
    word = input('Введите слово, которое вы хотите удалить: ')
    lenWord = len(word) - 1
    count = 0
    for elem in textList:                                    # Находит, сколько раз слово встречается в тексте
        for i in range(lenWord, len(elem) - 2):
            if i == 0 and elem[i - lenWord:i + 2] == word + ' ':
                count += 1
            elif i == len(elem) - 2 and elem[i - lenWord:i + 2] == ' ' + word:
                count += 1
            elif elem[i - lenWord - 1:i + 2] == ' ' + word + ' ':
                count += 1
    if count == 0:                                           # Если такого слова нет
        print('В тексте такого слова нет. Ничего не было удалено')
        return textList
    else:
        print('В тексте найдено', count, 'таких слов.')
        ind = input('  all - удалить все' + '\n' +
                    'Введите команду: ')
        if ind.lower() == 'all':                                # Удалить все слова
            for elem in textList:
                if elem.lower().startswith(word.lower() + ' '):
                    stroke = elem[len(word) + 1:]
                    textList[textList.index(elem)] = stroke
                if elem.lower().endswith(' ' + word.lower()):
                    stroke = elem[:elem.rfind(' ' + word.lower())]
            textList = [elem.replace(' ' + word + ' ', ' ') for elem in textList]
            textList = [elem.replace(' ' + word + '.', '.') for elem in textList]
            textList = [elem.replace(' ' + word + ',', ',') for elem in textList]
        elif not typeCheck.isInteger(ind) or int(ind) > count:
            print('Ввод неверный')
        elif int(ind) <= count:                                    # Удалить конкретное слово по номеру
            kelem = 0
            for elem in textList:
                for i in range(lenWord, len(elem) - 2):
                    if elem[i - lenWord - 1:i + 2] == ' ' + word + ' ':
                        kelem += 1
                        if kelem == int(ind):
                            textList[textList.index(elem)] = elem[:i - lenWord] + elem[i + 1:]
    fout = open(fl, 'w', encoding='utf8')                      # Перезапись нового списка в файл
    for elem in textList:
        fout.write(elem + '\n')
    fout.close()
    return textList

# Замена одного слова другим во всем тексте (пункт меню 5)
def replaceWord(textList, fl):
    word = input('Введите слово, которое вы хотите заменить: ')
    newWord = input('Введите новое слово, на которое вы хотите заменить: ')
    fout = open(fl, 'w', encoding='utf8')
    for elem in textList:
        ind = textList.index(elem)
        elem = elem.replace(word, newWord)
        textList[ind] = elem
        fout.write(elem + '\n')
    fout.close()
    return textList

# Сколько слов небходимой длинны
def countBySize(size, stroke):
    count = 0
    for sym in ['.', ',', ':']:
        stroke = stroke.replace(sym, ' ')
    for x in stroke.split():
        if len(x) == size:
            count += 1
    return count

# Пункт меню 7
def countWord(textList):
    text = ''
    for i in textList:
        text += i
    newList = text.split('.')
    for elem in newList:
        if elem != '':
            # print(elem.strip() + '.')
            print('В предложении №' + str(newList.index(elem) + 1), 'было найдено: ' + '\n' +
                  str(countBySize(2, elem)), 'слов(а) из 2 букв' + '\n' +
                  str(countBySize(3, elem)), 'слов(а) из 3 букв' + '\n' +
                  str(countBySize(4, elem)), 'слов(a) из 4 букв' + '\n')

def OneSignLest(ind, stroke):
    newInd = ind - 1
    while stroke[newInd] not in ['+','-', '*', '/'] and newInd != 0 and newInd != len(stroke) - 1:
        newInd -= 1
    if newInd == '-' and (newInd == 0 or stroke[newInd - 1] in ['+', '*', '/', '(', ')']):
        return newInd
    if newInd == 0 or newInd == len(stroke) - 1:
        return newInd
    else:
        return newInd + 1

def OneSignRight(ind, stroke):
    newInd = ind + 1
    while stroke[newInd] not in ['+', '-', '*', '/'] and newInd != 0 and newInd != len(stroke) - 1:
        newInd += 1
    if stroke[newInd] == '-' and newInd == ind + 1:
        newInd += 1
        while stroke[newInd] not in ['+','-', '*', '/'] and newInd != 0 and newInd != len(stroke) - 1:
            newInd += 1
    if newInd == 0 or newInd == len(stroke) - 1:
        return newInd
    else:
        return newInd - 1

def Umn(firstUmn,stroke):
    leftInd = OneSignLest(firstUmn, stroke)
    rigthInd = OneSignRight(firstUmn, stroke)
    fNumber = float(stroke[leftInd:firstUmn])
    lNumber = float(stroke[firstUmn + 1:rigthInd + 1])

    if leftInd == 0 and rigthInd == len(stroke) - 1:
        stroke = str(fNumber * lNumber)
    elif leftInd == 0:
        stroke = str(fNumber * lNumber) + stroke[rigthInd + 1:]
    elif rigthInd == len(stroke) - 1:
        stroke = stroke[:leftInd] + str(fNumber * lNumber)
    else:
        stroke = stroke[:leftInd] + str(fNumber * lNumber) + stroke[rigthInd + 1:]
    return stroke

def Del(x,stroke):
    leftInd = OneSignLest(x, stroke)
    rigthInd = OneSignRight(x, stroke)
    fNumber = float(stroke[leftInd:x])
    lNumber = float(stroke[x + 1:rigthInd + 1])

    if leftInd == 0 and rigthInd == len(stroke) - 1:
        stroke = str(fNumber / lNumber)
    elif leftInd == 0:
        stroke = str(fNumber / lNumber) + stroke[rigthInd + 1:]
    elif rigthInd == len(stroke) - 1:
        stroke = stroke[:leftInd] + str(fNumber / lNumber)
    else:
        stroke = stroke[:leftInd] + str(fNumber / lNumber) + stroke[rigthInd + 1:]
    return stroke

def Slog(firstSlog, stroke):
    leftInd = OneSignLest(firstSlog, stroke)
    rigthInd = OneSignRight(firstSlog, stroke)
    fNumber = float(stroke[leftInd:firstSlog])
    lNumber = float(stroke[firstSlog + 1:rigthInd + 1])

    if leftInd == 0 and rigthInd == len(stroke) - 1:
        stroke = str(fNumber + lNumber)
    elif leftInd == 0:
        stroke = str(fNumber + lNumber) + stroke[rigthInd + 1:]
    elif rigthInd == len(stroke) - 1:
        stroke = stroke[:leftInd] + str(fNumber + lNumber)
    else:
        stroke = stroke[:leftInd] + str(fNumber + lNumber) + stroke[rigthInd + 1:]
    return stroke

def Diff(x,stroke):
    leftInd = OneSignLest(x, stroke)
    rigthInd = OneSignRight(x, stroke)
    fNumber = float(stroke[leftInd:x])
    lNumber = float(stroke[x + 1:rigthInd + 1])

    if leftInd == 0 and rigthInd == len(stroke) - 1:
        stroke = str(fNumber - lNumber)
    elif leftInd == 0:
        stroke = str(fNumber - lNumber) + stroke[rigthInd + 1:]
    elif rigthInd == len(stroke) - 1:
        stroke = stroke[:leftInd] + str(fNumber - lNumber)
    else:
        stroke = stroke[:leftInd] + str(fNumber - lNumber) + stroke[rigthInd + 1:]
    return stroke

def calc(stroke):
    stroke = stroke.strip('--')
    stroke = stroke.replace(' ', '')
    stroke = stroke.replace('--', '+')
    firstSkob = stroke.find('(')
    lastSkob = stroke.find(')')
    if firstSkob != lastSkob:                                               # Если скобки есть
        stroke = stroke[:firstSkob] + str(calc(stroke[firstSkob + 1: lastSkob])) + stroke[lastSkob + 1:]
    else:                                                                   # Если есть только арифметические операции
        umn = stroke.find('*')
        delet = stroke.find('/')
        if umn != -1 and delet == -1:                                       # Есть только умножение
            stroke = Umn(umn, stroke)
        elif delet != -1 and umn == -1:                                     # Есть только деление
            stroke = Del(delet, stroke)
        elif umn < delet:                                                     # Первым идет умножение
            stroke = Umn(umn, stroke)
        elif umn > delet:                                                   # Первым идет деление
            stroke = Del(delet, stroke)

        else:
            firstSlog = stroke.find('+')
            firstVic = stroke.find('-')
            if firstVic == 0 or stroke[firstVic - 1] in ['+', '*', '/', '(', ')']:
                firstVic = stroke[firstVic + 1:].find('-') + 1
                firstVic = -1 if firstVic == 0 else firstVic

            if firstSlog != -1 and firstVic == -1:                                          # Есть только сложение
                stroke = Slog(firstSlog, stroke)
            elif firstSlog == -1 and firstVic != -1:                                        # Есть только вычитание
                stroke = Diff(firstVic, stroke)
            elif firstSlog < firstVic:                                                      # Первым идет сложение
                stroke = Slog(firstSlog, stroke)
            elif firstSlog > firstVic:                                                      # Первым идет вычитание
                stroke = Diff(firstVic,stroke)
    if typeCheck.isFloat(stroke):
        return stroke
    else:
        return calc(stroke)

def arithmetic(textList):
    global fInd
    Alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя.:,-'
    Numbers = '1234567890()-'
    Operations = '+-/*.'
    for j in range(len(textList)):
        stroke = textList[j]
        i = 0
        firstInd = 0; lastInd = 0
        flag = False                                       # Арифметического выражения в строке нет
        while i < len(stroke):
            if stroke[i] in Numbers and not flag:
                firstInd = i
                flag = True                                # Т.е. есть арифметическое выражение хотя бы из одного числа
            elif (stroke[i] in Numbers or stroke[i] in Operations or stroke[i] == ' ') and flag:
                lastInd = i
            elif stroke[i] in Alphabet and flag:
                flag = False
                if firstInd != lastInd:
                    try:
                        result = calc(stroke[firstInd:lastInd + 1])
                        textList[j] = stroke[:firstInd] + ' ' + str(result) + ' ' + stroke[lastInd + 1:]
                        stroke = textList[j]
                    except:
                        print('Арифметическое выражение в строке №' + str(j + 1),
                              'введено неверно. Вычисленно не было.')
                        continue
            i += 1
    printInFile(textList, 'textForLab10.txt')
    return textList

def printInFile(textList, fl):
    fout = open(fl, 'w', encoding='utf8')
    for elem in textList:
        fout.write(elem + '\n')
    fout.close()

def maxLen(textList):
    maxL = 0
    for elem in textList:
        maxL = max(maxL, len(elem))
    return maxL


def menu():
    print('  1 - выравнивание по левому краю' + '\n' +
          '  2 - выравнивание по правому краю' + '\n' +
          '  3 - выравнивание по ширине' + '\n' +
          '  4 - удалить слово' + '\n' +
          '  5 - замена одного слова другим во всем тексте' + '\n' +
          '  6 - посчитать все арифметические выражениея в тексте' + '\n' +
          '  7 - определить сколько слов из 2, 3, 4 букв в кажждом предложении')
    solve = input('Введите число: ')
    return solve

textList, maxLenStroke = createList('textForLab10.txt')
solve = menu()
while True:
    if solve == '1':
        textList = alignLeft(textList, maxLenStroke, 'textForLab10.txt')
    elif solve == '2':
        textList = alignRight(textList, maxLenStroke, 'textForLab10.txt')
    elif solve == '3':
        textList = alignWidth(textList, maxLenStroke, 'textForLab10.txt')
    elif solve == '4':
        textList = deleteWord(textList, 'textForLab10.txt')
    elif solve == '5':
        textList = replaceWord(textList, 'textForLab10.txt')
    elif solve == '6':
        textList = arithmetic(textList)
        maxLenStroke = maxLen(textList)
    elif solve == '7':
        countWord(textList)
    else:
        print('Ввод неверный')
    solve = menu()


