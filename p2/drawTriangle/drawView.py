from tkinter import *
from tkinter.messagebox import *
from drawTriangle.drawErrors import Check
from drawTriangle.drawControll import controll

class Window:
    def __init__(self, name, size, color):
        self.__name = name
        self.__size = size
        self.__color = color
        self.create()

    def create(self):
        self.__window = Tk()
        self.__window.title(self.__name)
        self.__window.geometry(self.__size)
        self.__window['bg'] = self.__color

    def addFrame(self, row, column, frame, columnspan=1, rowspan=1, sticky='NWSE'):
        frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def addMenu(self):
        self.__window.config(menu=menu.create())

    def showWindow(self):
        self.__window.mainloop()

class menuFrame:
    def __init__(self):
        self.__menu = Menu()

    def __makeDropDown(self, dictLabels):
        newItem = Menu(self.__menu, tearoff=0)
        for item in dictLabels:
            newItem.add_command(label=item, command=lambda: dictLabels[item]())
        return newItem

    def create(self):
        self.__menu.add_cascade(label='Info', menu=self.__makeDropDown({'Информация об авторе': self.__info}))
        return self.__menu

    def __info(self):
        showinfo('Info', 'Программа была создана 16.04.21. \n Автор: Гурова Наталия ИУ7-24Б')

class entryFrame:
    @staticmethod
    def create(row, column, color):
        entry = Frame(width=row, height=column, bg=color)
        return entry

class TextArea:
    def __init__(self, width, height, bg, fg):
        self.__frame = Frame()
        self.__text = Text(self.__frame, width=width, height=height, bg=bg, fg=fg, wrap=WORD,
                           font=('Verdana', 13), insertbackground="white")
        self.__text.grid(row=0, column=0)

    def create(self):
        return self.__frame

    def insert(self, position, str):
        self.__text.insert(position, str)

    def get(self):
        return self.__text.get("1.0", "end-1c")

    def delete_all(self):
        self.__text.delete('1.0', 'end')
        self.__text.update()

    def delete(self):
        self.__text.delete('end-2c')
        self.__text.update()

    def update(self):
        coordPoints = self.__takePoints()
        field.delTriangle()
        if coordPoints == None:
            showinfo('Info', 'Точки введены некорректно. Проверьте, что количество координат четно '
                             'и что нет лишних символов.')
            return

        # Поставили на поле точки, которых не хватало
        for i in coordPoints:
            if i not in field.coords:
                field.createPoint(i[0], i[1])

        # Удаляем с поля точки, которых нет в форме
        i = 0
        while i < len(field.coords):
            if field.coords[i] not in coordPoints:
                field.delPoint(field.points[i])

                field.coords.pop(i)
                field.points.pop(i)
            else:
                i += 1

    def __takePoints(self):
        text = self.get()
        for i in text:
            if i not in '0123456789.;() ':
                return None
        points = self.parser(text)
        if len(points) % 2 == 1:
            return None
        points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
        return points

    # Он считает, что строка валидна, то есть лишних символов в ней нет!
    def parser(self, text):
        list = text.split(' ')
        points = []
        for i in list:
            i = i.split(';')
            for j in i:
                j = j.split('(')
                for k in j:
                    k = k.split(')')
                    for l in k:
                        if Check.isFloat(l):
                            points.append(float(l))
        return points

    def calculate(self):
        self.update()
        field.delTriangle()
        print(field.coords)
        minPoints = controll(field.coords)
        if minPoints == None:
            showinfo('Info', 'Треугольник не найден. Проверьте, сколько у вас уникальных точек.')
            return
        field.drawTriangle(minPoints, "#f4d75e")

class Keyboard:
    def __init__(self, padx, pady, txt, bg, fg):
        self.__padx = padx
        self.__pady = pady
        self.__txt = txt
        self.__bg = bg
        self.__fg = fg
        self.__frame = Frame(bg='#7c7b89')

    # Делает кнопку с цифрой
    def __buttonNumber(self, number, col, row, frame):
        btn = Button(frame, text=number, padx=self.__padx, pady=self.__pady, font=('Consolas', 16),
                     bg=self.__bg, fg=self.__fg,
                     command=lambda: self.__txt.insert(END, str(number)))
        btn.grid(column=col, row=row)

    # Делает клавиатуру с циферками
    def create(self):
        for i in range(3):
            for j in range(3):
                self.__buttonNumber(i * 3 + j + 1, j, i, self.__frame)
        self.__buttonNumber('(', 0, 3, self.__frame)
        self.__buttonNumber('0', 1, 3, self.__frame)
        self.__buttonNumber(')', 2, 3, self.__frame)
        self.__buttonNumber('.', 0, 4, self.__frame)
        self.__buttonNumber(' ', 1, 4, self.__frame)
        self.__buttonNumber(';', 2, 4, self.__frame)
        return self.__frame

class Field:
    def __init__(self, width, height, bg, step=50, gridColor='grey'):
        self.__width = width
        self.__heigh = height
        self.__step = step
        self.__gridColor = gridColor

        self.__frame = Frame(bg=bg)
        self.__c = Canvas(self.__frame, width=width, height=height, bg=bg)
        self.__c.grid(row=0, column=0, sticky='S')

        self.coords = []
        self.points = []

        self.lines = []

        self.__c.bind('<1>', lambda event: self.__click(event))
        self.__ownGrid()

    def __ownGrid(self):
        for i in range(0, self.__width, self.__step):
            self.__c.create_line(i, 0, i, self.__width, fill=self.__gridColor, width=2, dash=(2,2))
        for i in range(0, self.__heigh, self.__step):
            self.__c.create_line(0, i, self.__heigh + 50, i, fill=self.__gridColor, width=2, dash=(2, 2))

    def create(self):
        return self.__frame

    def __click(self, event):
        point = self.__c.create_oval(event.x - 4, event.y - 4, event.x + 4, event.y + 4,
                             fill='#8eb2ac', outline='#8eb2ac')
        input.insert(END, f'({event.x} {event.y})')

        self.points.append(point)

        self.coords.append((event.x, event.y))

    def createPoint(self, x, y):
        point = self.__c.create_oval(x - 4, y - 4, x + 4, y + 4,
                             fill='#8eb2ac', outline='#8eb2ac')
        self.points.append(point)

        self.coords.append((x, y))

    def delPoint(self, point):
        self.__c.delete(point)

    def drawTriangle(self, listPoints, color):
        l1 = self.__c.create_line(listPoints[0][0], listPoints[0][1], listPoints[1][0], listPoints[1][1],
                                  fill=color, width=3)
        l2 = self.__c.create_line(listPoints[0][0], listPoints[0][1], listPoints[2][0], listPoints[2][1],
                                  fill=color, width=3)
        l3 = self.__c.create_line(listPoints[1][0], listPoints[1][1],
                                  listPoints[2][0], listPoints[2][1],
                                  fill=color, width=3)
        self.lines.append(l1)
        self.lines.append(l2)
        self.lines.append(l3)

    def delTriangle(self):
        for i in self.lines:
            self.__c.delete(i)
        self.lines = []

class SpecialBtns:
    def __init__(self, txt, bg, fg, padx, pady, font=('Consolas, 14')):
        self.__txt = txt
        self.__bg = bg
        self.__fg = fg
        self.__padx = padx
        self.__pady = pady
        self.__font = font
        self.__frame = Frame(bg='#7c7b89')

    def __btn(self, text, command, row, column, sticky='NWSE'):
        btn = Button(self.__frame, text=text, padx=self.__padx, pady=self.__pady, font=self.__font,
                          bg=self.__bg, fg=self.__fg,
                          command=command)
        btn.grid(row=row, column=column, sticky=sticky)

    def create(self):
        self.__btn('clear', self.__txt.delete, 0, 0)
        self.__btn('clear all', self.__txt.delete_all, 0, 1)
        self.__btn('update', self.__txt.update, 0, 2)
        self.__btn('calculate', self.__txt.calculate, 0, 3)
        return self.__frame

window = Window('Triangle', '900x580', '#7c7b89')
menu = menuFrame()
input = TextArea(25, 8, "#f1e4de", "black")
keyboard = Keyboard(32.4, 16, input, "#f1e4de", "black")
field = Field(500, 450, "white")
specBtn = SpecialBtns(input, "#f1e4de", "black", 20, 5)
window.addMenu()
window.addFrame(row=0, column=0, frame=entryFrame.create(10, 20, '#7c7b89'), columnspan=5)
window.addFrame(row=0, column=0, frame=entryFrame.create(20, 10, '#7c7b89'), rowspan=5)
window.addFrame(row=1, column=1, frame=input.create())
window.addFrame(row=2, column=1, frame=entryFrame.create(10, 10, '#7c7b89'), columnspan=2)
window.addFrame(row=3, column=1, frame=keyboard.create())

window.addFrame(row=1, column=2, frame=entryFrame.create(50, 50, '#7c7b89'), rowspan=5)
window.addFrame(row=1, column=3, frame=field.create(), rowspan=5, sticky='S')

window.addFrame(row=1, column=3, frame=specBtn.create(), sticky='NW')
window.showWindow()

