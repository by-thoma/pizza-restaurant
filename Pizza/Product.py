from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self,terminal,id):
        for i in terminal.pizzas_list:
            if i["id"] == id:
                self.set_info(i)

        for i in terminal.pies_list:
            if i["id"] == id:
                self.set_info(i)

    def set_info(self, product_tuple):
        self._name = product_tuple["name"]
        self._price = product_tuple["price"]
        self.filling = product_tuple["filling"]


    def show_info(self):
        print("Name: {}".format(self._name))
        print("Price: {}".format(self._price))
        print("Filling: {}".format(", ".join(str(x) for x in self.filling)))

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @price.setter
    def price(self, price):
        if (price >= 0):
            self._price = price
        else:
            raise ValueError

    @abstractmethod
    def prepare_self(self):
        pass
