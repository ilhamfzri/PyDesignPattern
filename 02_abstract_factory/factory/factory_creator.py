from .abstract_factory import AbstractFactory
from .amd_factory import AMDFactory
from .intel_factory import IntelFactory

class FactoryCreator:
    def __init__(self):
        self.factories = {
            "intel": IntelFactory,
            "amd": AMDFactory,
        }

    def create_factory(self, name) -> AbstractFactory:
        if name in self.factories.keys():
            return self.factories[name]()
        else:
            raise Exception('f factory with {name} name not supported!')