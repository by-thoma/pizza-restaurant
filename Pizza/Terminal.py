import json
from Order import Order


class Terminal():

    def __init__(self):
        with open('Menu.json', 'r') as menu_json:
            json_data = json.load(menu_json)
        self.pizzas_list = json_data["pizzas"]
        self.pies_list = json_data["pies"]

    def __str__(self) -> str:
        return "To see the menu invoke show_menu()"


    def show_menu(self):
        print("\n------MENU------\n")

        for i in self.pizzas_list:
            print("Name: {}".format(i["name"]))
            print("Price: {}".format(i["price"]))
            print("Sauces: {}".format(", ".join(str(x) for x in i["sauces"])))
            print("Ingredients: {}".format(", ".join(str(x) for x in i["filling"])))
            print("\n")

        for i in self.pies_list:
            print("Name: {}".format(i["name"]))
            print("Price: {}".format(i["price"]))
            print("Filling: {}".format(i["filling"]))
            print("\n")

        print("----------------\n")

    def get_player_input(self):
        while True:
            choice = input("Do you want to make a new order? y/n\n")

            if choice == 'n':
                return
            elif choice == 'y':
                o1 = Order()
                o1.get_order(self)
            else:
                raise ValueError
