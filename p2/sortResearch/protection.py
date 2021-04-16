from tkinter import *
# Пузырьковая сортировка с флагом
def bubbleSortWithFlag(list, index):
    for i in range(len(list) - 1):
        flag = False
        for j in range(len(list) - 1 - i):
            if list[j][index] > list[j + 1][index]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = True
        if not flag:
            break
    return list

def sortList(list):
    list = bubbleSortWithFlag(list, 1)
    list = bubbleSortWithFlag(list, 0)
    return list

def get_text():
    newText = text.get(1.0, END)
    return newText.split()

def controll():
    listWords = get_text()
    newList = []
    for i in range(0, len(listWords), 2):
        newList.append((int(listWords[i]), listWords[i+1]))
    newList = sortList(newList)
    outFrame= output(newList)
    outFrame.grid(row=0, column=1, sticky=N)

def output(list):
    outFrame = Frame()
    for j, i in enumerate(list):
        newLabel = Label(outFrame, text=f'{i[0]} {i[1]}')
        newLabel.grid(row=j, column=0)
    return outFrame



window = Tk()
window.geometry('260x220')
text = Text(width = 20, height = 10)
button = Button(text='Sort', command=controll, padx=10, pady=10)

text.grid(row=0, column=0)
button.grid(row=1, column=0, rowspan=2)
window.mainloop()