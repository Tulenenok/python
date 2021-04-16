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
    def invalidList(list):
        if list == '':
            messagebox.showinfo('Error', 'Вы не ввели массив')
            return False

        list = list.split()
        for number in list:
            if not Errors.__checkNumber(number):
                messagebox.showinfo('Error', 'Вы некорректно ввели массив')
                return False
        return True