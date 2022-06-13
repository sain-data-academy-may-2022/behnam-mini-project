# ----------- pretty print in terminal ----------------
def print_dict(menu_dict):
    print()
    for option, title in menu_dict.items():
        print(f'[{option}]: {title}')


def print_list(my_list):
    for i, item in enumerate(my_list):
        print(f'\t[{i}]: {" ".join(item[1:])}')
    print()
