classes bring functions and data together
unlike functions and variables classes use uppercase
(start with capital letters e.g. WonderDog)
# class Dog:
#     animal_type = "canine"
#
# # Initialisation
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#         self.legs = 4
#         self.animal_type
# # self is in so that we can set the names belonging to the object
#
#     def bark(self):
#         return f"Woof! I am {self.name}"


# can call methods inside other methods, everything within a class is defined at once
# the order within a class doesnt matter

# fido = Dog("Fido", "Black")
# lassie = Dog("Lassie", "Brown")
#
# print(fido.name)
# print(fido.colour)
# print(fido.legs)
# fido.legs = 3
# print(fido.legs)
# print(lassie.legs)
# print(lassie.name)
# print(lassie.colour)
#
#
# print(lassie.bark())
# when you print dont need self


# print(Dog)
# print(Dog.animal_type)
# print(Dog.bark)
#
#
#
# # self means referring to the current class. what is happening
# # whenevr u have a method the first argument it takes in is itself,
# # the class it belongs to
#
# # Instantiation - creating an instance of an object
#
# fido = Dog()
# lassie = Dog()
#
#
# print(fido)
# print(type(fido))
# # print(fido.animal_type)
# print(fido.bark())

# class is like a cookie cutter - can change a cookie
# wont affect anything else

# fido = Dog()
# lassie = Dog()
#
# print(fido.animal_type)
# print(lassie.animal_type)
#
# Dog.animal_type = "arachnid" # dangers of using classes
#
# print(fido.animal_type)


# define a shopping cart class
# it should initialise with empty 'contents' collection
# provide a method so that i can add things to the cart
# provide a method so that i can see whats in the cart


class Product:
    def __init__(self, price, name, brand):
        self.price = price
        self.name = name
        self.brand = brand


class ShoppingCart:
    def __init__(self):
        self.contents = []
# using an self._contents - hides it in a way- discourages user from using it

    def add_cart(self, new_item):
        self.contents.append(new_item)

    def show_cart(self):
        for product in self.contents:
            print(f"{product.name} from {product.brand}: £{product.price:.2f}")

    def get_cart_total(self):
        cart_total = 0.0
        for product in self.contents:
            cart_total += product.price
        return cart_total


sc = ShoppingCart()
sc.add_cart(Product(4.75, "Chicken", "Morrisons"))
sc.add_cart(Product(2.22, "Pizza", "Chicago Town"))
sc.show_cart()
print(sc.get_cart_total())


# __repr__ and __init__ are known as methods




