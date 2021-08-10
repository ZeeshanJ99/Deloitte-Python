# Sets
# similar to dictionary but if no colons its a set
# car_parts = {"wheels", "doors", "exhaust"}
# print(car_parts)
# print(type(car_parts))
#
# a = []
# b = ()
# c = {}
# print(type(c))
#
# # in order to define an empty set we need to use the set function
# # sets are unordered, cant index as 0 as there is no such thing in a set
#  # can add things, discard,
#
#  car_parts.add("windows")
#  car_parts.discard("wheels")
#  print(car_parts)

# # Frozenset - unordered and immutable
# fs = frozenset(['shrek', 'shrek 2' 'shrek 3'])
# print(fs)

# sets can only have unique values cant list same thing twice
# colours = {'Blue', 'Yellow', 'Green'}
# print(colours)
# colours.add("Blue")
# print(colours)
#
# # removes all same values
# alph =["A", "B", "A", "A", "A", "A"]
# print(alph)
# alph_set = set(alph)
# print(alph_set)
#
# # the in keyword provides a boolean to see whether or not something is in the dictionary
# # can check whether key is in dict but cant check whether value is in
# print("B" in alph)
# print("C" in alph)
