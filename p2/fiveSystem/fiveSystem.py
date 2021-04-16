''' Перевод заданного вещественного числа из 10-тичной в 5-ю и обратно '''

class fiveSystem:

    @staticmethod        # Делит вещественное число на целую и дробную часть (принимает строку!)
    def parseFloat(number):
        return number.split('.')[0], '0.' + number.split('.')[1]

    @staticmethod      # Функция переводит целое положительное число из 10 системы в 5 (принимает строку!)
    def intDecFive(number):
        ans = '' if number != '0' else '0'
        number = int(number)
        while number != 0:
            ans += str(number % 5)
            number //= 5
        return ans[::-1]

    @staticmethod       # Переводит дробную часть числа из 10 в 5 (принимает строку в виде 0.kjn)
    # precision - точность (количество знаков после .)
    def fracDecFive(number, precision):
        number = float(number)
        ans = ''
        while number != 0 and len(ans) != precision:
            number *= 5
            ans += str(int(number))
            number -= int(number)
        return ans.rstrip('0')

    @staticmethod                    # Переводит целое число из 5 в 10 (принимает строку!)
    def intFiveDec(number):
        lenNumber = len(number)
        number = int(number)
        ans = 0
        for degree in range(lenNumber):
            ans += (number % 10) * 5 ** degree
            number //= 10
        return str(ans)                         # Возвращает строку

    @staticmethod       # Переводит дробную часть числа в виде 0.kjhb из 5 в 10 (принимает строку!)
    def fracFiveDec(number):
        number = number.replace('0.', '').rstrip('0')[::-1]
        if number == '': return 0
        lenNumber = len(number)
        number = int(number)
        ans = 0
        for degree in range(1, lenNumber + 1):
            ans += (number % 10) * 5 ** (-degree)
            number //= 10
        return ans

    @staticmethod          # Переводит вещественное число из 10 в 5 (принимает строку!)
    def floatDecFive(number, precision):
        intDecNum, fracDecNum = fiveSystem.parseFloat(number)              # Разделили число на дробную и целую часть
        intFiveNum = fiveSystem.intDecFive(intDecNum)                      # Перевели целое в 5 систему
        fracFiveNum = fiveSystem.fracDecFive(fracDecNum, precision)        # Переволи дробную часть в 5 систему
        return (intFiveNum + '.' + fracFiveNum).rstrip('.')                 # Возврашает строку

    @staticmethod           # Переводит вещественное число из 5 в 10 (принимает строку!)
    def floatFiveDec(number):
        intFiveNum, fracFiveNum = fiveSystem.parseFloat(number)        # Разделили число на дробную и целую часть
        intDecNum = int(fiveSystem.intFiveDec(intFiveNum))             # Перевели целую
        fracDecNum = fiveSystem.fracFiveDec(fracFiveNum)               # Перевели дробную
        return str(intDecNum + fracDecNum)                             # Возврашает строку

    @staticmethod               # Переводит число из 10 в 5 (принимает и возвращает строку)
    def DecFive(number, prec = 5):
        if number.startswith('.'): number = '0' + number
        if number.endswith('.'): number = number.strip('.')
        if number[0] == '-':
            ans = '-'
            ans += fiveSystem.floatDecFive(number[1:], prec) if number.find('.') != -1 else fiveSystem.intDecFive(number[1:])
        else:
            ans = fiveSystem.floatDecFive(number, prec) if number.find('.') != -1 else fiveSystem.intDecFive(number)
            ans = str(round(float(ans), prec))
        return ans if abs(float(ans)) != 0 else '0.0'

    @staticmethod               # Переводит число из 5 в 10 (принимает и возвращает строку)
    def FiveDec(number, precision = 5):
        if number.startswith('.'): number = '0' + number
        if number.endswith('.'): number = number.strip('.')
        if number[0] == '-':
            ans = '-'
            ans += fiveSystem.floatFiveDec(number[1:]) if number.find('.') != -1 else fiveSystem.intFiveDec(number[1:])
        else:
            ans = fiveSystem.floatFiveDec(number) if number.find('.') != -1 else fiveSystem.intFiveDec(number)
            ans = str(round(float(ans), precision))
        return ans if abs(float(ans)) != 0 else '0.0'



