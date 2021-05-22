# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# 1 занятие
# j**2 = -1
# (1+2j) + (3 + 4j) = 4 + 6j
# (1+2j) * (3 + 4j) = 1*3 + 1*4j + 2j*3 + 2j*4j, т.к. j*j = -1!!! 3 + 4j + 6j - 8 = -5 + 10j
# Проверяется перегрузка, а не реализация комплексных чисел, поэтому можно
# использовать комплексные числа на вход.

class Complex:
    def __init__(self, real, imaginary):
        """
        complex(real=0, imaginary=0)
        Create a complex number from a real part and an optional imaginary part.
        This is equivalent to (real + imaginary*1j) where imaginary defaults to 0.

        :param real: the real part of a complex number
        :param imaginary: the imaginary part of a complex number
        """
        self.__complex = complex(real, imaginary)

    def __add__(self, other):
        result = self.__complex + other.__complex
        return Complex(result.real, result.imag)

    def __mul__(self, other):
        result = self.__complex * other.__complex
        return Complex(result.real, result.imag)

    def __str__(self):
        return f'{str(self.__complex)}'

    @property
    def real(self):
        return self.__complex.real

    @property
    def imaginary(self):
        return self.__complex.imag


if __name__ == '__main__':
    add_result = Complex(1, 2) + Complex(3, 4)
    assert add_result.real == 4 and add_result.imaginary == 6, "(1 + 2j) + (3 + 4j) = 4 + 6j"

    mul_result = Complex(1, 2) * Complex(3, 4)
    assert mul_result.real == -5 and mul_result.imaginary == 10, "(1 + 2j) * (3 + 4j) = -5 + 10j"

    print("The tests have been passed successfully")
