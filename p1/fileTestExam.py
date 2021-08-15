import matplotlib.pyplot as plt
import math
def oneLine(f):
    return f.readline()

def takeArithmetic(stroke):
    numbers = [str(i) for i in range(10)]
    signs = ['+', '-', '*', '/']
    leftNumber = ''
    rightNumber = ''
    sign = ''
    stroke = stroke.replace(' ', '')
    for elem in stroke:
        if elem in numbers and not sign:            # Левое число, знак еще не найден
            leftNumber += elem
        elif elem in signs and not sign:            # Знак
            sign += elem
        elif elem in numbers and sign:              # Правое число, знак уже есть
            rightNumber += elem
        elif sign and rightNumber:                  # Если правое число закончилось
            leftNumber, rightNumber = float(leftNumber), float(rightNumber)
            if sign == '+':
                return leftNumber + rightNumber
            elif sign == '-':
                return leftNumber - rightNumber
            elif sign == '*':
                return leftNumber * rightNumber
            else:
                return leftNumber / rightNumber
    return 1

# Основная часть программы
# with open('in.txt', 'r', encoding='utf8') as fin:
#     fout = open('result.txt', 'w', encoding='utf8')
#     newLine = oneLine(fin)
#     while newLine:
#         count = takeArithmetic(newLine)
#         fout.writelines((newLine) * int(count))
#         newLine = oneLine(fin)
#     fout.close()

def readFromFile(f):
    return f.readline().replace('\n', '')

def rimNumber(x):
    stroke = ''
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rim = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    dicRim = {numbers[i] : rim[i] for i in range(len(numbers))}
    while x != 0:
        for num in dicRim:
            if x - num >= 0:
                x -= num
                stroke += dicRim[num]
                break
    return stroke

# Основная программа
# with open('in1.txt', 'r') as fin1, open('in2.txt', 'r') as fin2, open('out.txt', 'w+') as fout, \
#     open('out1.txt', 'w') as fout1:
#     line1 = readFromFile(fin1)
#     line2 = readFromFile(fin2)
#     while line1 and line2:
#         if float(line1) < float(line2):
#             fout.write(line1 + '\n')
#             line1 = readFromFile(fin1)
#         else:
#             fout.write(line2 + '\n')
#             line2 = readFromFile(fin2)
#     while line1:
#         fout.write(line1 + '\n')
#         line1 = readFromFile(fin1)
#     while line2:
#         fout.write(line2 + '\n')
#         line2 = readFromFile(fin2)
#     maxLen = -1
#
#     fout.seek(0)
#     for line in fout:
#         x = rimNumber(int(line.replace('\n', ' ')))
#         maxLen = max(len(x), maxLen)
#
#     fout.seek(0)
#     for line in fout:
#         x = rimNumber(int(line.replace('\n', ' ')))
#         fout1.write(x.center(maxLen) + '\n')

def function(x):
    return math.cos(x)

def myRound(x):
    return int(x) + 1 if str(x)[-1] == 5 else int(x)

begin = float(input('Введите начало интервала: '))
end  = float(input('Введите конец интервала: '))
step = float(input('Введите шаг: '))

print(' ' * 2 + 'x' + ' ' * 8 + 'r' + ' ' * 5)
result = []
x = []

if begin < end:
    i = begin
    while i <= end:
        result.append(function(i))
        x.append(i)
        print('{:5.2f}{:10.2f}'.format(i, function(i)))
        i += step if step > 0 else -step
else:
    i = begin
    while i >= end:
        result.append(function(i))
        x.append(i)
        print('{:5.2f}{:10.2f}'.format(i, function(i)))
        i += step if step < 0 else -step

count_ = 120
countY = 6

minY = min(result)
maxY = max(result)
stepY = abs((maxY - minY) / count_)

t = minY
print('\n' * 4 + ' ' * 10, end = '')
cnt = 0
while t < maxY and cnt < countY:
    newT = str(t)[:str(t).find('.') + 3] if str(t).find('.') != -1 else str(t)
    print(newT + ' ' * (count_ // countY - len(newT)), end = '')
    t += abs(maxY - minY) / countY
    if -1e-10 < t <= 1e-10: t = 0
    cnt += 1

print('\n' + ' ' * 10 + ('|' + '-'*(count_ // countY - 1))*countY + '>')

if minY <= 0 and maxY >= 0:
    position = myRound((0 - minY) / stepY)
    for i in range(len(x)):
        if result[i] < 0:
            countEl = myRound((result[i] - minY) / stepY)
            if countEl != position:
                print('{:9.2f}'.format(x[i]), ' ' * countEl + '*', end = '')
                print(' ' * (position - countEl - 1) + '|')
            else:
                print('{:9.2f}'.format(x[i]), ' ' * countEl + '*')
        elif result[i] == 0:
            print('{:9.2f}'.format(x[i]), ' ' * position + '*')
        else:
            countEl = myRound((result[i] - minY) / stepY)
            print('{:9.2f}'.format(x[i]), ' ' * position + '|', end = '')
            print(' ' * (countEl - position - 1) + '*')


else:
    for i in range(len(x)):
        countEl = myRound((result[i] - minY) / stepY)
        print('{:9.2f}'.format(x[i]), ' ' * countEl + '*')









# plt.plot(x, result, marker = '*', linestyle = '', color = 'indigo', label = '$x^2$')
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))
# plt.legend(loc = 0)
# plt.show()


