# 4, 5, 6 - маленький проект
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым для
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определить параметры, общие для
# приведенных типов. В классах-наследниках реализовать параметры, уникальные
# для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за
# приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например
# словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
# Подсказка ValueError

# todo: modeling
# todo: document
# todo: split to files
# todo: test
# todo: check variables
# * https://docs.python.org/3/library/typing.html
# * https://askdev.ru/q/luchshiy-sposob-proverit-argumenty-funkcii-v-python-zakryt-77673/
# * best way to check arguments in python
# * https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments/
#   * duck-typing
#   * analyze docs
#   * entry point
#   * bear typing https://pypi.org/project/beartype/
# * https://realpython.com/python-type-checking/
#   * Enforce, 511
#   * Pydantic, 6430 https://pydantic-docs.helpmanual.io/usage/validation_decorator/
#   * or Pytypes 152
import json
from abc import abstractmethod
from pydantic import validate_arguments, BaseModel
from typing import Dict, List, Type, TypeVar


class Department:
    @abstractmethod
    def give_back(self, office_equipment, amount): pass

    @abstractmethod
    def take(self, office_equipments): pass


# todo: abstract
class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


TOfficeEquipment = TypeVar("TOfficeEquipment", bound="OfficeEquipment")


class Warehouse:
    # office_equipments: Dict[str, List[OfficeEquipment]] = dict()
    office_equipments = dict()

    @staticmethod
    @validate_arguments()
    def get_office_equipment_title(brand: str, model: str) -> str:
        return f'{brand}, {model}'

    @validate_arguments()
    def load(self, office_equipment: TOfficeEquipment, amount: int) -> None:
        title = self.get_office_equipment_title(office_equipment.brand, office_equipment.model)
        office_equipments = self.office_equipments.get(title, [])
        new_office_equipments = [office_equipment] * amount
        office_equipments.extend(new_office_equipments)
        self.office_equipments[title] = office_equipments

    @validate_arguments()
    def unload(self, office_equipment_title: str, amount: int, department) -> None:
        office_equipments = self.office_equipments.get(office_equipment_title, [])
        if amount > len(office_equipments):
            raise AttributeError('more than present')
        unloaded = office_equipments[:amount]
        department.take(unloaded)

        rest = office_equipments[amount:]
        if len(rest) == 0:
            del self.office_equipments[office_equipment_title]
        else:
            self.office_equipments[office_equipment_title] = office_equipments[amount:]

    @validate_arguments()
    def report(self):
        report = {title: len(wares) for title, wares in self.office_equipments.items()}
        print(json.dumps(report, indent=4))


class Printer(OfficeEquipment):
    @validate_arguments()
    def __init__(self, brand: str, model: str, price: str, printing_technology: str):
        super().__init__(brand, model, price)
        self.printing_technology = printing_technology
        # super().__init__(brand, model, price)


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, resolution):
        super().__init__(brand, model, price)
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, brand, model, price, resolution, printing_technology):
        super().__init__(brand, model, price)
        self.resolution = resolution
        self.printing_technology = printing_technology


# class Department:
#     @abstractmethod
#     def give_back(self, office_equipment, amount): pass
#
#     @abstractmethod
#     def take(self, office_equipments): pass


class ItDepartment(Department):
    def give_back(self, office_equipment, amount): pass

    def take(self, office_equipments):
        print(f'IT Department takes {len(office_equipments)}')


track = [
    Printer("HP", "J9V90A#B1H", "$74.95", "inkjet"),
    Scanner("Fujitsu", "ScanSnap iX1600", "$399.99", 600),
    Scanner("Brother", "Duplex Compact", "$129.98", 300),
    Copier("Pantum", "M6802FDW-V1X47B", "$129.98", 300, "laser")
]

warehouse = Warehouse()
warehouse.report()

for ware in track:
    warehouse.load(ware, 1)  # todo 1?
warehouse.report()

title = warehouse.get_office_equipment_title("HP", "J9V90A#B1H")
it_department = ItDepartment()
warehouse.unload(title, 1, it_department)
warehouse.report()
