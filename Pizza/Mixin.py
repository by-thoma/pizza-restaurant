class BakingMixin:

    def bake_food(self, temp):
        print("{} приготовлен(а) при температуре {} градусов".format(self.name, temp))