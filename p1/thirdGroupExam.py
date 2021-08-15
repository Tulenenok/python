'''В файле in.txt записаны строки, длина каждой не превышает 100 символов.
Столбцом символов в рамках этой задачи считать последовательность символов на одной
и той же позиции в каждой строке файла.
Требуется переписать в файл out.txt содержимое исходного файла так, чтобы туда не попали
столбцы из символов #, если они есть. Также к каждой строке через пробел нужно добавить число
слов-палиндромов длиной больше одного, которые в ней присутствуют.'''

def getLine(f):
    return f.readline().replace('\n', '')

def evenPolindrom(x):
    lX = x[:len(x) // 2]
    rX = x[len(x) // 2:]
    for i in range(len(lX)):
        if lX[i] != rX[-1 - i]:
            return False
    return True

def oddPolindrom(x):
    lX = x[:len(x) // 2]
    rX = x[len(x) // 2 + 1:]
    for i in range(len(lX)):
        if lX[i] != rX[-1 - i]:
            return False
    return True

def cutWord(x):
    result = ''
    rusAlth = ['абвгдеёжзийклмнопрстуфхзчшщьъэюя']
    for i in x:
        if i.isalpha() or i in rusAlth:
            result += i
    return result

with open('in.txt', 'r', encoding='utf8') as fin, open('out.txt', 'w', encoding='utf8') as fout:
    newLine = getLine(fin)
    positions = set()
    cntLine = 0
    while newLine:
        cntLine += 1
        for i in range(len(newLine)):
            if newLine[i] == '#':
                positions.add(i)
            elif i in positions:
                positions.remove(i)
        newLine = getLine(fin)

    fin.seek(0)
    newLine = getLine(fin)
    while newLine:
        j = 0
        listLine = newLine.split()
        for i in listLine:
            i = cutWord(i)
            if len(i) > 1 and (len(i) % 2 == 0 and evenPolindrom(i) or len(i) % 2 == 1 and oddPolindrom(i)):
                j += 1

        for i in range(len(newLine)):
            if i not in positions:
                elem = newLine[i]
                fout.write(elem)
        fout.write(' ' + str(j) + '\n')
        newLine = getLine(fin)
