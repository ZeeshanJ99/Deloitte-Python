# class Location:
#     def __init__(self, latitude, longitude) -> object:
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"location(latitude={self.latitude}, longitude={self.longtitude})"
#
#     def __str__(self):
#         return f"({self.longitude}, {self.longitude})"
# # represetation designed for developers,
# # useful for debugging/logging
#
#
# bham_academy = Location(latitude = 52.488647, longitude = -1.887249)
#
# print(bham_academy.__str__())
# print(repr(bham_academy))
# print(f"The Birmingham Academy is located at {bham_academy}")

# n = 0.003453
# print(f"Fixed Point: {n:f}")
# print(f"Exponential Notation: {n:f}")

class Cat:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old cat"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old cat"
        elif format_spec == "cat":
            return f"A {self.age * 5} cat-years old cat"
        else:
            return self.__str__()



whiskers = Cat(6)
print(whiskers)
print(f"Whiskers is {whiskers}")
print(f"Whiskers is {whiskers:dog}")
print(f"Whiskers is {whiskers:cat}")


