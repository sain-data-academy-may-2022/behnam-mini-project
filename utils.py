import json


# ----------- read & write data ----------------
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        products = data['products']
        couriers = data['couriers']
        orders = data['orders']
    return products, couriers, orders


def write_data(file_path, products, couriers, orders):
    with open(file_path, 'w') as file:
        json.dump(
            {
                'products': products,
                'couriers': couriers,
                'orders': orders,
            }, file)


# ----------- print in terminal ----------------
def print_menu(MAIN_MENU_OPTIONS):
    print('\n ')
    for option, title in MAIN_MENU_OPTIONS.items():
        print(f'[{option}]: {title}')

def print_list(products_list):
    for i, product in enumerate(products_list):
        print(f'\t[{i}]: {product}')
    print('\n ')


# ----------------product -----------------------
def add_product(products_list):
    product_name = input('enter product name: ')
    products_list.append(product_name)
    return products_list

def update_product(products_list):
    product_id = int(input('enter product id to update: '))
    product_name_new = input('enter product name: ')
    products_list[product_id] = product_name_new
    return products_list

def delete_product(products_list):
    product_id = int(input('enter product id to delete: '))
    del products_list[product_id]
    return products_list


# ---------------- courier -----------------------
def add_courier(couriers_list, orders_list):
    courier_name = input('enter courier name: ')
    couriers_list.append(courier_name)
    for order in orders_list:
        if order['courier_id'] < 0:
            order['courier_id'] = 0
    return couriers_list, orders_list

def update_courier(couriers_list):
    courier_id = int(input('enter courier id to update: '))
    courier_name_new = input('enter courier name: ')
    couriers_list[courier_id] = courier_name_new
    return couriers_list

def delete_courier(couriers_list, orders_list):
    courier_id = int(input('enter courier id to delete: '))
    del couriers_list[courier_id]
    for order in orders_list:
        if order['courier_id'] >= courier_id:
            order['courier_id'] -= 1
    return couriers_list


# ----------------order -----------------------
def add_order(orders_list, couriers):
    print_list(couriers)
    orders_list.append(
            {
                "customer_name": input('customer_name: '),
                "customer_address": input('customer_address: '),
                "customer_phone": input('customer_phone: '),
                "courier_id": int(input('courier id: ')),
                "status": "preparing",
            }
        )
    return orders_list


def update_order_status(orders_list, order_id, status):
    orders_list[order_id]['status'] = status
    return orders_list


def delete_order(orders_list, order_id):
    order_id = int(input('enter order_id id to delete: '))
    del orders_list[order_id]
    return orders_list
