from creationals.factory_method.product import Product
from creationals.factory_method.concrete_product1 import ConcreteProduct1
from creationals.factory_method.creator import Creator


class ConcreteCreator1(Creator):
    """
        Note that the signature of the method still uses the abstract product type,
        even though the concrete product is actually returned from the method. This
        way the Creator can stay independent of concrete product classes.
        """
    def factory_method(self) -> Product:
        return ConcreteProduct1()
