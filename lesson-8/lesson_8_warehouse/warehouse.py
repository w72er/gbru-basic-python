import json
from typing import Dict, List

from office_equipment import OfficeEquipment


class Warehouse:
    __office_equipments: Dict[str, List[OfficeEquipment]] = dict()

    @staticmethod
    def get_office_equipment_title(brand: str, model: str) -> str:
        return f'{brand}, {model}'

    def load(self, office_equipment: OfficeEquipment) -> None:
        title = self.get_office_equipment_title(office_equipment.brand, office_equipment.model)
        office_equipments = self.__office_equipments.get(title, [])
        office_equipments.append(office_equipment)
        self.__office_equipments[title] = office_equipments

    def unload(self, office_equipment_title: str, amount: int, department) -> None:
        office_equipments = self.__office_equipments.get(office_equipment_title, [])
        if amount > len(office_equipments):
            raise AttributeError('more than present')
        unloaded = office_equipments[:amount]
        department.take(unloaded)

        rest = office_equipments[amount:]
        if len(rest) == 0:
            del self.__office_equipments[office_equipment_title]
        else:
            self.__office_equipments[office_equipment_title] = office_equipments[amount:]

    def report(self) -> Dict[str, int]:
        return {title: len(wares) for title, wares in self.__office_equipments.items()}
