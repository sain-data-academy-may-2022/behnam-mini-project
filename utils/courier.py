from .db_functions import read_from_db, execute_on_db
from .utils import print_list, print_dict


COURIERS_MENU_OPTIONS = {
    "1": "show couriers list",
    "2": "add a courier",
    "3": "update a courier",
    "4": "delete a courier",
    "0": "back to main menu",
}


# ------------db--------------------------
def read_couriers():
    return read_from_db(
        " SELECT courier_id, name as courier_name FROM couriers ORDER BY courier_id "
    )


def insert_courier_into_db(courier_name):
    execute_on_db(f" INSERT INTO couriers(name) VALUES('{courier_name}') ")


def update_courier_on_db(courier_id, new_name):
    execute_on_db(
        f"""
    UPDATE couriers 
    SET 
        name = '{new_name}'
    WHERE
        courier_id = {courier_id};
    """
    )


def delete_courier_from_db(courier_id):
    execute_on_db(
        f"""
    DELETE FROM couriers 
    WHERE
        courier_id = {courier_id};
    """
    )


# --------------------------------------
def add_courier(
    insert_courier_into_db=insert_courier_into_db, read_couriers=read_couriers
):
    courier_name = input("enter courier name: ")
    insert_courier_into_db(courier_name)
    return read_couriers()


def update_courier(
    couriers_list,
    update_courier_on_db=update_courier_on_db,
    read_couriers=read_couriers,
):
    try:
        courier_index = int(input("enter courier id to update: "))
        courier_id = couriers_list[courier_index][0]
        courier_name_new = input("enter courier name: ")
        update_courier_on_db(courier_id, courier_name_new)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_couriers()


def delete_courier(
    couriers_list,
    delete_courier_from_db=delete_courier_from_db,
    read_couriers=read_couriers,
):
    try:
        courier_index = int(input("enter courier id to delete: "))
        courier_id = couriers_list[courier_index][0]
        delete_courier_from_db(courier_id)
    except Exception as e:
        print("error: ", e)
        print("Please try again.")
    return read_couriers()


def run_couriers_menu(products, couriers, orders, run_main_menu):
    print_dict(COURIERS_MENU_OPTIONS)
    user_input = input("Select your option:")
    if user_input == "1":
        print_list(couriers)
    elif user_input == "2":
        couriers = add_courier()
    elif user_input == "3":
        couriers = update_courier(couriers)
    elif user_input == "4":
        couriers = delete_courier(couriers)
    elif user_input == "0":
        run_main_menu()
    else:
        print("try again")
    run_couriers_menu(products, couriers, orders, run_main_menu)
