'''В текстовом файле in.txt записан текст, в котором есть вещественные числа с фиксированной точкой
(числа отделены от слов пробелами).
В файл out.txt переписать те из них, которые могут быть числами в восьмеричной системе счисления, каждое с новой строки.
Далее отделить в файле числа пустой строкой и, приняв эти числа числами в восьмеричной системе счисления,
записать их в шестнадцатеричной системе счисления по одному в строке (функции hex, int не использовать).
Целиком файл в память не считывать.'''


# Программа умеет переводит только числа без точки
def hexConvert(num):
    res = ''
    alp = '0123456789ABCDEF'
    if num == 0:
        return '0'
    while num != 0:
        res += alp[num % 16]
        num = num // 16
    return res[::-1]


def isFloat(x):
    try:
        x = float(x)
        return True
    except:
        return False

def decConvert(x):
    l = len(x) - 1
    res = 0
    while l >= 0:
        res += int(x[0]) * 8**l
        l -= 1
        x = x[1:]
    return res

with open('in.txt', 'r', encoding='utf8') as fin:
    fout = open('out.txt', 'w', encoding='utf8')
    for line in fin:
        flag = False                # Числа еще не было
        num = ''
        for elem in line:
            if elem in ['0', '1', '2', '3', '4', '5', '6', '7'] and not flag:
                flag = True
                num += elem
            elif elem in ['0', '1', '2', '3', '4', '5', '6', '7'] and flag:
                num += elem
            elif elem == '.' and flag:
                num += elem
            elif isFloat(elem) and float(elem) >= 8 and flag:
                flag = False
                num = ''
            elif flag:
                if isFloat(num):
                    fout.write(num + '\n')
                flag = False
                num = ''


        # Вторая часть работает, но почему то не дописывает в файл
        # Раскоментируйте, пожалуйста

        fin.seek(0)
        for line in fin:
            flag = False  # Числа еще не было
            num = ''
            for elem in line:
                if elem in ['0', '1', '2', '3', '4', '5', '6', '7'] and not flag:
                    flag = True
                    num += elem
                elif elem in ['0', '1', '2', '3', '4', '5', '6', '7'] and flag:
                    num += elem
                elif elem == '.' and flag:
                    num += elem
                elif isFloat(elem) and float(elem) >= 8 and flag:
                    flag = False
                    num = ''
                elif flag:
                    if isFloat(num):
                        num = decConvert(num)
                        fout.write(hexConvert(int(num)) + '\n')
                    flag = False
                    num = ''