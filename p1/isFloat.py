s = input('Введите число: ')
flag = True
while flag == True:
    i = 0
    while i < len(s):
        if (ord('0') > ord(s[i]) or ord(s[i]) > ord('9')) and s[i] != 'e' and s[i] != '-' and s[i] != '.' and s[i] != '+' \
                or s.count('e') > 1 or s.count('-') > 1 or s.count('.') > 1 or s.count('+') > 1 \
                or (s[i] == 'e' or s[i] == '.' or s[i] == '-' or s[i] == '+') and i == len(s) - 1 \
                or (s[i] == 'e' and s[i+1] == '.') \
                or s[i] == '-' and (s[i+1] == '+' or s[i+1] == '.' or s[i+1] == 'e') \
                or s[i] == '+' and (s[i+1] == '-' or s[i+1] == '.' or s[i+1] == 'e') \
                or s[i] == '.' and (s[i+1] == '-' or s[i+1] == '+' or s[i+1] == 'e') \
                or i == 0 and s[i] == 'e':
            print('Число введено некорректно')
            print('Повторите ввод')
            s = input('Введите число: ')
            flag = True
            break
        if i == len(s) - 1:
            flag = False
        i += 1
if flag == False:
    print('Вы ввели корректное число')
    x = float(s)
    