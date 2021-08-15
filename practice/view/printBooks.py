# -*- coding: utf-8 -*-

from dao import daoBook

# Записывает все книги из списка в файл, учитывая их местонахождение
def printInFile(stroke, listBooks, fout):
    fout.write(stroke + '\n')
    for book in listBooks:
        fout.write(book.toString() + '\n')
    fout.write('\n')

def toScreen(stroke, listBooks, fout):
    print(stroke + '\n')
    for book in listBooks:
        print(book.toString() + '\n')
    fout.write('\n')


# Печатает результаты для пользователя в текстовый файл
def printBooks(libraryList):
    listOnShelve = daoBook.findByStatus(0, libraryList)             # Все книги, которые сейчас на полке
    listOnHands = daoBook.findByStatus(1, libraryList)              # Все книги, которые сейчас на руках
    listOnTable = daoBook.findByStatus(2, libraryList)              # Все книги, которые сейчас на столе
    fout = open('files/userBooks.txt', 'w', encoding='utf8')
    printInFile('На полке: ', listOnShelve, fout)
    printInFile('На руках: ', listOnHands, fout)
    printInFile('На столе: ', listOnTable, fout)
    fout.close()

