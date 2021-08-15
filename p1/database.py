# Лабораторная работа №11
# Гурова Наташа ИУ7-14Б
# Имитировать работу БД, используя бинарный файл
# Запись содержит 3-4 поля.
# Необходимо сделать меню:
#   1. Создание БД
#   2. Добавление записи в БД
#   3. Вывод всей БД
#   4. Поиск записей по одному полю
#   5. Поиск записей по одному полю
import pickle
import typeCheck
import prettytable

def menu():
    print('  1. Создание БД' + '\n' +
          '  2. Добавление записи в БД' + '\n' +
          '  3. Вывод всей БД' + '\n' +
          '  4. Поиск записей по одному полю' + '\n' +
          '  5. Поиск записей по двум полям')
    solve = input('Введите команду: ')
    return solve

# При создании новой БД проверяет название файла, в который она будет записываться
def importFile(s):
    nameFile = input(s)
    if nameFile.endswith('.txt'):
        print('Вы хотите использовать текстовый файл, но БД должна храниться в бинарном. Расширение изменено')
        nameFile = nameFile[:len(nameFile) - 4]
    if not nameFile.endswith('.bin'):
        nameFile += '.bin'
    while nameFile == '.bin' or len(nameFile) == 0:
        solve = input('Название файла введено некорректно повторите: ')
    return nameFile

# Реализует первый пункт меню, создает БД
def createBase():
    nameFile = importFile('Введите название файла, где будет храниться новая БД: ')
    fin = open(nameFile, 'wb')
    countFields = typeCheck.natRequest('Введите количество полей в БД: ')
    dict = {}
    for i in range(countFields):
        field = input('Введите поле №' + str(i + 1) + ' ')
        if field not in dict:
            dict[field] = ''
        else:
            print('Такое поле уже существует')
    pickle.dump(dict, fin)
    fin.close()
    print('БД создана')

# Возвращает ключи (поля) БД
def fieldBase(fileName):
    fin = open(fileName, 'rb')
    newDict = pickle.load(fin)
    fin.close()
    return newDict.keys()

# Вывод БД в консоль в виде таблицы
def printBase(fileName):
    fin = open(fileName, 'rb')
    table = prettytable.PrettyTable()
    while True:
        try:
            newDict = pickle.load(fin)
            table.field_names = newDict.keys()
            if list(newDict.values()) != ['']*len(list(newDict.values())):
                table.add_row(newDict.values())
        except EOFError:
            break
    fin.close()
    return table

# Выводит словарь (т.е. одну запись таблицы) в файл
def printInFile(newDict, fileName):
    fin = open(fileName, 'ab')
    pickle.dump(newDict, fin, protocol=None)
    fin.close()

# Осуществляет второй пункт меню, добавляет запись в БД
def addRecord(fileName):
    try:
        allKeys = fieldBase(fileName)
        newDict = {}
        for field in allKeys:
            valueField = input('Введите поле "' + str(field) + '": ')
            newDict[field] = valueField
        printInFile(newDict, fileName)
        print('Запись добавлена')
    except:
        print('Название файла введено неверно')

# Осуществляет вывод в консоль всех полей БД, используется в 4 и 5 пункте меню
def takeField(listKeys, s):
    i = 1
    for item in listKeys:
        print('  ' + str(i) + ' - ' + str(item))
        i += 1
    solve = typeCheck.natRequest(s)
    while solve > i:
        solve = typeCheck.natRequest('Значение введено неверно. Повторите: ')

    field = listKeys[solve - 1]
    valueField = input('Введите значение этого поля, по которому нужно искать: ')
    return field, valueField

# 4 пункт меню, ищет записи по одному полю
def findByField(fileName):
    fin = open(fileName, 'rb')
    table = prettytable.PrettyTable()
    newDict = pickle.load(fin)
    listKeys = list(newDict.keys())
    table.field_names = newDict.keys()
    field, valueField = takeField(listKeys, 'Введите номер поля, по которому вы хотите искать: ')
    if newDict[field].lower() == valueField.lower():
        table.add_row(newDict.values())
    while True:
        try:
            newDict = pickle.load(fin)
            if newDict[field].lower() == valueField.lower():
                table.add_row(newDict.values())
        except EOFError:
            break
    fin.close()
    return table

# 5 пункт меню, ищет записи по двум полям
def findByTwoField(fileName):
    fin = open(fileName, 'rb')
    table = prettytable.PrettyTable()
    newDict = pickle.load(fin)
    listKeys = list(newDict.keys())
    table.field_names = newDict.keys()
    field1, valueField1 = takeField(listKeys, 'Введите первое поле, по которому вы хотите искать: ')
    field2, valueField2 = takeField(listKeys, 'Введите второе поле, по которому вы хотите искать: ')
    while field1 == field2:
        print('Значение введено неверно. Нельзя искать по одному полю. Повторите')
        field1, valueField1 = takeField(listKeys, 'Введите первое поле, по которому вы хотите искать: ')
        field2, valueField2 = takeField(listKeys, 'Введите второе поле, по которому вы хотите искать: ')
    if newDict[field1].lower() == valueField1.lower() and newDict[field2].lower() == valueField2.lower():
        table.add_row(newDict.values())
    while True:
        try:
            newDict = pickle.load(fin)
            if newDict[field1].lower() == valueField1.lower() and newDict[field2].lower() == valueField2.lower():
                table.add_row(newDict.values())
        except EOFError:
            break
    fin.close()
    return table

while True:
    solve = menu()
    if solve == '1':
        createBase()
    elif solve == '2':
        try:
            fileName = input('Введите название файла, где находится БД: ')
            addRecord(fileName)
        except:
            print('Невозможно выполнить')
    elif solve == '3':
        fileName = input('Введите название файла, где находится БД: ')
        try:
            table = printBase(fileName)
            print(table)
        except:
            print('Название файла введено неверно')
    elif solve == '4':
        try:
            fileName = input('Введите название файла, где находится БД: ')
            table = findByField(fileName)
            print(table)
        except:
            print('Название файла введено неверно или он пуст')
    elif solve == '5':
        try:
            fileName = input('Введите название файла, где находится БД: ')
            table = findByTwoField(fileName)
            print(table)
        except:
            print('Название файла введено неверно или он пуст')
    else:
        print('Команда введена неверно')