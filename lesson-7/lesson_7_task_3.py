# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать
# параметр, соответствующий количеству ячеек клетки (целое число). В классе
# должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление
# клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
# разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр
# класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки
# по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество
# ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда
# метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
from functools import wraps


def check_type(function):
    @wraps(function)
    def wrapper(obj_1, obj_2):
        if type(obj_1) != type(obj_2):
            raise AttributeError('attributes have different types')
        return function(obj_1, obj_2)

    return wrapper


class Cell:
    def __init__(self, point_count):
        point_count = int(point_count)
        if point_count < 0:
            raise AttributeError('should be positive number')
        self.__point_count = point_count

    @check_type
    def __add__(self, other):
        return Cell(self.__point_count + other.__point_count)

    @check_type
    def __sub__(self, other):
        sub = self.__point_count - other.__point_count
        if sub <= 0:
            raise ArithmeticError('can not sub: first cell less than second')
        return Cell(sub)

    @check_type
    def __mul__(self, other):
        mul = self.__point_count * other.__point_count
        return Cell(mul)

    @check_type
    def __truediv__(self, other):
        truediv = self.__point_count // other.__point_count
        return Cell(truediv)

    def make_order(self, points_in_row):
        rows = []

        full_row_count = self.__point_count // points_in_row
        if full_row_count > 0:
            full_row = '*' * points_in_row
            full_rows = [full_row] * full_row_count
            rows.extend(full_rows)

        rest_points = self.__point_count % points_in_row
        if rest_points > 0:
            rest_row = '*' * rest_points
            rows.append(rest_row)

        return '\n'.join(rows)


if __name__ == '__main__':
    cell_1 = Cell(20)
    cell_2 = Cell(4)
    try:
        cell_2 - 1
    except AttributeError as e:
        print(e)
    print('add: ', (cell_1 + cell_2).make_order(5), sep='\n')
    print('sub: ', (cell_1 - cell_2).make_order(5), sep='\n')
    try:
        cell_2 - cell_1
    except ArithmeticError as e:
        print(e)
    print('mul: ', (cell_1 * cell_2).make_order(5), sep='\n')
    print('truediv: ', (cell_1 / cell_2).make_order(5), sep='\n')
