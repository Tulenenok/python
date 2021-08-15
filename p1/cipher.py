# Гурова Наташа ИУ7-14Б
# Лабораторная работа №9
# Шифрование и дешифрование введенной строки методом Виженера

import typeCheck

# Меню
def menu():
    print('  1 - Ввести строку' + '\n' +
          '  2 - Настроить шифрующий алгоритм' + '\n' +
          '  3 - Шифрование строки, используя шифр Виженера' + '\n' +
          '  4 - Расшифровывание строки')
    solve = input('Введите число от 1 до 4: ')
    while True:
        if not typeCheck.isInteger(solve) or solve not in ['1', '2', '3', '4']:
            solve = input('Значение введено некорректно. Повторите ввод: ')
        else: break
    return solve

# Ввод ключа
def inputKey(phrase):
    stroke = input(phrase).lower()
    stroke = stroke.replace(' ', '')
    while True:
        flag = stroke[0] in engAlphabet
        flag1 = flag2 = False
        for i in range(len(stroke)):                    # Проверка, что нет не англ или русских букв
            if stroke[i] not in engAlphabet and stroke[i] not in rusAlphabet:
                stroke = input('Некорректно. Допустимы только русские или английские буквы. Повторите: ')
                flag1 = True
                break
        if flag1: continue
        for j in range(len(stroke)):                    # Проверка, что слово однородно
            if flag != (stroke[j] in engAlphabet):
                stroke = input('Некорректно. Нельзя использовать и русские, и английские буквы. Повторите: ')
                flag2 = True
                break
        if flag2: continue
        return stroke

# Первый пункт меню
def inputStroke(phrase):
    stroke = input(phrase).lower()
    while True:
        flag = stroke[0] in engAlphabet
        flag1 = flag2 = False
        for i in range(len(stroke)):                    # Проверка, что нет не англ или русских букв
            if stroke[i] not in engAlphabet and stroke[i] not in rusAlphabet and stroke[i] != ' ':
                stroke = input('Некорректно. Допустимы только русские или английские буквы. Повторите: ')
                flag1 = True
                break
        if flag1: continue
        for j in range(len(stroke)):                    # Проверка, что слово однородно
            if flag != (stroke[j] in engAlphabet) and stroke[j] != ' ':
                stroke = input('Некорректно. Нельзя использовать и русские, и английские буквы. Повторите: ')
                flag2 = True
                break
        if flag2: continue
        return stroke

# Функция возвращает строку-ключ для конкретной строки(где ключ подставлен необходимое число раз)
def helpStroke(stroke, key):
    j = 0
    newStroke = ''
    for i in range(len(stroke)):
        if stroke[i] == ' ':
            newStroke += ' '
        else:
            newStroke += key[j]
            j += 1
            if j == len(key):
                j = 0
    return newStroke

# Проверка, что строка и ключ написаны в одинаковом алфавите
def alphabetRequest(stroke, key):
    while (stroke[0] in engAlphabet) != (key[0] in engAlphabet):
        print('Ключ и введенная строка(шифр) используют разные алфавиты. Необходимо, чтобы они совпадали')
        solve = input('Вы хотите поменять строку(шифр) или ключ? 1 - строка(шифр), 2 - ключ: ')
        while True:                             # Переввод, если что-то неправильно
            if solve == '1':
                stroke = inputStroke('Введите строку(шифр), которую вы хотите зашифровать(расшифровать): ')
                break
            elif solve == '2':
                key = inputStroke('Введите ключ, которым вы хотите шифровать: ')
                break
            solve = input('Значение введено неверно. Повторите ввод: ')
    return stroke, key

# Третий пункт меню
def creareCipher(stroke, key):
    newStroke = ''
    if stroke[0] in engAlphabet:                                        # Если строка состоит из английских букв
        for i in range(len(stroke)):
            if stroke[i] == ' ':
                newStroke += ' '
            else:
                sum = engAlphabet.index(stroke[i]) + engAlphabet.index(key[i])
                sum = sum - 26 if sum >= 26 else sum
                newStroke += engAlphabet[sum]
    else:                                                               # Если строка состоит из русских букв
        for i in range(len(stroke)):
            if stroke[i] == ' ':
                newStroke += ' '
            else:
                sum = rusAlphabet.index(stroke[i]) + rusAlphabet.index(key[i])
                sum = sum - 33 if sum >= 33 else sum
                newStroke += rusAlphabet[sum]
    return newStroke

# Четвертый пункт меню
def interpretCipher(cipher, key):
    newStroke = ''
    if cipher[0] in engAlphabet:                                        # Если шифр состоит из английских букв
        for i in range(len(cipher)):
            if cipher[i] == ' ':
                newStroke += ' '
            else:
                sum = engAlphabet.index(cipher[i]) - engAlphabet.index(key[i])
                sum = sum + 26 if sum < 0 else sum
                newStroke += engAlphabet[sum]
    else:                                                               # Если шифр состоит из русских букв
        for i in range(len(cipher)):
            if cipher[i] == ' ':
                newStroke += ' '
            else:
                sum = rusAlphabet.index(cipher[i]) - rusAlphabet.index(key[i])
                sum = sum + 33 if sum < 0 else sum
                newStroke += rusAlphabet[sum]
    return newStroke

# Инициализация переменных
engAlphabet = 'abcdefghijklmnopqrstuvwxyz'
rusAlphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
key = ''
stroke = ''
cipher = ''

# Основная программа
while True:
    solve = menu()
    if solve == '1':
        stroke = inputStroke('Введите строку, которую хотите зашифровать: ')
    elif solve == '2':
        key = inputKey('Введите ключ, которым хотите шифровать: ')
    elif solve == '3':
        if key == '' or stroke == '':
            print('Невозможно выполнить этот пункт, так как еще нет строки или ключа. Выполните сначала пункты 1, 2 ил 4')
        else:
            stroke, key = alphabetRequest(stroke, key)
            helpStr = helpStroke(stroke, key)
            strokeCipher = creareCipher(stroke, helpStr)
            print('Шифр Виженера для строки', str(stroke), ', с ключом', str(key), '=', strokeCipher)
    elif solve == '4':
        cipher = inputStroke('Введите шифр, который хотите расшифровать: ')
        if key == '':
            print('Невозможно выполнить этот пункт, так как еще нет ключа. Выполните сначала пункт 2')
        else:
            cipher, key = alphabetRequest(cipher, key)
            helpStr = helpStroke(cipher, key)
            cipherStr = interpretCipher(cipher, helpStr)
            print('Шифр Виженера', str(cipher), '- это строка', str(cipherStr))