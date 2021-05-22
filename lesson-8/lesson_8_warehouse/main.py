import json
from typing import List

from printer import Printer
from scanner import Scanner
from copier import Copier
from it_department import ItDepartment
from warehouse import Warehouse
from office_equipment import OfficeEquipment


class Dispatcher:
    __COMMAND_EXIT = "0"
    __COMMAND_ACCEPT_TRUCK = "1"
    __COMMAND_UNLOAD_TO_IT_DEPARTMENT = "2"
    __COMMAND_MAKE_REPORT = "3"

    def __init__(self):
        self.__warehouse = Warehouse()
        self.__it_department = ItDepartment()
        self.__office_equipments: List[OfficeEquipment] = [
            Printer("HP", "J9V90A#B1H", "$74.95", "inkjet"),
            Scanner("Fujitsu", "ScanSnap iX1600", "$399.99", 600),
            Scanner("Brother", "Duplex Compact", "$129.98", 300),
            Copier("Pantum", "M6802FDW-V1X47B", "$129.98", 300, "laser")
        ]

    def accept_truck(self):
        for office_equipment in self.__office_equipments:
            self.__warehouse.load(office_equipment)

    def unload_to_it_department(self):
        title = input("Введите название оргтехники '<Бренд>, <Модель>': ")
        amount = input("Введите количество единиц оргтехники: ")
        try:
            amount = int(amount)
            self.__warehouse.unload(title, amount, self.__it_department)
            if amount < 0:
                print("Количество единиц оргтехники меньше нуля")
                return
        except ValueError:
            print("Количество единиц оргтехники не целое число")
        except AttributeError:
            print("На складе не достаточное количество оргтехники")
        except KeyError:
            print("Оргтехника по введенному названию не найдена")

    def make_report(self):
        report = self.__warehouse.report()
        print(json.dumps(report, indent=4))

    def run(self):
        while True:
            print("Команды:")
            print(f"{self.__COMMAND_ACCEPT_TRUCK} - принять грузовик на склад")
            print(f"{self.__COMMAND_UNLOAD_TO_IT_DEPARTMENT} - отгрузить оргтехнику в IT-отдел")
            print(f"{self.__COMMAND_MAKE_REPORT} - вывести отчет по остаткам на складе")
            print(f"{self.__COMMAND_EXIT} - выйти из программы")
            command = input("Выберите номер команды: ")

            if command == self.__COMMAND_EXIT:
                exit(0)
            elif command == self.__COMMAND_ACCEPT_TRUCK:
                self.accept_truck()
            elif command == self.__COMMAND_UNLOAD_TO_IT_DEPARTMENT:
                self.unload_to_it_department()
            elif command == self.__COMMAND_MAKE_REPORT:
                self.make_report()


if __name__ == '__main__':
    dispatcher = Dispatcher()
    dispatcher.run()
