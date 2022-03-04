from Product import Product
from Mixin import BakingMixin
import time
import asyncio

class Pie(Product, BakingMixin):

    def __init__(self,terminal,id):
        super().__init__(terminal,id)

    def set_info(self, product_tuple):
        super().set_info(product_tuple)

    def show_info(self):
        super().show_info()

    async def prepare_self(self):
        await asyncio.sleep(1)
        self.bake_food(180)
        await asyncio.sleep(2)
        self._slicing()
        await asyncio.sleep(1)
        self._packing()

    def _slicing(self):
        print(f"Пирог {self.name} разрезан на аппетитные кусочки...")
    def _packing(self):
        print(f"Пирог {self.name} упакован с любовью и ждет вас. Приятного аппетита!")
    def __str__(self) -> str:
        return '(Название: {}\nЦена:{}\nИнгредиенты:{}\n)'.format(self.name,self.price,self.filling)

