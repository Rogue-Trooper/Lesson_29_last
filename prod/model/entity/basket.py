from prod.model.entity import *


class Basket:
    def __init__(self):
        self._products = []

    def add(self, product):
        if isinstance(product, Product):
            self._products.append(product)

    def __bool__(self):
        return len(self._products) != 0

    def __len__(self):
        return len(self._products)

    def __getitem__(self, item):
        return self._products[item]

    def __setitem__(self, key, value):
        self._products[key] = value

    def __delitem__(self, key):
        del self._products[key]


    # def __iter__(self):
    #     return iter(self._products)

    # def __iter__(self):
    #     self.__index = -1
    #     return self
    #
    # def __next__(self):
    #     self.__index += 1
    #     return self._products[self.__index]

    # def get(self, index):
    #     if isinstance(index, int) and 0 <= index < self.size():
    #         return self._products[index]
    #
    # def size(self):
    #     return len(self._products)

    def __str__(self):
        return f""


# basket = Basket()
# basket.add(Product(10))
# basket.add(Product(20))
# basket.add(Product(30))
#
# print(basket[0])
# basket[0] = Product(100)
# del basket[2]
#
#
# for pr in basket:
#     print(pr)