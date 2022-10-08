from typing import Union


class Product:
    __id = 0

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return super().__new__(cls)

    def __init__(self, name: Union[str], weight: Union[int, float], price: Union[int, float]):
        self.id = self.__id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        annotations = {"id": (int,), "name": (str,), "weight": (int, float), "price": (int, float)}
        if type(value) in annotations[key]:
            if type(value) in (float, int) and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                return super().__setattr__(key, value)
        raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super().__delattr__(item)


class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)