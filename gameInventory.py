# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Displays the inventory.
def display_inventory(inventory):
    item_names = list(inventory.keys())
    item_cnt = 0
    print("\nInventory:")
    for i in range(len(item_names)):
        print("{1} {0}".format(item_names[i], inventory[item_names[i]]))
        item_cnt += inventory[item_names[i]]
    print("Total number of items: {}\n".format(item_cnt))

    return 0


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    item_names = list(inventory.keys())
    for i in range(len(added_items)):
        if added_items[i] in item_names:
            inventory[added_items[i]] += 1
        else:
            inventory[added_items[i]] = 1
            item_names.append(added_items[i])
    return inventory


def print_table_ordered(inv_list, str_len, num_len):
    for i in range(len(inv_list)):
        print(("{0:>{num_padding}}{1:>{str_padding}}").format(inv_list[i][1], inv_list[i][0], str_padding=str_len, num_padding=num_len))


# creat a 2 dimensional list from inventory dictionary. 1st value is the key of the dictionary, 2nd is the value
def list_creator(inventory):
    tmp_a = list(inventory.keys())
    tmp_b = list(inventory.values())
    w = 2
    h = len(tmp_a)
    inv_list = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(tmp_a)):
        inv_list[i][0] = tmp_a[i]
        inv_list[i][1] = tmp_b[i]
    return inv_list


# sorts the numbers in list in asc order
def sort_asc(inv_list, lenght):
    iterations = 1
    for iterations in range(1, lenght):
        j = 0
        for j in range(0, lenght-2):
            if inv_list[j][1] > inv_list[j+1][1]:
                temp = inv_list[j+1]
                inv_list[j+1] = inv_list[j]
                inv_list[j] = temp
            j += 1
    return inv_list


# sorts the given 2 dim list by it's second variable (has to be a number)
def sort_desc(inv_list, lenght):
    iterations = 1
    for iterations in range(1, lenght):
        j = 0
        for j in range(0, lenght-2):
            if inv_list[j][1] < inv_list[j+1][1]:
                temp = list[j+1]
                inv_list[j+1] = inv_list[j]
                inv_list[j] = temp
            j += 1
    return inv_list


def str_padding_calc(str_list, max_value):
    for i in range(len(str_list)):
        if len(str_list[i]) > max_value:
            max_value = len(item_names[i])
    return max_value + 3


def num_padding_calc(num_list, max_value):
    for i in range(len(num_list)):
        if len(str(num_list[i])) > max_value:
            max_value = len(str(num_list[i]))
    return max_value + 2


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    longest_str_len = len("item names")
    longest_num_len = len("count")
    item_names = list(inventory.keys())
    item_nums = list(inventory.values())
    longest_str_len = str_padding_calc(item_names, longest_str_len)
    longest_num_len = num_padding_calc(item_nums, longest_num_len)
    print("\nInvnroty:")
    print("{0:>{num_padding}}{1:>{str_padding}}".format("count", "item names", str_padding=longest_str_len, num_padding=longest_num_len))
    print("-"*(longest_str_len+longest_num_len))
    if order is None:
        inv_list = list_creator(inventory)
        print_table_ordered(inv_list, longest_str_len, longest_num_len)
    elif order is "count,desc":
        inv_list = list_creator(inventory)
        print_table_ordered(sort_desc(inv_list, len(inv_list)), longest_str_len, longest_num_len)
    elif order is "count,asc":
        inv_list = list_creator(inventory)
        print_table_ordered(sort_asc(inv_list, len(inv_list)), longest_str_len, longest_num_len)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as inv_file:
        inv_str = inv_file.read()
        inv_list = inv_str.split(",")
        add_to_inventory(inventory, inv_list)
        print_table(inventory)
    inv_file.closed


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open(filename, "w") as inv_file:
        inv_list = list_creator(inventory)
        inv = []
        for i in range(len(inv_list)):
            for j in range(inv_list[i][1]):
                inv.append(inv_list[i][0])
        inv_str = ",".join(inv)
        inv_file.write(inv_str)
