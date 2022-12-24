from .abstract_products import CPU, Motherboard, Fan

class IntelCPU(CPU):
    """
    Type: Concrete Product
    Abstract methods of the CPU base class are implemented.
    """

    def get_socket_type(self) -> str:
        return "Intel CPU Socket"
    
class IntelMotherboard(Motherboard):
    """
    Type: Concrete Product
    Abstract methods of the Motherboard base class are implemented.
    """

    def get_socket_type(self) -> str:
        return "Intel CPU Socket"
    

class IntelFan(Fan):
    """
    Type: Concrete Product
    Abstract methods of the Fan base class are implemented.
    """
    def get_socket_type(self) -> str:
        return "Intel CPU Socket"