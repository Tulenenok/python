from fiveSystem.fiveSystem import fiveSystem
from fiveSystem.fiveSysErrors import fiveSysErrors

class Controller:

    @staticmethod               # Переводит в обе стороны в зависимости от параметра
    # param = 0 - перевести из 10 в 5
    # param = 1 - перевести из 5 в 10
    def conversion(param, number, precision = 5):
        if param == 0:
            return fiveSystem.DecFive(number, precision)
        else:
            return fiveSystem.FiveDec(number)

    @staticmethod
    def mainController(param, number, precision = 5):
        if number.count('+') > 1: return '!'
        number = number.lstrip('+')
        if param == 1 and not fiveSysErrors.checkFiveNumber(number) or not fiveSysErrors.checkNumber(number):
            return '!'
        return Controller.conversion(param, number, precision)
