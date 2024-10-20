def show_menu():

    print()
    print("*********Menu*********")

    print("Item                    Price")
    print("_______________________________")
    for item in menu:
        print(f"{item}.....................{menu[item]}")


def add_menu(item_name, price):
    global menu

    if item_name != "":
        menu[item_name] = price
    else:
        return


def remove_item(item_name):
    global menu
    if item_name not in menu:
        print(f"{item_name} not in menu.")
        return
    else:
        menu.pop(item_name)


menu = {
    "momo": 100,
    "coke": 50,
    "water": 30,
    "cake": 300,
    "coffee": 70,
}


if __name__ == "__main__":
    print("Welcome to menu section of cafe")
    option = input("Enter 1 to add item and 2 to remove item from menu").lower()

    if option == "1":
        item_name = input("Enter the name of item to be added.")
        price = int("Enter the price of item .")  # handle the possible exceptions
        add_menu(item_name, price)
    elif option == "2":
        item_name = input("Enter the item name to be removed.")
        remove_item(item_name)
    else:
        print("Invalid option .")
