from office_equipment import OfficeEquipment


class Copier(OfficeEquipment):
    def __init__(self, brand: str, model: str, price: str, resolution: int, printing_technology: str):
        super().__init__(brand, model, price)
        self.resolution: int = resolution
        self.printing_technology: str = printing_technology
