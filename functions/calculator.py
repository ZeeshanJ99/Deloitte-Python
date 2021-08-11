# build a calculator by defining functions for the following
# addition
# subtraction
# multiply
# division

def add(int1, int2):
    return int1 + int2


def subtract(int1, int2):
    return int1 - int2


def multiply(int1, int2):
    return int1 * int2


def divide(int1, int2):
    return int1 / int2

# print(add(1, 4))
# print(subtract(1, 4))
# print(multiply(1, 4))
# print(divide(1, 4))


def calculator(instruction, int1, int2):
    if instruction == "add":
        return add(int1, int2)
    elif instruction == "subtract":
        return subtract(int1, int2)
    elif instruction == "multiply":
        return divide(int1, int2)
    elif instruction == "divide":
        return divide(int1, int2)

print(calculator("add", 2345, 345))