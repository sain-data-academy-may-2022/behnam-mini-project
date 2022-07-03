from .utils import print_dict
from .db_functions import close_db_connections
from .product import read_products, run_products_menu
from .courier import read_couriers, run_couriers_menu
from .order import read_orders, run_orders_menu


MAIN_MENU_OPTIONS = {
    "1": "products menu",
    "2": "couriers menu",
    "3": "orders menu",
    "0": "exit",
}


def run_main_menu():
    products = read_products()
    couriers = read_couriers()
    orders = read_orders()
    print_dict(MAIN_MENU_OPTIONS)
    user_input = input("Select your option:")
    if user_input == "1":
        run_products_menu(products, couriers, orders, run_main_menu)
    elif user_input == "2":
        run_couriers_menu(products, couriers, orders, run_main_menu)
    elif user_input == "3":
        run_orders_menu(products, couriers, orders, run_main_menu)
    elif user_input == "0":
        close_db_connections()
        exit()
    else:
        print("try again")
        run_main_menu()
