from tkinter import *
from fiveSystem.fiveSystem import txt, getAnswer

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