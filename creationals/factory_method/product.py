from abc import abstractmethod


class Product:
    """
    The Product interface declares the operations that all concrete products must implement.
    """
    @abstractmethod
    def operation(self) -> str:
        pass