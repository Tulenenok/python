# -*- coding: utf-8 -*-

from model.Book import Book

# Сортирует список книг по автору и названию
def sortedALl(listBooks):
    listBooks = sorted(listBooks, key=lambda book: (book.getAuthor(), book.getName()))
    return listBooks

# Читает все книги из файла, преобразует в список и сортирует по автору и названию
def findAll(fl):
    fin = open(fl, 'r', encoding='utf8')
    libraryList = []
    for line in fin:
        try:
            book = Book(line)
            if book.getName() != '' and '"' not in book.getAuthor() and book.getName() != '"':
                libraryList.append(Book(line))
        except: continue
    libraryList = sortedALl(libraryList)
    fin.close()
    return libraryList

# Находит в списке книг нужную по названию
def find(name, libraryList):
    for book in libraryList:
        if book.getName() == name: break
    return book

# Находит в библиотеке книги с нужным статусом
def findByStatus(status, libraryList):
    listWithStatus = []
    for book in libraryList:
        if book.getStatus() == status: listWithStatus.append(book)
    return listWithStatus

# Печатает результаты в текстовый файл
def saveAll(libraryList, fl):
    fout = open(fl, 'w', encoding='utf8')
    for book in libraryList:
        fout.write(book.getAll() + '\n')
    fout.close()


