# Lambda functions

# def add(n1, n2):
#     return n1 + n2
#
#
# print(add(2, 4))
#
# add = lambda n1, n2: n1 + n2
# print(add(2, 4))

# anonymous function - when you dont
# want to write a full function out


# Map - takes in a function, map needs a function and an iterable
# def double_add_one(n):
#     return (n * 2) + 1
#
nums = [1, 2, 3, 4, 5]
# new_nums = list(map(double_add_one, nums))
# print(list(new_nums))
#
# new_nums = list(map(lambda n: (n * 2) + 1, nums))
# print(new_nums)

savings = [234.00, 555.00, 674.00, 78.00]
# savings = each saving plus 10%
# implement this using map and a lambda function

new_savings = list(map(lambda s: (s * 1.1), savings))
print(new_savings)


# Filter - keeps the ones that are true
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, nums)))
# write the above using a lambda function
print(list(filter(lambda x: x % 2 == 0, nums)))


print(list(filter(lambda y: y > 200,
    filter(
    lambda x: x % 2 == 0, range(210)
))))


# if its simple enough to express in
# 1 line of code use a lambda



# AND NOW FOR SOMETHING COMPLETELY DIFFERENT

# List Comprehension - flattened for loop,
# does similar to lambda

savings = [234.00, 555.00, 674.00, 78.00]
bonus = [x + x/10 for x in savings]
print(bonus)


large_savings = [x for x in savings if x > 500]
print(large_savings)

large_savings_bonus = [x + x/10 for x in savings if x > 500]
print(large_savings_bonus)
