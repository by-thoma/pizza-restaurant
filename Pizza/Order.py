from Pizza import Pizza
from Pie import Pie
from datetime import datetime
from time import time
import asyncio



def add_to_file(func):
    def wrapper(self,product):
        result = func(self,product)
        with open('orders.txt','a', encoding='utf-8') as orders:
            orders.write(str(datetime.now()) + "\n")
            orders.write("Added: " + product.name + "\n")
            orders.write("Price: " + str(product.price) + "\n\n")
        return result
    return wrapper


class Order():
    def __init__(self):
        self.price = 0
        self.ordered_products = []


    def get_order(self, terminal):
        while True:
            product = input("Выберите пиццу(1) или пирог(2). Выберите (0) если хотите отправить заказ.\n")
            if product == '1':
                id = self.choose_pizza()
                pizza = Pizza(terminal, id)
                self.add_position(pizza)
            elif product == '2':
                id = self.choose_pie()
                pie = Pie(terminal, id)
                self.add_position(pie)
            elif product == '0':
                self.show_order()
                self.prepare_order()
                print("\n")
            else:
                raise ValueError



    def choose_pizza(self) -> int:
        pizza_id = input("Выберите пиццу.. p/b/s\n")

        if pizza_id == 'p':
            return 101
        elif pizza_id == 'b':
            return 102
        elif pizza_id == 's':
            return 103
        else:
            raise ValueError

    def choose_pie(self) -> int:
        pizza_id = input("Выберите пирог.. a/p/c\n")

        if pizza_id == 'a':
            return 201
        elif pizza_id == 'p':
            return 202
        elif pizza_id == 'c':
            return 203
        else:
            raise ValueError



    def prepare_order(self):
        start=time()
        prepare = []
        for product in self.ordered_products:
            new_prep = asyncio.ensure_future(product.prepare_self())
            prepare.append(new_prep)

        loop=asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(*prepare))
        loop.close()
        print("{:.2F}".format(time()-start))


    @add_to_file
    def add_position(self, product):
        self.ordered_products.append(product)
        self.price += product.price


    def show_order(self):
        print("Заказано: {}".format(", ".join((x).name for x in self.ordered_products)))
        print("К оплате: {}\n".format(self.price))






