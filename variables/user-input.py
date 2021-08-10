# name = input("what is your name?\n")
# age = int(input("how old are you?\n"))
# food = input("what do you like to eat?\n")
#
# print("Nice to meet you, " + name + " " + age + " " + food)
# print(age, type(age))

# use inputs to populate a dictionary
# print the dictionary
# print certain values from the dictionary

about_me = {
    "name": input("what is your name?\n"),
    "age": input("how old are you?\n"),
    "food": input("what do you like to eat?\n")
}
print(about_me)
print(about_me["age"])

