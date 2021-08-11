def repeat_greeting(message="Hello!", number_of_times=3, upper=False):
    if upper:
        print(message * number_of_times)
    else:
        print(message * number_of_times)

# have to define all of the non-optional variables first

repeat_greeting()
repeat_greeting("Hello", 5, "True")
repeat_greeting("Hey There!")
repeat_greeting(upper=True)

# default arguments, e.g. defaults the legs to 4


class Dog:
    def __init__(self, name: str,
                 legs: int = 4
                 ):
        self.name = name
        self.legs = legs


fido = Dog("Fido")
stool = Dog("Stool", 3)
lassie = Dog("lassie")
