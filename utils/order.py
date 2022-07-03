from .db_functions import read_from_db, execute_on_db
from .utils import print_list, print_dict


ORDERS_MENU_OPTIONS = {
    "1": "show orders list",
    "2": "add an order",
    "3": "update existing order status",
    "4": "update existing order courier",
    "5": "delete order",
    "0": "back to main menu",
}


ORDERS_STATUS_OPTIONS = {
    "1": "PREPARING",
    "2": "Out for delivery",
    "3": "Delivered",
}


# ---------------db------------------------
def read_orders():
    return read_from_db(
        """
     SELECT 
        order_id
        , customer_name
        , customer_address
        , CAST(customer_phone as CHAR(50)) as customer_phone
        , p.name as product_name
        , c.name as courier_name
        , current_status
    FROM orders o
    INNER JOIN products p USING(product_id)
    INNER JOIN couriers c USING(courier_id)
    ORDER BY order_id
     """
    )


def insert_order_into_db(new_order_dict):
    execute_on_db(
        f"""
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
    """
    )


def update_order_status_on_db(order_id, new_status):
    execute_on_db(
        f"""
    UPDATE orders
    SET
        current_status = '{new_status}'
    WHERE
        order_id = {order_id};
    """
    )


def update_order_courier_on_db(order_id, courier_id):
    execute_on_db(
        f"""
    UPDATE orders
    SET
        courier_id = {courier_id}
    WHERE
        order_id = {order_id};
    """
    )


def delete_order_from_db(order_id):
    execute_on_db(
        f"""
    DELETE FROM orders 
    WHERE
        order_id = {order_id};
    """
    )


# ---------------------------------------
def add_order(
    products_list,
    couriers_list,
    insert_order_into_db=insert_order_into_db,
    read_orders=read_orders,
):
    print("Available products:")
    print_list(products_list)
    print("Available couriers:")
    print_list(couriers_list)
    print("Status codes:")
    print_dict(ORDERS_STATUS_OPTIONS)
    try:
        new_order_dict = {
            "customer_name": input("customer_name: "),
            "customer_address": input("customer_address: "),
            "customer_phone": input("customer_phone: "),
            "product_id": products_list[int(input("product id: "))][0],
            "courier_id": couriers_list[int(input("courier id: "))][0],
            "current_status": ORDERS_STATUS_OPTIONS[input("current status code: ")],
        }
        insert_order_into_db(new_order_dict)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_orders()


def update_order_status(
    orders_list,
    update_order_status_on_db=update_order_status_on_db,
    read_orders=read_orders,
):
    try:
        order_index = int(input("enter order id to update: "))
        assert orders_list[order_index], "wrong order_id"
        order_id = orders_list[order_index][0]
        print_dict(ORDERS_STATUS_OPTIONS)
        new_status = ORDERS_STATUS_OPTIONS[input("select status_id id: ")]
        update_order_status_on_db(order_id, new_status)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_orders()


def update_order_courier(
    orders_list,
    couriers_list,
    update_order_courier_on_db=update_order_courier_on_db,
    read_orders=read_orders,
):
    try:
        order_index = int(input("enter order id to update: "))
        assert orders_list[order_index], "wrong order_id"
        order_id = orders_list[order_index][0]
        print_list(couriers_list)
        courier_id = couriers_list[int(input("select courier_id id: "))][0]
        update_order_courier_on_db(order_id, courier_id)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_orders()


def delete_order(
    orders_list, delete_order_from_db=delete_order_from_db, read_orders=read_orders
):
    try:
        order_index = int(input("enter order_id id to delete: "))
        assert orders_list[order_index], "wrong order_id"
        order_id = orders_list[order_index][0]
        delete_order_from_db(order_id)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_orders()


def run_orders_menu(products, couriers, orders, run_main_menu):
    print_dict(ORDERS_MENU_OPTIONS)
    user_input = input("Select your option:")
    if user_input == "1":
        print_list(orders)
    elif user_input == "2":
        orders = add_order(products, couriers)
    elif user_input == "3":
        orders = update_order_status(orders)
    elif user_input == "4":
        orders = update_order_courier(orders, couriers)
    elif user_input == "5":
        orders = delete_order(orders)
    elif user_input == "0":
        run_main_menu()
    else:
        print("try again")
    run_orders_menu(products, couriers, orders, run_main_menu)
