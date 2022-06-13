import imp
import json
from .db_functions import read_from_db, execute_on_db, close_db_connections


DATA_FILE = 'data/cafe.json'
DB_FILE = './db/caffe.sql'


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
    1: 'PREPARING',
    2: 'Out for delivery',
    3: 'Delivered',
}

MAIN_MENU_OPTIONS = {
    '1': 'products menu',
    '2': 'couriers menu',
    '3': 'orders menu',
    '0': 'exit',
}



# ----------- print in terminal ----------------
def print_menu(MAIN_MENU_OPTIONS):
    print()
    for option, title in MAIN_MENU_OPTIONS.items():
        print(f'[{option}]: {title}')

def print_list(my_list):
    for i, item in enumerate(my_list):
        print(f'\t[{i}]: {" ".join(item[1:])}')
    print()

# ----------- read & write data ----------------
# def read_data(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#         products = data['products']
#         couriers = data['couriers']
#         orders = data['orders']
#     return products, couriers, orders


def read_products():
    return read_from_db(" SELECT product_id, name as product_name FROM products ")

def read_couriers():
    return read_from_db(" SELECT courier_id, name as courier_name FROM couriers ")

def read_orders():
    return read_from_db("""
     SELECT 
        order_id
        , p.name as product_name
        , c.name as courier_name
        , customer_name
        , customer_address
        , CAST(customer_phone as CHAR(50)) as customer_phone
        , current_status
    FROM orders o
    INNER JOIN products p USING(product_id)
    INNER JOIN couriers c USING(courier_id)
     """)

def insert_product_into_db(product_name):
    execute_on_db(f" INSERT INTO products(name) VALUES('{product_name}') ")

def insert_courier_into_db(courier_name):
    execute_on_db(f" INSERT INTO couriers(name) VALUES('{courier_name}') ")

def insert_order_into_db(new_order_dict):
    execute_on_db(f"""
    INSERT INTO orders(
        product_id,
        courier_id,
        current_status,
        customer_name,
        customer_address,
        customer_phone) 
    VALUES(
        {new_order_dict["product_id"]},
        {new_order_dict["courier_id"]},
        '{new_order_dict["current_status"]}',
        '{new_order_dict["customer_name"]}',
        '{new_order_dict["customer_address"]}',
        {new_order_dict["customer_phone"]}
        ) 
    """)

def update_product_on_db(product_id, new_name):
    execute_on_db(f"""
    UPDATE products 
    SET 
        name = '{new_name}'
    WHERE
        product_id = {product_id};
    """)

def update_courier_on_db(courier_id, new_name):
    execute_on_db(f"""
    UPDATE couriers 
    SET 
        name = '{new_name}'
    WHERE
        courier_id = {courier_id};
    """)

def update_order_status_on_db(order_id, new_status):
    execute_on_db(f"""
    UPDATE orders
    SET
        current_status = '{new_status}'
    WHERE
        order_id = {order_id};
    """)

def update_order_courier_on_db(order_id, courier_id):
    execute_on_db(f"""
    UPDATE orders
    SET
        courier_id = {courier_id}
    WHERE
        order_id = {order_id};
    """)

def delete_product_from_db(product_id):
    execute_on_db(f"""
    DELETE FROM products 
    WHERE
        product_id = {product_id};
    """)

def delete_courier_from_db(courier_id):
    execute_on_db(f"""
    DELETE FROM couriers 
    WHERE
        courier_id = {courier_id};
    """)

def delete_order_from_db(order_id):
    execute_on_db(f"""
    DELETE FROM orders 
    WHERE
        order_id = {order_id};
    """)

def read_data():
    products = read_products()
    couriers = read_couriers()
    orders = read_orders()
    return products, couriers, orders


# def write_data(file_path, products, couriers, orders):
#     with open(file_path, 'w') as file:
#         json.dump(
#             {
#                 'products': products,
#                 'couriers': couriers,
#                 'orders': orders,
#             }, file, indent=4)


# ----------------product -----------------------
def add_product():
    product_name = input('enter product name: ')
    insert_product_into_db(product_name)
    return read_products()

def update_product(products_list):
    try:
        product_index = int(input('enter product id to update: '))
        product_id = products_list[product_index][0]
        product_name_new = input('enter product name: ')
        update_product_on_db(product_id, product_name_new)
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return read_products()

def delete_product(products_list):
    try:
        product_index = int(input('enter product id to delete: '))
        product_id = products_list[product_index][0]
        delete_product_from_db(product_id)
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return read_products()


# ---------------- courier -----------------------
def add_courier():
    courier_name = input('enter courier name: ')
    insert_courier_into_db(courier_name)
    return read_couriers()

def update_courier(couriers_list):
    try:
        courier_index = int(input('enter courier id to update: '))
        courier_id = couriers_list[courier_index][0]
        courier_name_new = input('enter courier name: ')
        update_courier_on_db(courier_id, courier_name_new)
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return read_couriers()

def delete_courier(couriers_list):
    try:
        courier_index = int(input('enter courier id to delete: '))
        courier_id = couriers_list[courier_index][0]
        delete_courier_from_db(courier_id)
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return read_couriers()


# ----------------order -----------------------
def add_order(orders_list, products_list, couriers_list):
    print('Available couriers:')
    print_list(couriers_list)
    print('Status codes:')
    print_menu(ORDERS_STATUS_OPTIONS)
    try:
        new_order_dict = {
                    "customer_name": input('customer_name: '),
                    "customer_address": input('customer_address: '),
                    "customer_phone": input('customer_phone: '),
                    "product_id": products_list[int(input('product id: '))][0],
                    "courier_id": couriers_list[int(input('courier id: '))][0],
                    "current_status": ORDERS_STATUS_OPTIONS[int(input('current status code: '))],
                    }
        insert_order_into_db(new_order_dict)
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return read_orders()


def update_order_status(orders_list):
    try:
        order_id = int(input('enter order_id id to update: '))
        assert orders_list[order_id], 'wrong order_id'
        print_list(ORDERS_STATUS_OPTIONS)
        orders_list[order_id]['status'] = ORDERS_STATUS_OPTIONS[int(input('select status_id id: '))]
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return orders_list


def delete_order(orders_list):
    try:
        order_id = int(input('enter order_id id to delete: '))
        del orders_list[order_id]
    except Exception as e:
        print('error: ', e)
        print('Please try again.')
    return orders_list
