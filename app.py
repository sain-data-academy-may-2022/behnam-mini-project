from utils import (
    write_data,
    read_data,

    print_menu,
    print_list,
)


class Product():
    PRODUCTS_MENU_OPTIONS = {
        '1': 'show products list',
        '2': 'add a product',
        '3': 'update a product',
        '4': 'delete a product',
        '0': 'back to main menu',
    }
    products_list = []
    def __init__(self) -> None:
        self.name = input('enter product name: ')
        Product.products_list.append(self)

    @classmethod
    def update(cls) -> None:
        print_list(cls.products_list)
        product_id = int(input('enter product id to update: '))
        product_name_new = input('enter product name: ')
        cls.products_list[product_id] = product_name_new

    @classmethod
    def update(cls) -> None:
        print_list(cls.products_list)
        product_id = int(input('enter product id to delete: '))
        del cls.products_list[product_id]
