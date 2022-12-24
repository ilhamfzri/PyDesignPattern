from .abstract_factory import AbstractFactory
from .abstract_products import CPU, Motherboard, Fan
from .amd_products import AmdCPU, AmdMotherboard, AmdFan

class AMDFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_processor(self) -> CPU:
        return AmdCPU()
    
    def create_motherboard(self) -> Motherboard:
        return AmdMotherboard()
    
    def create_fan(self) -> Fan:
        return AmdFan()
    
