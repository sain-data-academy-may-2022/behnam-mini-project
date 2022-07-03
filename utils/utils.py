# ----------- pretty print in terminal ----------------
def print_dict(menu_dict):
    print()
    for option, title in menu_dict.items():
        print(f"[{option}]: {title}")


def print_list(my_list):
    """
    The first item in the list is id of the table
    in db, so lets replace it with index in the list
    when printing
    """
    for i, item in enumerate(my_list):
        msg = ",\t".join(item[1:])
        print(f"\t[{i}]: {msg}")
    print()
