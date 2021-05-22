from office_equipment import OfficeEquipment


class Printer(OfficeEquipment):
    def __init__(self, brand: str, model: str, price: str, printing_technology: str):
        super().__init__(brand, model, price)
        self.printing_technology = printing_technology
