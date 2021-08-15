# Проверка, что число является натуральным
def N_number(x):
    i = 0
    flag = True
    while i < len(x):
        if '0' <= x[i] <= '9' or x[i] == 'e':
            i += 1
        else:
            flag = False
            break
    return flag

# Проверка, что число является целым
def Z_number(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def F_number_new(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# Проверка, что число при вводе является действительным
def F_number(s):
    flag = True
    while flag == True:
        i = 0
        while i < len(s):
            if (ord('0') > ord(s[i]) or ord(s[i]) > ord('9')) and s[i] != 'e' and s[i] != '-' and s[i] != '.' and s[i] != '+' \
                    or s.count('e') > 1 or s.count('-') > 1 or s.count('.') > 1 or s.count('+') > 1 \
                    or (s[i] == 'e' or s[i] == '-' or s[i] == '+') and i == len(s) - 1 \
                    or (s[i] == 'e' and s[i+1] == '.') \
                    or s[i] == '-' and (s[i+1] == '+' or s[i+1] == '.' or s[i+1] == 'e') \
                    or s[i] == '+' and (s[i+1] == '-' or s[i+1] == '.' or s[i+1] == 'e') \
                    or s[i] == '.' and i != len(s) - 1 and ( [i+1] == '-' or s[i+1] == '+' or s[i+1] == 'e') \
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
        return float(s)

#Проверка, что это не число
def isStr(x):
    try:
        float(x)
        return False
    except ValueError:
        return True

def float_num(s):
    i = 0
    while i < len(s):
        if (ord('0') > ord(s[i]) or ord(s[i]) > ord('9')) and s[i] != 'e' and s[i] != '-' and s[i] != '.' and s[i] != '+' \
            or s.count('e') > 1 or s.count('-') > 1 or s.count('.') > 1 or s.count('+') > 1 \
            or (s[i] == 'e' or s[i] == '-' or s[i] == '+') and i == len(s) - 1 \
            or (s[i] == 'e' and s[i + 1] == '.') \
            or s[i] == '-' and (s[i + 1] == '+' or s[i + 1] == '.' or s[i + 1] == 'e') \
            or s[i] == '+' and (s[i + 1] == '-' or s[i + 1] == '.' or s[i + 1] == 'e') \
            or s[i] == '.' and i != len(s) - 1 and ([i + 1] == '-' or s[i + 1] == '+' or s[i + 1] == 'e') \
            or i == 0 and s[i] == 'e':
                return False
        else:
            i += 1
    return True

def menu():
    print()
    print('Введите 1, если хотите проинициализировать список')
    print('Введите 2, если хотите добавить элемент в произвольное место списка')
    print('Введите 3, если хотите удалить произвольный эл из списка')
    print('Введите 4, если хотите очистить список')
    print('Введите 5, если хотите найти значение k-того экстремума в списке')
    print('Введите 6, если хотите найти наиболее длинную убыв посл целых четных чисел')
    print('Введите 7, если хотите найти посл с наиб количеством эл строк')
    ans = input('Введите число от 1 до 7: ')
    return ans
    print()

def record_list(list, n, s):
    i = 0
    if n == 'all' or n == 'All':
        while i < len(s):
            list.append(s[i])
            i += 1
    else:
        while i < int(n):
            list.append(s[i])
            i += 1
    return list

def number_1(list):
    print('Вы хотите ввести значения из бесконечного ряда или с клавитатуры?')
    solve = input('1 - из бесконечного ряда, 2 - с клавиатуры ')
    while not ((solve == '1') or (solve == '2')):
        print('Введенные данные некоректны. Повторите ввод')
        solve = input('1 - из бесконечного ряда, 2 - с клавиатуры ')

    if solve == '2':
        n = input('Введите количество первых элементов массива, которые необходимо добавить в список. Введите "all", если необходимо добавить все ')
        while True:
            if n != 'all'  and n != 'All' and N_number(n) != True:
                n = input('Кол-во эл введено некорректно(необходимо целое число или all), повторите ввод ')
            else:
                break
        s = input('Введите ряд, все элементы необходимо вводить через пробел ').split()
        if len(list) == 0:
            record_list(list, n, s)
            return list
        else:
            print()
            print('В текущем списке уже существует элементы.')
            print('Если вы хотите добавить новые элементы в конец этого списка, введите 1.')
            print('Если вы хотите очистить список и записать новые элементы, введите 2.')
            while True:
                ans = input('Введите 1 или 2: ')
                if ans == '1' or ans == ' 1':
                    record_list(list, n, s)
                    return list
                elif ans == '2' or ans == ' 2':
                    list = []
                    record_list(list, n, s)
                    return list
                else:
                    print('Введенное значение некорректно. Повторите ввод')
    else:
        k = input('Введите количество элементов бесконечного ряда: ')
        while N_number(k) == False:
            print('Данные введены некорректно')
            k = input('Введите количество элементов бесконечного ряда: ')
        x = input('Введите x, для которого необходимо расчитать бесконечный ряд: ')
        while Z_number(x) == False:
            print('Данные введены некорректно')
            x = input('Введите x, для которого необходимо расчитать бесконечный ряд: ')
        x = int(x)
        k = int(k)
        new = - x ** 2 / 2
        n = 3
        for j in range(k):
            if j == 0:
                list.append('1')
            else:
                list.append(str("%3.3g" % new))
                new = - new * x * x / (n * (n + 1))
            n += 2
        return list


def number_2(list):
    x = input('Введите элемент, который необходимо добавить: ')
    n = input('Введите номер позиции, куда необходимо поставить элемент(нумерация начинается с 0): ')
    while True:
        if N_number(n) == False:
            print('Номер позиции введен неверно, повторите ввод.')
            n = input('Введите номер позиции, куда необходимо поставить элемент(нумерация начинается с 0): ')
        elif int(n) > len(list):
            print('Номер позиции введен неверно, повторите ввод.')
            n = input('Введите номер позиции, куда необходимо поставить элемент(нумерация начинается с 0): ')
        else:
            list.insert(int(n), x)
            break
    return list

def number_3(list):
    print('Вы хотетите удалить элемент по индексу или по значению?')
    ans = input('Введите 1, если по индексу. 2, если по значению: ')
    while True:
        if ans != '1' and ans != '2':
            ans = input('Значение введено неверно. Повторите ввод ')
        else:
            break
    if ans == '1':
        i = input('Введите индекс, с которого хотите удалить элемент ')
        while True:
            if N_number(i) == False or int(i) < 0 or int(i) >= len(list):
                i = input('Такого индекса не существует. Повторите ввод ')
            else:
                break
        list.pop(int(i))
        return list
    elif ans == '2':
        x = input('Введеите элемент, который хотите удалить ')
        while x not in list:
            x = input('Такого элемента в списке нет. Повторите ввод ')
        list.remove(x)
        return list

def number_4(list):
    list = []
    return list

def number_5new(list):
    solve = input('Введите max, если хотите искать максимальный экстремум, min если минимальный: ')
    while solve != 'min' and solve != 'max':
        solve = input('Значение введено неверно. Повторите ввод: ')
    ans = []
    for i in range(1, len(list) - 1):
            if F_number_new(list[i - 1]) and F_number_new(list[i]) and F_number_new(list[i + 1]):
                if solve == 'min':
                    if list[i] < list[i - 1] and list[i] < list[i + 1]:
                        ans.append(list[i])
                else:
                    if list[i] > list[i - 1] and list[i] > list[i + 1]:
                        ans.append(list[i])
    k = input('Введите номер экстремума, который хотите найти (нумерация начинается с 1): ')
    while True:
        if N_number(k) == False or int(k) - 1 < 0 or int(k) - 1 >= len(ans):
            k = input('Значение введено неверно(должно быть целое число). Повторите ввод: ')
        else:
            break
    if ans == []:
        print('Локальный экстремум невозможно найти')
    else:
        print(ans[int(k) - 1])

def number_5(list):
    for x in list:
        if F_number_new(x) == False:
            print('Текущий список не является числовым, поэтому вычислить значение экстремума невозможно')
            return list
    list_new = [float(x) for x in list]
    ans = input('Введите max, если хотите искать максимальный экстремум, min если минимальный: ')
    while ans != 'min' and ans != 'max':
        ans = input('Значение введено неверно. Повторите ввод: ')
    if ans == 'min':
        list_new.sort()
    else:
        list_new.sort(reverse=True)

    k = input('Введите номер экстремума, который хотите найти (нумерация начинается с 1): ')
    while N_number(k) == False and k-1 < 0 and k-1 >= len(list):
        k = input('Значение введено неверно(должно быть целое число). Повторите ввод: ')
    print(list_new, int(k) - 1)
    return list_new[int(k)-1]

def number_6(list):
    i = 0
    flag = False
    max_length = 0
    first_index = 0
    last_index = 0
    while i <= len(list) - 1:
        if i == len(list) - 1:
            if flag and Z_number(list[i]) and int(list[i]) % 2 == 0:
                length += 1
                last_id = i
                last_index = last_id if max_length < length else last_index
                first_index = first_id if max_length < length else first_index
                max_length = length if max_length < length else max_length
            i += 1
        else:
            if flag == False:
                length = 0
                first_id = i
                last_id = i
            if Z_number(list[i]):
                list[i] = int(list[i])
                if list[i] % 2 == 0 and Z_number(list[i+1]) and list[i] > int(list[i+1]):
                    length += 1
                    last_id = i
                    flag = True
                    i += 1
                else:
                    if list[i] % 2 == 0:
                        length += 1
                        last_id = i
                    flag = False
                    last_index = last_id if max_length < length else last_index
                    first_index = first_id if max_length < length else first_index
                    max_length = length if max_length < length else max_length
                    i += 1
            else:
                flag = False
                last_index = last_id if max_length < length else last_index
                first_index = first_id if max_length < length else first_index
                max_length = length if max_length < length else max_length
                i += 1
    if max_length == 0 or max_length == 1 and first_index == last_index:
        print('Такой последовательности не существует')
    else:
        print('Максимальная длина такой последовательности = ', max_length)
        print(first_index, last_index)
        print('Последовательность ', ' '.join(map(str, list[first_index:last_index + 1])))

def number_7(list):
    i = 0
    best_ans = []
    ans = []
    helper = []
    while i < len(list):
        if isStr(list[i]) == False:
            best_ans = ans[:] if len(ans) > len(best_ans) and len(ans) > 1 else best_ans[::]
            ans = []
            helper = []
            i += 1
        else:
            x = str(list[i])
            if len(helper) == 0:
                ans.append(x)
                for k in x:
                    helper.append(k.lower())
            else:
                flag = True
                for j in x:
                    if (j not in helper) and (j.lower() not in helper):
                        flag = False
                        break
                if flag == True:
                    ans.append(x)
                else:
                    best_ans = ans[::] if len(ans) > len(best_ans) and len(ans) > 1 else best_ans[::]
                    ans = [x]
                helper = []
                for k in x:
                    helper.append(k.lower())
            i += 1
    best_ans = ans[:] if len(ans) > len(best_ans) and len(ans) > 1 else best_ans[::]
    if len(best_ans) == 0:
        print('Такой последовательности не сущ')
    else:
        print('Максимальная длинна такой последовательности =', len(best_ans))
        print('Последовательность ', ' '.join(best_ans))


list1 = ['2', '16.0', '8', '4', '2', 'str', '2', '2', '3', '8', '6', '4', '2', 'gfc']
list2 = ['Aswer', 'ans', 'a', 'ns', 'n']
list = []
while True:
    ans = menu()
    if ans == '1':
        list = number_1(list)
        print('Текущий список ', list)
    elif ans == '2':
        list = number_2(list)
        print('Элемент добавлен')
        print('Текущий список: ', list)
    elif len(list) == 0 and ans > '2' and ans < '8':
        print('Ваш список пуст. Произвести над ним эту операцию невозможно.')
        print('Добавьте элементы в список командами 1 или 2')
    elif ans == '3':
        list = number_3(list)
        print('Элемент удален')
        print('Текущий список: ', list)
    elif ans == '4':
        list = number_4(list)
        print('Список очищен.')
        print('Текущий список: ', list)
    elif ans == '5':
        number_5new(list)
        print('Текущий список ', list)
    elif ans == '6':
        number_6(list)
        list = [str(x) for x in list]
        print('Текущий список ', list)
    elif ans == '7':
        number_7(list)
    else:
        print()
        print('Значение введено некорректно, повторите ввод')

    print()
    solve = input('Хотите продолжить? Введите Да/Нет: ')
    while True:
        if solve == 'Да' or solve == 'да':
            break
        elif solve == 'Нет' or solve == 'нет':
            break
        else:
            print('Значение введено некорректно. Повторите')
            solve = input('Хотите продолжить? Введите Да/Нет: ')
    if solve == 'Нет' or solve == 'нет':
        break