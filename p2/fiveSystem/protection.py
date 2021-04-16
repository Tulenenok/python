from tkinter import *

def conversion(number1, number2):
    if len(number1) > len(number2):
        number2 = '0' * (len(number1) - len(number2)) + number2
    else:
        number1 = '0' * (len(number2) - len(number1)) + number1

    ans = ''
    byf = 0
    while number1 != '':
        last1 = int(number1[-1])
        last2 = int(number2[-1])
        ans += str((last1 + last2 + byf) % 4)
        byf = (last1 + last2 + byf) // 4
        number1 = number1[:len(number1) - 1]
        number2 = number2[:len(number2) - 1]
    ans = ans + str(byf) if byf != 0 else ans
    return ans[::-1]

def inputFrame(num):
    global inputTxt
    inputF = Frame()
    inputLabel = Label(inputF, text=f'{num} число: ', font = ('Consolas', 12))
    inputLabel.grid(column=0, row=0)
    inputTxt = Entry(inputF, width=25)
    inputTxt.grid(column=1, row=0)
    return inputF

def calculate():
    number1 = inputTxt1.get()
    number2 = inputTxt2.get()
    ans = conversion(number1, number2)
    outputLabrel.configure(text=f'Ответ: {ans}')


window = Tk()
window.title('Сложение в 4 системе')
window.geometry('300x300')

inputF1 = Frame()
inputLabel1 = Label(inputF1, text='Первое число: ', font = ('Consolas', 12))
inputLabel1.grid(column=0, row=0)
inputTxt1 = Entry(inputF1, width=25)
inputTxt1.grid(column=1, row=0)

inputF1.grid(column=0, row=0)

inputF2 = Frame()
inputLabel2 = Label(inputF2, text='Второе число: ', font = ('Consolas', 12))
inputLabel2.grid(column=0, row=0)
inputTxt2 = Entry(inputF2, width=25)
inputTxt2.grid(column=1, row=0)

inputF2.grid(column=0, row=1)

outputLabrel = Label(text='Ответ:', font=('Consolas', 12))
outputLabrel.grid(column=0, row=2, sticky=W)

buttonAns = Button(text='Посчитать', font=('Consolas', 11), padx=18, pady=2, command=calculate)
buttonAns.grid(column=0, row=3)

window.mainloop()

