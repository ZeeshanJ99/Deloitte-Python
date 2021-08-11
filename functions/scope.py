# def square(num):
#     result = num ** 2
#     return result
#
# print(square(10))



# LEGB rule
# local
# enclosed
# global
# built-in

# local scope is stuff defined only for functions
# we can define functions inside of another function


var = 1000

def get_var():
    var = 5
    return var

print(get_var())
print(var)


# debug, modules, special variables - whenever you call
# a variable starts with __ (double _)


