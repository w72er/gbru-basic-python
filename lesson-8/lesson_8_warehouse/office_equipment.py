from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    @abstractmethod
    def __init__(self, brand: str, model: str, price: str):
        self.brand: str = brand
        self.model: str = model
        self.price: str = price
