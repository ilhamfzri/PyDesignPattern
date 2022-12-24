from abc import ABC, abstractmethod
from .abstract_products import CPU, Motherboard, Fan

class AbstractFactory(ABC):
    """
    The AbstractFactory
    """

    @abstractmethod
    def create_processor(self) -> CPU:
        pass

    @abstractmethod
    def create_motherboard(self) -> Motherboard:
        pass

    @abstractmethod
    def create_fan(self) -> Fan:
        pass