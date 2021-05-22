# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionByZeroError(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    a = float(input('Enter number a: '))
    b = float(input('Enter number b: '))

    try:
        if b == 0:
            raise DivisionByZeroError("b is zero")
    except DivisionByZeroError as error:
        print(error)
        exit(0)

    c = a / b
    print(f"{a} / {b} = {c}")
