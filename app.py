from utils.db_functions import initialize_db, close_db_connections

from utils.functions import (
    MAIN_MENU_OPTIONS,
    PRODUCTS_MENU_OPTIONS,
    COURIERS_MENU_OPTIONS,
    ORDERS_MENU_OPTIONS,
    DB_FILE,

    read_data,

    print_menu,
    print_list,

    add_product,
    update_order_courier,
    update_product,
    delete_product,

    add_courier,
    update_courier,
    delete_courier,

    add_order,
    update_order_status,
    delete_order,
)


def run_products_menu(products, couriers, orders):
    print_menu(PRODUCTS_MENU_OPTIONS)
    user_input = input('Select your option:')
    if user_input == '1':
        print_list(products)
    elif user_input == '2':
        products = add_product()
    elif user_input == '3':
        products = update_product(products)
    elif user_input == '4':
        products = delete_product(products)
    elif user_input == '0':
        run_main_menu(products, couriers, orders)
    else:
        print('try again')
    run_products_menu(products, couriers, orders)


def run_couriers_menu(products, couriers, orders):
    print_menu(COURIERS_MENU_OPTIONS)
    user_input = input('Select your option:')
    if user_input == '1':
        print_list(couriers)
    elif user_input == '2':
        couriers = add_courier()
    elif user_input == '3':
        couriers = update_courier(couriers)
    elif user_input == '4':
        couriers = delete_courier(couriers)
    elif user_input == '0':
        run_main_menu(products, couriers, orders)
    else:
        print('try again')
    run_couriers_menu(products, couriers, orders)


def run_orders_menu(products, couriers, orders):
    print_menu(ORDERS_MENU_OPTIONS)
    user_input = input('Select your option:')
    if user_input == '1':
        print_list(orders)
    elif user_input == '2':
        orders = add_order(products, couriers)
    elif user_input == '3':
        orders = update_order_status(orders)
    elif user_input == '4':
        orders = update_order_courier(orders, couriers)
    elif user_input == '5':
        orders = delete_order(orders)
    elif user_input == '0':
        run_main_menu(products, couriers, orders)
    else:
        print('try again')
    run_orders_menu(products, couriers, orders)


def run_main_menu(products, couriers, orders):
    print_menu(MAIN_MENU_OPTIONS)
    user_input = input('Select your option:')
    if user_input == '1':
        run_products_menu(products, couriers, orders)
    elif user_input == '2':
        run_couriers_menu(products, couriers, orders)
    elif user_input == '3':
        run_orders_menu(products, couriers, orders)
    elif user_input == '0':
        close_db_connections()
        exit()
    else:
        print('try again')
        run_main_menu(products, couriers, orders)


if __name__ == '__main__':
    initialize_db(DB_FILE)
    products, couriers, orders = read_data()
    run_main_menu(products, couriers, orders)
