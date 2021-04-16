from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from defineRoot.rootControll import *
import pandas as pd

class Window:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def createWindow(self):
        self.window = Tk()
        self.window.title(self.name)
        self.window.geometry(self.size)

    def addFrame(self, row, column, frame, columnspan=1):
        frame.grid(row=row, column=column, columnspan=columnspan)

    def showWindow(self):
        self.window.mainloop()

class menuFrame:
    def __init__(self):
        self.menu = Menu()

    def __makeDropDown(self, menu, dictLabels):
        newItem = Menu(self.menu, tearoff=0)
        for item in dictLabels:
            newItem.add_command(label=item, command=lambda: dictLabels[item]())
        return newItem

    def createMenu(self):
        self.menu.add_cascade(label='Info', menu=self.__makeDropDown(self.menu, {'Информация об авторе': self.__info}))
        return self.menu

    def __info(self):
        messagebox.showinfo('Info', 'Программа была создана 22.03.21. \n Автор: Гурова Наталия ИУ7-24Б')

class Table:
    def __init__(self, table):
        self.setting()

        self.resultTable = table
        self.countRow = table.shape[0]
        self.heads = ['N'] + list(table.columns)
        self.values = []

    def setting(self):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Consolas', 13))
        style.configure('Treeview', rowheight=30, color='blue')

    def create(self):

        self.table = ttk.Treeview(show='headings')
        self.table['columns'] = self.heads

        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center', width=120, stretch=NO)

        self.__addRows()

        for row in self.values:
            self.table.insert('', 'end', values=row)

        return self.table

    def __addRows(self):
        for i in range(self.countRow):
            newRow = [i + 1] + [round(i, 3) for i in list(self.resultTable.iloc[i, ::].values)]
            self.values.append(newRow)

class entryFrame:
    @staticmethod
    def createEntry(row, column):
        entry = Frame(width=row, height=column)
        return entry

class Arrows:
    @staticmethod
    def createArrows(frame = None):
        arrowsFrame = Frame(frame) if (frame != None) else Frame()
        for i in range(5):
            arrow = Label(arrowsFrame, text='  >>>  ', font=('Consolas', 11))
            arrow.grid(row=i, column=1)
        return arrowsFrame

class allLabels:
    def __init__(self, listLabel):
        self.__frame = Frame()
        for i, label in enumerate(listLabel):
            newLabel = Label(self.__frame, text=label, font=('Consolas', 11))
            newLabel.grid(row=i, column=0)

    def create(self):
        return self.__frame

class allEntry:
    def __init__(self, count):
        self.__frame = Frame()
        self.__all = []
        self.__count = count

    def create(self):
        self.__createEntry().grid(row=0, column=0)
        Arrows.createArrows(self.__frame).grid(row=0, column=1)
        self.__clearOneButton().grid(row=0, column=2, rowspan=5)
        self.__clearAllButton().grid(row=0, column=3, rowspan=5, sticky='news')
        return self.__frame

    def setAll(self):
        return self.__all

    def __createEntry(self):
        entryFrame = Frame(self.__frame)

        for i in range(self.__count):
            newEntry = Entry(entryFrame, width=25)
            self.__all.append(newEntry)

            newLabel = Label(entryFrame, text='', font=('Consolas', 12))
            newLabel.grid(row=i, column=0)
            newEntry.grid(row=i, column=1)

        return entryFrame

    def __clearOne(self, i):
        self.__all[i].delete(0, last=END)

    def __clearAll(self):
        for i in self.__all:
            i.delete(0, last=END)

    def __clearOneButton(self):
        clearFrame = Frame(self.__frame)

        firstButton = Button(clearFrame, text='clear', font=('Consolas', 9), command=lambda: self.__clearOne(0))
        secondButton = Button(clearFrame, text='clear', font=('Consolas', 9), command=lambda: self.__clearOne(1))
        thirdButton = Button(clearFrame, text='clear', font=('Consolas', 9), command=lambda: self.__clearOne(2))
        fourthButton = Button(clearFrame, text='clear', font=('Consolas', 9), command=lambda: self.__clearOne(3))
        fifthButton = Button(clearFrame, text='clear', font=('Consolas', 9), command=lambda: self.__clearOne(4))

        allBut = [firstButton, secondButton, thirdButton, fourthButton, fifthButton]

        for i in range(self.__count):
            allBut[i].grid(row=i, column=0)
        return clearFrame

    def __clearAllButton(self):
        return Button(self.__frame, text='clear all', font=('Consolas', 9), command=lambda: self.__clearAll())

class MainButton:
    def __init__(self):
        self.__table = []
        self.__frame = Button(text='Провести расчет', font=('Consolas', 15), command=self.__click,
                              padx=190, pady=13)

    def create(self):
        return self.__frame

    def __drawTable(self, tableResult):
        table = Table(tableResult)
        window.addFrame(row=row + 5, column=column + 1, frame=table.create(), columnspan=5)

    def __click(self):
        allInput = []

        for i in range(len(allEnt.setAll())):
            allInput.append(allEnt.setAll()[i].get())

        flag, table, graph = main(allInput)

        if flag:
            self.__drawTable(table)
            graph.showGraph()


row = 0
column = 0
window = Window('Уточнение корней уравнения', '900x600')
window.createWindow()
allLab = allLabels(['Начало интервала', 'Конец интервала', 'Шаг',
                    'Точность измерений', 'Максимальное количество итераций'])
allEnt = allEntry(5)
mainBtn = MainButton()
table = Table(pd.DataFrame(columns=['begin', 'end', 'root', 'F(root)', 'countIter', 'Codeerror']))
window.addFrame(row=row, column=column, frame=entryFrame.createEntry(30, 20))
window.addFrame(row=row + 1, column=column + 1, frame=allLab.create())
window.addFrame(row=row + 1, column=column + 2, frame=Arrows.createArrows())
window.addFrame(row=row + 1, column=column + 3, frame=allEnt.create())
window.addFrame(row=row + 2, column=column + 1, frame=entryFrame.createEntry(70, 20))
window.addFrame(row=row + 3, column=column + 1, frame=mainBtn.create(), columnspan=5)
window.addFrame(row=row + 4, column=column + 1, frame=entryFrame.createEntry(70, 20))
window.addFrame(row=row + 5, column=column + 1, frame=table.create(), columnspan=5)
window.showWindow()
