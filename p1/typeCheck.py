# Проверка, что число типа int
def isInteger(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# Проверка, что число типа float
def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# Проверка, что число натуральное (с перезапросом, если это неверно)
def natRequest(s):
    x = input(s)
    while True:
        if isInteger(x) == False or int(x) <= 0:
            print('Значение введено неверно(должно быть натуральное число). Повторите ввод')
            x = input(s)
        else:
            break
    return int(x)

# Проверка, что число типа int (с перезапросом, если это неверно)
def intRequest(s):
    x = input(s)
    while isInteger(x) == False:
        print('Значение введено неверно(должно быть целое число). Повторите ввод')
        x = input(s)
    return int(x)

# Проверка, что число положительное типа float (с перезапросом, если это неверно)
def natFloatRequest(s):
    x = input(s)
    while True:
        if isFloat(x) == False or float(x) <= 0:
            print('Значение введено неверно(должно быть действительное число). Повторите ввод')
            x = input(s)
        else:
            break
    return float(x)

# Проверка, что число типа float (с перезапросом, если это неверно)
def floatRequest(s):
    x = input(s)
    while True:
        if isFloat(x) == False:
            print('Значение введено неверно(должно быть действительное число). Повторите ввод')
            x = input(s)
        else:
            break
    return float(x)