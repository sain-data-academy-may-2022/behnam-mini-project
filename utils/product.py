from .db_functions import read_from_db, execute_on_db
from .utils import print_list, print_dict


PRODUCTS_MENU_OPTIONS = {
    "1": "show products list",
    "2": "add a product",
    "3": "update a product",
    "4": "delete a product",
    "0": "back to main menu",
}


# --------------db-------------------------
def read_products():
    return read_from_db(
        """
    SELECT 
        product_id
        , name as product_name
    FROM
        products
    ORDER BY product_id
    """
    )


def insert_product_into_db(product_name):
    execute_on_db(f" INSERT INTO products(name) VALUES('{product_name}') ")


def update_product_on_db(product_id, new_name):
    execute_on_db(
        f"""
    UPDATE products 
    SET 
        name = '{new_name}'
    WHERE
        product_id = {product_id};
    """
    )


def delete_product_from_db(product_id):
    execute_on_db(
        f"""
    DELETE FROM products 
    WHERE
        product_id = {product_id};
    """
    )


# ---------------------------------------
def add_product(
    insert_product_into_db=insert_product_into_db, read_products=read_products
):
    product_name = input("enter product name: ")
    insert_product_into_db(product_name)
    return read_products()


def update_product(
    products_list,
    update_product_on_db=update_product_on_db,
    read_products=read_products,
):
    try:
        product_index = int(input("enter product id to update: "))
        product_id = products_list[product_index][0]
        product_name_new = input("enter product name: ")
        update_product_on_db(product_id, product_name_new)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_products()


def delete_product(
    products_list,
    delete_product_from_db=delete_product_from_db,
    read_products=read_products,
):
    try:
        product_index = int(input("enter product id to delete: "))
        product_id = products_list[product_index][0]
        delete_product_from_db(product_id)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_products()


def run_products_menu(products, couriers, orders, run_main_menu):
    print_dict(PRODUCTS_MENU_OPTIONS)
    user_input = input("Select your option:")
    if user_input == "1":
        print_list(products)
    elif user_input == "2":
        products = add_product()
    elif user_input == "3":
        products = update_product(products)
    elif user_input == "4":
        products = delete_product(products)
    elif user_input == "0":
        run_main_menu()
    else:
        print("try again")
    run_products_menu(products, couriers, orders, run_main_menu)
