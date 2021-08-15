# -*- coding: utf-8 -*-
class Book:
    __name = ''
    __author = ''
    __status = ''  # 0 - полка, 1 - на руках, 2 - на столе

    def __init__(self, information):
        self.__name, self.__author, self.__status = self.__readInf(information)

    # Метод позволяет разбить введенунную строку на Название книги(name), Автора(author) и Местонахождение(status)
    def __readInf(self, s):
        s = s.replace('\n', '')                 # Убираем из названия перевод строки
        firstInd = s.find('"')
        lastInd = s.rfind('"')
        name = s[firstInd:lastInd + 1]
        ind = lastInd + 1
        while s[ind] == ' ':                        # Пропускает пробелы до by
            ind += 1
        if s[ind] == 'b' and s[ind + 1] == 'y':     # Пропускает by
            ind += 2
        while s[ind] == ' ':                        # Пропускает пробелы после by
            ind += 1
        author = s[ind:]                                    # Имя автора
        status = 0                                          # Статус по умолчанию
        if s[-1] == '1' or s[-1] == '2' or s[-1] == '0':
            status = int(s[-1])
            author = author[:len(author) - 1]               # Если статус указан, то удаляет его из фамилии автора
        return name, author, status

    def setStatus(self, newStatus):                         # Поменять местонахождение книги(статус)
        self.__status = newStatus

    def getName(self):                                      # Возвращает название книги
        return self.__name

    def getAuthor(self):                                    # Возвращает автора книги
        return self.__author

    def getStatus(self):                                    # Возвращает текущий статус
        return self.__status

    def getAll(self):                                       # Возвращает все данные о книге
        return self.__name + ' by ' + self.__author + ' ' + str(self.__status)
    def toString(self):
        return self.__name + ' by ' + self.__author;
