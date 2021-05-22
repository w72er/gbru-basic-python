from office_equipment import OfficeEquipment


class Scanner(OfficeEquipment):
    def __init__(self, brand: str, model: str, price: str, resolution: int):
        super().__init__(brand, model, price)
        self.resolution: int = resolution
