''' Осуществляет проверки перед переводом чисел '''

class fiveSysErrors:

    @staticmethod                             # Проверяет, что число является числом
    def checkNumber(number):
        if number.rfind('-') not in [0, -1] or number in ['.', '-'] or number=='': return False
        if number.count('.') not in [0, 1] or '-.' in number: return False
        for elem in number:
            if elem not in '0123456789.-':
                return False
        return True

    @staticmethod
    def checkFiveNumber(number):          # Проверяет, что число является числом в 5 системе
        if fiveSysErrors.checkNumber(number):
            for elem in number:
                if elem != '.' and elem != '-' and int(elem) > 4:
                    return False
            return True
        return False