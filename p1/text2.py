'''В файле записан текст на английском языке, предложения разделяются точками.
Требуется переписать текст в новый файл так, чтобы каждое предложение было записано в
отдельной строке. Более одной строки файла в память не считывать.
Далее найти предложение с наибольшим количеством слов, в которых гласные и согласные буквы чередуются, и
дописать в файл его слова в порядке уменьшения количества букв.'''

def getLine(f):
    return f.readline()

def getLineByNumber(n, f):
    f.seek(0)
    line = getLine(f)
    i = 1
    while i != n:
        line = getLine(f)
        i += 1
    f.seek(0)
    return line

def sortByLen(word):
    return len(word)

with open('in.txt', 'r', encoding='utf8') as fin, open('out.txt', 'w+', encoding='utf8') as fout:
    for line in fin:
        line = line.replace('\n', '')
        for j in range(len(line)):
            if line[j] != '.':
                fout.write(line[j])
            elif line[j] == '.':
                fout.write(line[j] + '\n')

    cogl = 'bcdfghjklmnpqrstvwxyz'
    gl = 'aeiouy'
    fout.seek(0)
    i = 0
    maxCount = 0
    maxLine = 0
    for line in fout:
        i += 1
        line = line.replace('.\n', '')
        lineList = line.split()
        count = 0
        for word in lineList:
            flag = True
            if len(word) % 2 == 0:
                for j in range(len(word) - 1):
                    if (word[j] in cogl and word[j + 1] in gl) or (word[j] in gl and word[j + 1] in cogl):
                        pass
                    else:
                        flag = False
                        break
            else:
                for j in range(len(word) - 2):
                    if (word[j] in cogl and word[j + 1] in gl) or (word[j] in gl and word[j + 1] in cogl):
                        pass
                    else:
                        flag = False
                        break
            if flag:
                count += 1
        if count > maxCount:
            maxCount = count
            maxLine = i

    line = getLineByNumber(maxLine, fout).replace('.\n', '')
    lineList = line.split()
    lineList = sorted(lineList, reverse = True, key = sortByLen)
    fout.seek(0)
    for line in fout:
        pass
    fout.write('\n' + ' '.join(lineList) + '.')
