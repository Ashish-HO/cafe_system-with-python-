from menu import *
from order import *
from datetime import datetime, date
import sys


class customer:

    def __init__(self, customer_name, order):
        self.customer_name = customer_name
        self.order = order
        pass

    def bill(self):
        now = datetime.now()
        amount = 0
        with open("output.txt", "a") as f:
            sys.stdout = f
            print("************BILL***************")
            print("cafe ko name")
            print("cafe ko address")
            print("cafe ko contact no.")
            print("_______________________________________")

            print(f"Name:{self.customer_name}")
            print(f"Date:{date.today()}")
            print(f'Time:{ now.strftime("%H:%M:%S")}')
            print("_______________________________________")

            print("Item Name     Quantity       Per price")
            for item in order:
                print(f"{item}          {order[item]}            {menu[item]}")
                amount += order[item] * menu[item]
            print("              __________________________")
            print(f"                Total      {amount}")
            print("_______________________________________")

            print("    ****Visit us Again :)*****   ")
            print()
        f.close()


while True:
    print("==============================")
    customer_name = input("Enter customer name:")
    order = take_order()
    c = customer(customer_name, order)
    print("Displaying bill....")
    print()
    c.bill()

    cont = input("press q to quit and any key to continue.(q/any).").lower()

    if cont == "q":
        exit(0)
