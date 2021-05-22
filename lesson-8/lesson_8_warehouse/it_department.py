from typing import List

from department import Department
from office_equipment import OfficeEquipment


class ItDepartment(Department):
    def give_back(self, office_equipments: List[OfficeEquipment]): pass

    def take(self, office_equipments: List[OfficeEquipment]):
        print(f'IT Department takes {len(office_equipments)}')
