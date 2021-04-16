from tkinter import *
from tkinter import messagebox
from fiveSystem.fiveSysControl import Controller

# Руководит процессом перевода чисел
def getAnswer():
    number = txt.get()
    answer = Controller.mainController(param, number)
    if answer == '!':
        messagebox.showinfo('Ошибка', 'Ваш ввод некорректен')
        answerLabel.configure(text='')
    else:
        answerLabel.configure(text = f'{answer}')

# Делает кнопку с цифрой
def buttonNumber(number, col, row, frame):
    btn = Button(frame, text=number, padx=25, pady=11, font=('Consolas', 16),
                 command=lambda: txt.insert(len(txt.get()), str(number)))
    btn.grid(column=col, row=row)


# Делает клавиатуру с циферками
def frameButtons():
    buttonFrame = Frame()
    for i in range(3):
        for j in range(3):
            buttonNumber(i * 3 + j + 1, j, i, buttonFrame)
    buttonNumber('-', 0, 3, buttonFrame)
    buttonNumber('0', 1, 3, buttonFrame)
    buttonNumber('.', 2, 3, buttonFrame)
    return buttonFrame

# Делает кнопку ответ
def answerButton():
    return Button(text='Ответ', font=('Consolas', 16), command=getAnswer)

# Делает выпадающий список для меню
def makeDropDown(menu, dictLabels):
    newItem = Menu(menu, tearoff = 0)
    for item in dictLabels:
        newItem.add_command(label=item, command=lambda: dictLabels[item]())
    return newItem

# Делает меню
def makeMenu():
    menu = Menu(window)
    menu.add_cascade(label='Рeжим', menu=makeDropDown(menu, {'10 -> 5': changeSS, '5 -> 10': changeSS}))
    menu.add_cascade(label='Очистка', menu=makeDropDown(menu, {'Поле ввода': clearInput, 'Всё': clearAll}))
    menu.add_cascade(label='Info', menu=makeDropDown(menu, {'Информация об авторе': info}))
    return menu

def changeSS():
    global param, inputSystem, outputSystem, inputLabel, outputLabel

    param = int(not param)
    inputSystem = 5 if inputSystem == 10 else 10
    outputSystem = 10 if outputSystem == 5 else 5

    txt.delete(0, last=END)
    answerLabel.configure(text='')
    inputLabel.configure(text=f'{inputSystem} СС: ')
    outputLabel.configure(text=f'{outputSystem} CC:')

def change10to5():
    global param, inputSystem, outputSystem, inputLabel, outputLabel
    param = 0
    inputSystem = 10
    outputSystem = 5
    txt.delete(0, last=END)
    answerLabel.configure(text='')
    inputLabel.configure(text=f'{inputSystem} СС: ')
    outputLabel.configure(text=f'{outputSystem} CC:')

def change5to10():
    global param, inputSystem, outputSystem, inputLabel, outputLabel
    param = 1
    inputSystem = 5
    outputSystem = 10
    txt.delete(0, last=END)
    answerLabel.configure(text='')
    inputLabel.configure(text=f'{inputSystem} СС: ')
    outputLabel.configure(text=f'{outputSystem} CC:')

def clearInput():
    txt.delete(0, last=END)

def clearAll():
    clearInput()
    answerLabel.configure(text=' ')

def info():
    messagebox.showinfo('Info', 'Программа была создана 16.02.21. \n Автор: Гурова Наталия ИУ7-24Б')

def inputFrame(system = 10):
    global txt, inputLabel
    inputF = Frame()
    inputLabel = Label(inputF, text=f'{inputSystem} СС: ', font=('Consolas', 11))
    inputLabel.grid(column=0, row=0)
    txt = Entry(inputF, width=25)
    txt.grid(column=1, row=0)
    return inputF

def outFrame():
    global outputLabel, answerLabel
    outputF = Frame()
    outputLabel = Label(outputF, text=f'{outputSystem} CC:', font=('Consolas', 11))
    outputLabel.grid(column=0, row=0)
    answerLabel = Label(outputF, text='', font=('Consolas', 11))
    answerLabel.grid(column=1, row=0)
    return outputF

def delOneSim():
    number = txt.get()
    txt.delete(0, last=END)
    txt.insert(0, number[:len(number)-1])

def clearFrame():
    clearF = Frame()
    delF = Button(clearF, text='del', font=('Consolas', 11), padx=3, pady=2, command=delOneSim)
    clearFr = Button(clearF, text='clear', font=('Consolas', 11), padx=5, pady=2, command=clearAll)
    delF.grid(row=0, column=0)
    clearFr.grid(row=0, column=1)
    return clearF

def reverseButton():
    reverseFrame = Frame()
    reverseB = Button(reverseFrame, text='reverse', font=('Consolas', 11), padx=18, pady=2, command=changeSS)
    reverseB.grid(row=0, column=0)
    return reverseFrame

param = 0                       # Режим, в котором считать (0 - из 10 в 5, 1 - из 5 в 10)
inputSystem = 10
outputSystem = 5

window = Tk()
window.title('Конвертер систем счисления')
window.geometry('334x315')

window.config(menu=makeMenu())                                      # Создали меню
inputFrame().grid(column=0, row=0, sticky=W+E)                      # Создали поле ввода
clearFrame().grid(column=1, row=0)                                  # Создали кнопки для очистки
outFrame().grid(column=0, row=1, sticky=W+E)                        # Создали поле вывода
reverseButton().grid(column=1, row=1, sticky='nwse')
frameButtons().grid(column=0, row=2, sticky=W+E)                    # Создали клавиатуру с цифрами
answerButton().grid(column=1, row=2, sticky='nwse')                 # Создали кнопку "ответ"

window.mainloop()