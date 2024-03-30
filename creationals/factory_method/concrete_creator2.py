from creationals.factory_method.product import Product
from creationals.factory_method.concrete_product2 import ConcreteProduct2
from creationals.factory_method.creator import Creator


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
