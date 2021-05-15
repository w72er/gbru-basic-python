# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.
# Подсказка: сложить матрицы можно лишь одинаковые по размеру
# [строка][столбец]

# str_elements = map(lambda row: map(lambda el: str(el), row), self.matrix)  # почему реализация не через цепочку:
# list.map().map().filter()?

# можно ли выносить так функцию ради читабельности?
def make_elements_strings(elements):
    return map(lambda element: str(element), elements)


class Matrix:
    def __init__(self, matrix):
        rows_count = len(matrix)
        columns_count = len(matrix[0]) if rows_count > 0 else 0
        if columns_count > 0:
            for row in matrix[1:]:
                if len(row) != columns_count:
                    raise AttributeError('Different amount of columns in rows')

        self.rows_count = rows_count
        self.columns_count = columns_count
        self.matrix = matrix

    def __str__(self):
        str_elements = map(make_elements_strings, self.matrix)
        str_rows = map(lambda row: ' '.join(row), str_elements)
        return '\n'.join(str_rows)

    def __add__(self, other):
        if self.columns_count != other.columns_count or self.rows_count != other.rows_count:
            raise AttributeError('operation under different dimensions matrix')

        sum_matrix = []
        for r in range(self.rows_count):
            row = []
            for c in range(self.columns_count):
                row.append(self.matrix[r][c] + other.matrix[r][c])
            sum_matrix.append(row)
        return Matrix(sum_matrix)


m_1 = Matrix([[31, 22], [37, 43], [51, 86]])
m_2 = Matrix([[3, 5], [2, 4], [-1, 64]])
print('matrix 1:')
print(m_1)
print('matrix 2:')
print(m_2)
print('matrix 1 + matrix 2:')
print(m_1 + m_2)

