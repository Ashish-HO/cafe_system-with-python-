from menu import *

order = {}


def take_order():

    more_order = 1
    while True:
        item_name = input("Item Name:")
        if item_name in menu:
            quantity = int(input("Quantity:"))
            order[item_name] = quantity
        else:
            print(f"{item_name} not in menu")
        more_order = input("More order.......(y/n)?").lower()
        if more_order == "y":
            continue
        else:
            break
    return order


def show_order():
    print()
    print()
    print("Your order is ..")
    print("item name          Quantity")
    for item in order:
        print(f"{item}                {order[item]}")

    return order


if __name__ == "__main__":
    take_order()
    show_order()

    print(order)
