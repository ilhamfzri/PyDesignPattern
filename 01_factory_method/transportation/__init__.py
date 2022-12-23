from typing import Union
from .motorcycle import MotorycleTransportation
from .car import CarTransportation
from .truck import TruckTransportation

class FactoryTransportation:
    def __init__(self):
        self.transporation_list = {
            "motorcycle": MotorycleTransportation,
            "car": CarTransportation,
            "truck": TruckTransportation
        }

    def create_transporation(self, name:str) -> Union[MotorycleTransportation, CarTransportation, TruckTransportation]:
        if name in self.transporation_list.keys():
            return self.transporation_list[name]()
        else:
            raise Exception('f transportation with {name} name not supported!')