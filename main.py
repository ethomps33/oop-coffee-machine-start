from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
coin = money.COIN_VALUES
latte = MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

machine.report()

menu.get_items()

order = input(f"Hi! What can I get for you today? {menu.get_items()}: ").lower()

menu.find_drink(order)
if order == "latte":
    order = latte
elif order == "espresso":
    order = espresso
elif order == "cappuccino":
    order = cappuccino

machine.is_resource_sufficient(order)

money.make_payment(order.cost)



