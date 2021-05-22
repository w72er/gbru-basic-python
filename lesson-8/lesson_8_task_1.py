# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    delimiter = '-'

    def __init__(self, date):
        """
        Creates date
        :param date: as string in format "<day>-<month>-<year>
        """
        numbers = self.parse(date)
        self.validate(numbers)
        self.day, self.month, self.year = numbers

    @classmethod
    def parse(cls, date):
        string_numbers = date.split(cls.delimiter)
        numbers = map(lambda string: int(string), string_numbers)
        return list(numbers)

    @staticmethod
    def validate(numbers):
        if type(numbers) and len(numbers) != 3:
            raise AttributeError("numbers must be a list with 3 numbers (day, month, year)")

        day, month = numbers[:2]
        if not 1 <= day <= 31:
            raise AttributeError(f"day {day} is not between [1 - 31]")
        if not 1 <= month <= 12:
            raise AttributeError(f"month {month} is not between [1 - 12]")


Date("20-05-2021")
# Date("0-05-2021")
Date("20-05-2021-")
Date("20-05-2021-2")



