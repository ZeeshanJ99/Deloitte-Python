# four pillars
#
# Abstraction - use methods to make life easier
# Encapsulation - hide away dangerous things (hide things we dont want users to interact with directly)
# Inheritance -
# Polymorphism -

#
# # inheritance
# class Animal:
#     def __init__(self):
#         self.alive = True
#
#     def hunt(self):
#         print("Searching for food")
#
#     def move(self):
#         print("Moving...")
# #
# # # reptile is inheriting from animal
# #
# #
# class Reptile(Animal):
#     def __init__(self, reptile_type, colour):
#         super().__init__()
#         self.type = reptile_type
#         self.colour = colour
#
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breed(self):
#         print("Giving birth to live young")
#
# class Platypus(Mammal):
#     def __init__(self):
#         super().__init__()
#
#     def breed(self):
#         print("Laying eggs")
#
#
# perry = Platypus()
# perry.breed()
# m = Mammal()
# m.breed()

# this is polymorphism - changing a subclass - not locked into
# the methods of the previous class. we are overwriting the
# platypus class. polymorphism = method overwriting


# some other langauges do method overloading -
# python doesnt do this

# class Snake(Reptile):
#     def __init__(self, colour):
#         super().__init__("Snake", colour)
#
#
#
# s = Snake("green")
# print(s.type)


# a = Animal()
# a.hunt()
# a.move()

# r = Reptile("Snake")
# print(r.alive)
# r.hunt()
# r.move()


# a static method doesnt need to be associated with the class
# can work outside as a function
# a method is a function inside a class


# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def get_area(self):
#         return self.width * self.length
#
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
#
#
# r = Rectangle(10,20)
# print(r.get_area())
#
# s = Square(5)
# print(s.get_area())


# super is referring to the parent class - which is rectangle






# scrabble checker object
# initialise it with a string of 7 random letters
# a method to check that a submitted word can be made from those tiles
# A method to return the score for a submitted word
# a method to use the methods above to check a word is valid
# and if it is, return the score for that word

