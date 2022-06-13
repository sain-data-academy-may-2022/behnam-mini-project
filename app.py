# OOP & tests


from utils import (
    write_data,
    read_data,

    print_menu,
    print_list,

    add_product,
    update_product,
    delete_product,

    add_courier,
    update_courier,
    delete_courier,

    add_order,
    update_order_status,
    delete_order,
)


MAIN_MENU_OPTIONS = {
    '1': 'products menu',
    '2': 'couriers menu',
    '3': 'orders menu',
    '0': 'exit',
}

PRODUCTS_MENU_OPTIONS = {
    '1': 'show products list',
    '2': 'add a product',
    '3': 'update a product',
    '4': 'delete a product',
    '0': 'back to main menu',
}

COURIERS_MENU_OPTIONS = {
    '1': 'show couriers list',
    '2': 'add a courier',
    '3': 'update a courier',
    '4': 'delete a courier',
    '0': 'back to main menu',
}

ORDERS_MENU_OPTIONS = {
    '1': 'show orders list',
    '2': 'add an order',
    '3': 'update existing order status',
    '4': 'update existing order',
    '5': 'delete order',
    '0': 'back to main menu',
}

ORDERS_STATUS_OPTIONS = {
    '1': 'PREPARING',
    '2': 'Out for delivery',
    '3': 'Delivered',
}

DATA_FILE = 'data/cafe.json'


def run_products_menu(products, couriers, orders):
    user_input = input('Select your option:')
    if user_input == '1':
        print_list(products)
    elif user_input == '2':
        products = add_product(products)
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
    user_input = input('Select your option:')
    if user_input == '1':
        print_list(couriers)
    elif user_input == '2':
        couriers, orders = add_courier(couriers, orders)
    elif user_input == '3':
        couriers = update_courier(couriers)
    elif user_input == '4':
        couriers = delete_courier(couriers, orders)
    elif user_input == '0':
        run_main_menu(products, couriers, orders)
    else:
        print('try again')
    run_couriers_menu(products, couriers, orders)


def run_orders_menu(products, couriers, orders):
    user_input = input('Select your option:')
    if user_input == '1':
        print_list(orders)
    elif user_input == '2':
        orders = add_order(orders, couriers)
    elif user_input == '3':
        order_id = int(input('enter order_id id to update: '))
        print_menu(ORDERS_STATUS_OPTIONS)
        status_id = input('select status_id id: ')
        orders = update_order_status(
            orders, order_id, ORDERS_STATUS_OPTIONS[status_id])
    elif user_input == '5':
        orders = delete_order(orders, order_id)
    elif user_input == '0':
        run_main_menu(products, couriers, orders)
    else:
        print('try again')
    run_orders_menu(products, couriers, orders)


def run_main_menu(products, couriers, orders):
    print_menu(MAIN_MENU_OPTIONS)
    user_input = input('Select your option:')
    if user_input == '1':
        print_menu(PRODUCTS_MENU_OPTIONS)
        run_products_menu(products, couriers, orders)
    elif user_input == '2':
        print_menu(COURIERS_MENU_OPTIONS)
        run_couriers_menu(products, couriers, orders)
    elif user_input == '3':
        print_menu(ORDERS_MENU_OPTIONS)
        run_orders_menu(products, couriers, orders)
    elif user_input == '0':
        write_data(DATA_FILE, products, couriers, orders)
        exit()
    else:
        print('try again')
        run_main_menu(products, couriers, orders)


if __name__ == '__main__':
    products, couriers, orders = read_data(DATA_FILE)
    run_main_menu(products, couriers, orders)
