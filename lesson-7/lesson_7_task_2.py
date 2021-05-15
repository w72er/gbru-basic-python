# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod, abstractproperty


class Clothes(ABC):
    # @property  # не обязывает наличие у потомка геттера
    # @abstractproperty  # не обязывает наличие у потомка геттера
    # тогда в чем смысл такого абстрактного класса, если мы не можем
    # единообразно обрабатывать объекты
    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property  # хуже того мы теряем совместимость с cloth_consumption() интерфейса
    def cloth_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cloth_consumption(self):
        return 2 * self.h + 0.3


if __name__ == '__main__':
    clothes = [Coat(6.5), Costume(1)]
    total_cloth_consumption = sum(map(lambda c: c.cloth_consumption, clothes))
    print(total_cloth_consumption)
