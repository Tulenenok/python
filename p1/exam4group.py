''' В текстовом файле in.txt записан текст, в котором есть вещественные числа с фиксированной точкой
(числа отделены от слов пробелами).
В файл out.txt переписать те из них, которые могут быть числами в восьмеричной системе счисления, каждое с новой строки.
Далее отделить в файле числа пустой строкой и, приняв эти числа числами в восьмеричной системе счисления,
записать их в шестнадцатеричной системе счисления по одному в строке (функции hex, int не использовать).
Целиком файл в память не считывать. '''

def getLine(f):
    return f.readline().split()

def isFloat(x):
    try:
        x = float(x)
        return True
    except:
        return False

def isXinOct(x):
    if isFloat(x) and '8' not in x and '9' not in x:
        return True
    return False

def findOctInLine(line):
    num = []
    for elem in line:
        if isXinOct(elem):
            fout.write(elem + '\n')
            num += [elem]
    return num

def fromOcttoBin(x):
    result = ''
    if x.endswith('.'):
        x.replace('.', '')
    for i in x:
        if i == '-' or i == '.':
            result += i
        else:
            result += triad[i]
    return result

def toHexforInteger(x):
    x = x.lstrip('0')
    x = '0' * (4 - len(x) % 4) + x
    result = ''
    while x != '':
        y = x[:4]
        result += tetrad[y]
        x = x[4:]
    return result[1:] if result.startswith('0') else result

def toHexforFraction(x):
    x = x.rstrip('0')
    x += '0' * (4 - len(x) % 4)
    result = ''
    while x != '':
        y = x[:4]
        result += tetrad[y]
        x = x[4:]
    return result[:-1] if result.endswith('0') or result.endswith('.') else result

def fromBintoHex(x):
    if '-' in x:
        result = '-'
        x = x.replace('-', '')
    else:
        result = ''
    if '.' in x:
        beforePoint, afterPoint = x.split('.')
        result += toHexforInteger(beforePoint) + '.' + toHexforFraction(afterPoint)
        result = result.rstrip('.')
    else:
        result += toHexforInteger(x)
    return result

with open('in.txt', 'r', encoding='utf8') as fin, open('out.txt', 'w', encoding='utf8') as fout:

    triad = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
    tetrad = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
              '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D',
              '1110': 'E', '1111': 'F'}

    line = getLine(fin)
    numbers = []
    while line:
        numbers += findOctInLine(line)
        line = getLine(fin)

    fout.write('\n')

    for x in numbers:
        binX = fromOcttoBin(x)
        hexX = fromBintoHex(binX)
        fout.write(hexX + '\n')

