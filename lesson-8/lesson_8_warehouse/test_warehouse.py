import json

from warehouse import Warehouse
from printer import Printer


class TestWarehouse:
    def test_report_when_warehouse_has_just_created_should_return_empty_report(self):
        warehouse = Warehouse()

        report = warehouse.report()

        empty_report = dict()
        assert json.dumps(report) == json.dumps(empty_report)

    def test_load_when_receive_office_equipment_should_store_it(self):
        printer = Printer("HP", "J9V90A#B1H", "$74.95", "inkjet")
        warehouse = Warehouse()

        warehouse.load(printer)

        report = warehouse.report()
        expected_report = {"HP, J9V90A#B1H": 1}
        assert json.dumps(report) == json.dumps(expected_report)

