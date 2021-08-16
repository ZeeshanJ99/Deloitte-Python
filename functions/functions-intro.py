# in order to create a funtion
# we need to define it
# function names use snakecase-
# lowercase with _
# need round brackets and colon
#
# once we define it can use it later, define functions
# at the top
# customise how function behaves by giving it input
# nothing special about word its the name of the variable

# def print_something(word1, word2):
#     print("print")
#     print(word1)
#     print(word2)
#     print("")
#
# print("This is outside the function definition")
#
# print_something("dog", "woof")
# print_something("cat", "meow")
# print_something("rabbit", "squeak")
# print_something("mouse", "squeak")


# def add_plus_one(int1, int2):
#     return int1 + int2 + 1
#     return a


# print(add_plus_one(4, 6)) or can
# x = add_plus_one(4, 6)


# print(add_plus_one(5,5))
# print(add_plus_one(7,23))
#
# def add_plus_one(int1: int, int2: int) -> int:
#     return int1 + int2 + 1
#     return a
#
# # can add type hints to help with str, dont control anything they are just hints
# print(add_plus_one(5,5))
# print(add_plus_one(7,23))
# print(add_plus_one("hello"))

# multiple arguments, we put a *
# in front of whatever its gonna be
# the star tells it its gonna accept any variables

# def handle_multi(*multiargs):
#     print(multiargs)
#     for arg in multiargs:
#         print(arg)
#
# handle_multi(1, 2, 3)


# i want to write a function to
# calculate the average values
#
# def average(*multiargs):
#     total = 0
#     count = 0
#     for arg in multiargs:
#         total += arg
#         count += 1
#     return total / count
#
# print(average(1, 4, 6))







