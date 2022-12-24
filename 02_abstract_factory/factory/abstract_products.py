from abc import ABC, abstractmethod

class CPU(ABC):
    """
    Creates "Abstract CPU"
    """

    @abstractmethod
    def get_socket_type(self) -> str:
        pass

class Motherboard(ABC):
    """
    Create "Abstract Motherboard"
    """

    @abstractmethod
    def get_socket_type(self) -> str:
        pass

class Fan(ABC):
    """
    Create "Abstract Fan"
    """

    @abstractmethod
    def get_socket_type(self) -> str:
        pass