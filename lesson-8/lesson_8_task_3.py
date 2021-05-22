# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном
# примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду
# “stop”. При этом скрипт завершается, сформированный список выводится на
# экран.
# Подсказка: для данного задания примем, что пользователь может вводить только
# числа и строки. При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести текст
# (не число) и отобразить соответствующее сообщение. При этом работа скрипта не
# должна завершаться.
class NotNumberError(Exception):
    def __init__(self, message):
        self.message = message


def is_int(string):
    string = string.lstrip("-")
    return string.isnumeric()


def is_float(string):
    string = string.lstrip("-")
    decimal_point = '.'
    return string.count(decimal_point) == 1 and string.replace(decimal_point, '', 1).isnumeric()


def get_number(str_number):
    if is_int(str_number):
        return int(str_number)

    if is_float(str_number):
        return float(str_number)

    raise NotNumberError(f"The argument ({str_number}) is not a number")


if __name__ == '__main__':
    numbers = []
    while True:
        string = input("Enter number or 'stop' to exit: ")

        if string == 'stop':
            print(*numbers)
            exit(0)

        try:
            number = get_number(string)
        except NotNumberError as err:
            print(err)
        else:
            numbers.append(number)
