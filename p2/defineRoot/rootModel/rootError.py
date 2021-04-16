from tkinter import messagebox

class Errors:
    @staticmethod
    def __checkNumber(number):
        if number.rfind('-') not in [0, -1] or number in ['.', '-'] or number == '': return False
        if number.count('.') not in [0, 1] or '-.' in number: return False
        for elem in number:
            if elem not in '0123456789.-':
                return False
        return True

    @staticmethod
    def __isFloat(number):
        try:
            number = float(number)
            return True
        except:
            return False

    @staticmethod
    def invalidList(list):
        listCol = {0: 'начало', 1: 'конец', 2: 'шаг', 3: 'точность', 4: 'количество итераций'}
        if list == ['', '', '', '', '']:
            messagebox.showinfo('Error', 'Вы не ввели данные')
            return False

        for i, number in enumerate(list):
            if i not in [3, 4] and not Errors.__isFloat(number):
                messagebox.showinfo('Error', f'Вы некорректно ввели {listCol[i]}')
                return False
            if i in [3, 4] and (not Errors.__isFloat(number) or float(number) <= 0):
                messagebox.showinfo('Error', f'Вы некорректно ввели {listCol[i]}')
                return False

        if float(list[0]) < float(list[1]) and float(list[2]) <= 0:
            messagebox.showinfo('Error', 'Отрицательный шаг при левой границе меньшей правой')
            return False
        elif float(list[0]) > float(list[1]) and float(list[2]) >= 0:
            messagebox.showinfo('Error', 'Положительный шаг при левой границе большей правой')
            return False
        elif float(list[0]) == float(list[1]):
            messagebox.showinfo('Error', 'Начало и конец отрезка совпадают')
            return False
        elif float(list[2]) == 0:
            messagebox.showinfo('Error', 'Шаг равен 0')
            return False

        if (float(list[3]) > 0.01):
            messagebox.showinfo('Error', 'Слишком большая точность')
            return False
        return True