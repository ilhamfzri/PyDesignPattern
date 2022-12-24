from .abstract_products import CPU, Motherboard, Fan

class AmdCPU(CPU):
    """
    Type: Concrete Product
    Abstract methods of the CPU base class are implemented.
    """

    def get_socket_type(self) -> str:
        return "AMD CPU Socket"
    
class AmdMotherboard(Motherboard):
    """
    Type: Concrete Product
    Abstract methods of the Motherboard base class are implemented.
    """

    def get_socket_type(self) -> str:
        return "AMD CPU Socket"
    

class AmdFan(Fan):
    """
    Type: Concrete Product
    Abstract methods of the Fan base class are implemented.
    """
    def get_socket_type(self) -> str:
        return "AMD CPU Socket"