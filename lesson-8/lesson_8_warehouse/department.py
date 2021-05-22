from abc import ABC, abstractmethod
from typing import List

from office_equipment import OfficeEquipment


class Department(ABC):
    @abstractmethod
    def give_back(self, office_equipments: List[OfficeEquipment]): pass

    @abstractmethod
    def take(self, office_equipments: List[OfficeEquipment]): pass
