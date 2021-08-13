import os

parent_dir = os.path.dirname(__file__)
# filepath = os.path.join(parent_dir + "/lunch_order.txt")

# file gives address of current file,
# dir name gives directory that the file is in


# file = open(os.path.join(parent_dir + "/lunch_order.txt"))
# data = list(map(lambda x : x.strip("/n"), file.readlines()))
# print(data)
# file.close()

# with open(filepath) as file:
#     data = list(map(lambda x: x.strip("/n"), file.readlines()))
#     print(data)
# print("The file has now been closed")
# another way of closing the file

# filepath = os.path.join(parent_dir + "/lunch_order.txt")

# try:
#     with open(filepath, "") as file:
#         data = list(map(lambda x: x.strip("/n"), file.readlines()))
# except FileNotFoundError as errmsg:
#     print("Could not find the right file", errmsg)
# finally:
#     print("this will happen if there is or isnt an error")

# finally is very rarely used


# r = Open for reading
# w = open for writing - once you open it it completely empties file out, overwrites it
# x = eXclusive creation - creates a new file (fails if already exists)
# a = appending (instead of overwriting)
# t = text mode (combined with above)
# b = binary mode
# + = updating (reading AND writing)

# with open(filepath, "r") as file:
#     data = file.read()
#     print(data, type(data))

# filepath = os.path.join(parent_dir + "/lunch_order.txt")


# def add_order_to_file(filepath, order_item):
#     try:
#         with open(filepath, "a") as file:
#             file.write(order_item + "\n")
#     except FileNotFoundError:
#         print("Get the file path right you fool")
#         raise


# add_order_to_file("Zeeshan.txt", "Eggs on Toast") # creates a new file with x

# add_order_to_file(filepath, "Eggs on Toast")
# add_order_to_file(filepath, "Quiche")


# Read from a drinks_order file (drinks_order.txt)
# check that each drink in the order is available
# in the drinks menu.txt
# what should happen if it isnt

filepath = os.path.join(parent_dir + "/drinks_menu.txt")


#
def available_drinks(filepath, drink):
    try:
        with open(filepath, "a") as file:
            file.write(drink)
        if drink in filepath:
            print("Here you go")
    except FileNotFoundError:
        print(f"The {drink} you ordered is not available")


available_drinks(filepath, "water")


# def available_drinks(filepath, drink):
#     try:
#         with open(filepath, "r+") as file:
#             drinks_menu = [drink.strip("\n") for drink in file.readlines()]
#             if drink not in drinks_menu:
#                 print(f"The {drink} you ordered is not available")
#             else:
#                 print("Here you go")
#
# available_drinks("filepath", "Pepsi")


# try:
#     with open(filepath) as file:
#         data = list(map(lambda x: x.strip("/n"), file.readlines()))
#         print(data)
#     print("The file has now been closed")
#     print(data[0])
# except FileNotFoundError as errmsg:
#     print("Could not find the right file")
#     print(errmsg)
#     data = []
#     raise
# except IndexError as errmsg:
#     print("Order file is currently empty!")
#
# print(data)

# tool for handling errors
# if theres a possibility of things to break then

# data = file.read()
# print(data, type(data))
# data = file.readline() # next line in buffer as a string
# data = file.read()
# print(data, type(data))
# data = file.readlines() # processed all of lines in document
# and made each line into a string. /n = new line character -

# data = file.readlines()
# # print(data)
# # line_1 = data[0].strip("/n") # how to remove the/n
# # print(line_1)
# # line_2 = data[1].strip("/n")
# # print(line_2)
# file.close()

# print(file.read) gets contents of file
# a buffer holds onto data until it is read, if you read
# and try to read again it is gone as its read the first time
# file is the object that is read. e.g. printer is a buffer - as soon as you print a
# document it forgets it - temporary memory. once its gone its gone

#
# data = file.readlines()
# file.close()
