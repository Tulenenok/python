from tkinter import *
from tkinter import messagebox
from sortResearch import sortModel
from tkinter import ttk

class Window:
    def __init__(self):
        self.name = 'Исследование сортировок'
        self.size = '1050x300'

    def createWindow(self):
        self.window = Tk()
        self.window.title(self.name)
        self.window.geometry(self.size)

    def addMenu(self):
        self.window.config(menu=menu.createMenu())

    def addFrame(self, row, column, frame, columnspan=1):
        frame.grid(row=row, column=column, columnspan=columnspan)

    def showWindow(self):
        self.window.mainloop()

class List:
    def __init__(self):
        self.listFrame = Frame()
        self.allLists = []

    def oneInputList(self, frame):

        oneListFrame = Frame(frame)
        label = Label(oneListFrame, text='', font=('Consolas', 11))
        oneList = Entry(oneListFrame, width=110)
        label.grid(row=1, column=0)
        oneList.grid(row=1, column=1)

        self.allLists.append(oneList)
        return oneListFrame

    def createInputList(self):
        inputN1 = self.oneInputList(self.listFrame)
        inputN2 = self.oneInputList(self.listFrame)
        inputN3 = self.oneInputList(self.listFrame)

        inputN1.grid(row=1, column=0)
        inputN2.grid(row=2, column=0)
        inputN3.grid(row=3, column=0)

        return self.listFrame

    def clear(self, i):
        self.allLists[i].delete(0, last=END)

    def random(self, numberList):
        try:
            sizeList = size.allSize[numberList].get()
            randomList = sortModel.makeRandomList(int(sizeList))
            self.allLists[numberList].delete(0, last=END)
            self.allLists[numberList].insert(0, randomList)
        except:
            messagebox.showinfo('Error', 'Вы не ввели размер массива')

    def updateList(self, numberList):
        self.newList = sortModel.simpleSort([float(i) for i in self.allLists[numberList].get().split()])
        self.newStr = ' '.join([str(i) for i in self.newList])
        self.allLists[numberList].delete(0, last=END)
        self.allLists[numberList].insert(0, self.newStr)

class sizeList:
    def __init__(self):
        self.sizeFrame = Frame()
        self.allSize = []

    def oneInputSize(self, text, frame):

        inputSizeFrame = Frame(frame)
        label = Label(inputSizeFrame, text=text, font=('Consolas', 11))
        size = Entry(inputSizeFrame, width=12)
        label.grid(row=1, column=0)
        size.grid(row=1, column=1)

        self.allSize.append(size)
        return inputSizeFrame

    def createInputSize(self):
        inputN1 = self.oneInputSize(' N1: ', self.sizeFrame)
        inputN2 = self.oneInputSize(' N2: ', self.sizeFrame)
        inputN3 = self.oneInputSize(' N3: ', self.sizeFrame)

        inputN1.grid(row=1, column=0)
        inputN2.grid(row=2, column=0)
        inputN3.grid(row=3, column=0)

        return self.sizeFrame

    def clear(self, i):
        self.allSize[i].delete(0, last=END)

class basicButton:
    def __init__(self, name, param):
        self.btnFrame = Frame()

        self.firstBtn = Button(self.btnFrame, text=name, font=('Consolas', 9), command=lambda: self.click(0, param))
        self.secondBtn = Button(self.btnFrame, text=name, font=('Consolas', 9), command=lambda: self.click(1, param))
        self.thirdBtn = Button(self.btnFrame, text=name, font=('Consolas', 9), command=lambda: self.click(2, param))

        self.allButtons = [self.firstBtn, self.secondBtn, self.thirdBtn]

    def createButton(self):
        for row, btn in enumerate(self.allButtons):
            btn.grid(row=row, column=0)
        return self.btnFrame


    # param 0 - удалить содержимое
    # param 1 - сгенирить рандомную последовательность
    def click(self, numberList, param):
        if param == 0:
            lst.clear(numberList)
            size.clear(numberList)
        else:
            lst.random(numberList)

class SortButton:
    @staticmethod
    def createSortBtn():
        btnFrame = Frame()
        sortButton = Button(btnFrame, text='Conduct research', font=('Consolas', 14),
                            padx=38, pady=10, command=table.updateTable)
        sortButton.grid(row=2, column=2)
        return btnFrame

class Arrows:
    @staticmethod
    def createArrows():
        arrowsFrame = Frame()
        for i in range(1, 4):
            arrow = Label(arrowsFrame, text='  >>>  ', font=('Consolas', 11))
            arrow.grid(row=i, column=1)
        return arrowsFrame

class Table:
    def __init__(self):
        ttk.Style().configure('Treeview', rowheight=30, columnweight=1000)
        self.heads = ['', 'N1', 'N2', 'N3']
        self.listTable = []
        self.table = ttk.Treeview(show='headings',  height=3)
        self.values = [['Случайный', '', '', ''], ['Упорядоченный', '', '', ''], ['Обратный', '', '', '']]

    def createTable(self):
        del self.table
        self.table = ttk.Treeview(show='headings', height=3)
        self.table['columns'] = self.heads
        for header in self.heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, anchor='center')

        for row in self.values:
            self.table.insert('', 'end', values=row)
        return self.table

    def updateTable(self):
        for number, list in enumerate(lst.allLists):
            resultList = sortModel.researchList(list.get())
            for row in range(len(self.values)):
                self.values[row][number + 1] = resultList[number]
            lst.updateList(number)
        window.addFrame(4, 1, table.createTable(), 3)

class entryFrame:
    @staticmethod
    def createEntry(row, column):
        entry = Frame(width=row, height=column)
        return entry

class menuFrame:
    def __init__(self):
        self.menu = Menu()

    def __makeDropDown(self, menu, dictLabels):
        newItem = Menu(self.menu, tearoff=0)
        for item in dictLabels:
            newItem.add_command(label=item, command=lambda: dictLabels[item]())
        return newItem

    def createMenu(self):
        # self.menu.add_cascade(label='Random', menu=self.__makeDropDown(self.menu, {'Random 1': lst.random(1),
        #                                                                            'Random 2': lst.random(2),
        #                                                                            'Random 3': lst.random(3)}))
        self.menu.add_cascade(label='Info', menu=self.__makeDropDown(self.menu, {'Информация об авторе': self.__info}))
        return self.menu

    def __info(self):
        messagebox.showinfo('Info', 'Программа была создана 09.03.21. \n Автор: Гурова Наталия ИУ7-24Б')

window = Window()
window.createWindow()

menu = menuFrame()
window.addMenu()
size = sizeList()
lst = List()

randomButton = basicButton('random', 1)
clearButton = basicButton('clear', 0)
table = Table()

window.addFrame(0, 0, size.createInputSize())
window.addFrame(0, 1, Arrows.createArrows())
window.addFrame(0, 2, lst.createInputList())
window.addFrame(0, 3, Arrows.createArrows())
window.addFrame(0, 4, randomButton.createButton())
window.addFrame(0, 5, clearButton.createButton())
window.addFrame(1, 0, entryFrame.createEntry(10, 7), 5)
window.addFrame(2, 2, SortButton.createSortBtn())
window.addFrame(3, 0, entryFrame.createEntry(10, 15), 5)
window.addFrame(4, 1, table.createTable(), 3)

window.showWindow()