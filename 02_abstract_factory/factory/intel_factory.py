from .abstract_factory import AbstractFactory
from .abstract_products import CPU, Motherboard, Fan
from .intel_products import IntelCPU, IntelMotherboard, IntelFan

class IntelFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_processor(self) -> CPU:
        return IntelCPU()
    
    def create_motherboard(self) -> Motherboard:
        return IntelMotherboard()
    
    def create_fan(self) -> Fan:
        return IntelFan()
    
