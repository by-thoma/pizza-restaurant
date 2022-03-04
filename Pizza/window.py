from tkinter import *
import sqlite3
import tkinter.messagebox as mb
import json
import datetime
from datetime import datetime

class App(Tk):
    def __init__(self):
        super().__init__()
        menu = Menu(self)

        menu.add_command(label="About", command=self.show_info)
        menu.add_command(label="Exit", command=self.destroy)
        self.config(menu=menu)
    def show_info(self):
        msg = "GUI разработан 21.12.2021\nСтудент: Цогоева Т.В. гр.К33201"
        mb.showinfo("About", msg)

    def add_products(self):
        result = ""
        price=0
        for item in menu_l.curselection():
            result = result + str(menu_l.get(item))+ "\n"
            s = str(menu_l.get(item))
            for pizza in pizzas_list:
                if str(pizza["name"]) == s:
                    price+=int(pizza["price"])
            for pie in pies_list:
                if str(pie["name"]) == s:
                    price+=int(pie["price"])
            add_lbl.config(text="Your pizza selection:\n" + result + "\n")
        add_lbl1.config(text="Price: " + str(price))
        return price


    def add_order(self):
        result = ""
        price=0
        for item in menu_l.curselection():
            result = result + str(menu_l.get(item))+ "\n"
            s = str(menu_l.get(item))
            cursor.execute("INSERT INTO order (product) VALUES (?)",
                           (s))
            for pizza in pizzas_list:
                if str(pizza["name"]) == s:
                    price+=int(pizza["price"])

            for pie in pies_list:
                if str(pie["name"]) == s:
                    price+=int(pie["price"])

            add_lbl.config(text="Your pizza selection:\n" + result + "\n")
        add_lbl1.config(text="Price: " + str(price))

        newname= name_entry.get()
        newaddress = address_entry.get()
        newnumber=number_entry.get()
        date = datetime.now().strftime("%Y-%b-%d %H:%M:%S")

        cursor.execute("SELECT COUNT(*) from user  ")
        result = cursor.fetchone()
        if int(result[0]) > 0:
            print("")
        else:
            cursor.execute("INSERT INTO user (username,address,phone) VALUES (?, ?, ?)", (newname, newaddress, newnumber))
            db.commit()

        cursor.execute("SELECT COUNT(*) from orders_list  ")
        result = cursor.fetchone()
        if int(result[0]) > 0:
            print("")
        else:
            cursor.execute("INSERT INTO orders_list (order_price,date) VALUES (?, ?)",
                           (price,date))
            db.commit()



with sqlite3.connect("pizzeria.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, address TEXT, phone TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS orders_list(order_id INTEGER PRIMARY KEY AUTOINCREMENT,order_price INTEGER, date TEXT)""")



window = App()
window.geometry(f"900x620+500+100")
window.title("Pizzeria")

header = Label(window,text="MENU")
header.grid(row=0, column=1)

with open('Menu.json', 'r') as menu_json:
    json_data = json.load(menu_json)
pizzas_list = json_data["pizzas"]
pies_list = json_data["pies"]

for count, i in enumerate(pizzas_list):
    p = ""
    p += str("Name: {}\n".format(i["name"]))
    p += str("Price: {}\n".format(i["price"]))
    p += str("Sauces: {}\n".format(", ".join(str(x) for x in i["sauces"])))
    p += str("Ingredients: {}".format(", ".join(str(x) for x in i["filling"])))

    menu_pizza = Label(window, text=p, padx=10, pady=10, justify=LEFT)
    menu_pizza.grid(column=count, row=2)


for count, i in enumerate(pies_list):
    pie = ""
    pie += str("Name: {}\n".format(i["name"]))
    pie += str("Price: {}\n".format(i["price"]))
    pie += str("Ingredients: {}".format(", ".join(str(x) for x in i["filling"])))

    menu_pizza = Label(window, text=pie, padx=10, pady=10, justify=LEFT)
    menu_pizza.grid(column=count, row=3)

header1 = Label(window, text="ORDER",pady=10)
header1.grid(row=4, column=1)

name_label=Label(window,text="Enter your name")
name_label.grid(row=5, column=0,pady= 10)

name_entry = Entry(window, width=30)
name_entry.grid(row=5, column=1, pady= 10)

address_label = Label(window, text="Enter your address ")
address_label.grid(row=6, column=0, pady= 10)

address_entry = Entry(window, width=30)
address_entry.grid(row=6, column=1)


number_label = Label(window, text="Enter your phone number ")
number_label.grid(row=7, column=0, pady= 10)

number_entry = Entry(window, width=30)
number_entry.grid(row=7, column=1)

menu_l = Listbox(window, selectmode=MULTIPLE)
menu_l.grid(row=8, column=0)

for item in pies_list:
    menu_l.insert(0, item["name"])

for item in pizzas_list:
    menu_l.insert(0, item["name"])

add_lbl = Label(window, text="")
add_lbl.grid(row=8, column=1)
add_lbl1 = Label(window, text="")
add_lbl1.grid(row=9, column=1)

button= Button(window, text="Order", command=window.add_order, width=20)
button.grid(row=10, column=0)


window.mainloop()