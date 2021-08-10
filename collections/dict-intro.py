# Dictionaries

# Dictionary = a collection of Key-Value Pairs, only can look up key first then the value  like a real life dictionary
# we seperate key value pairs with commas
# with pycharm we can't have duplicate keys
# about_me = {
#     "name": "Zeeshan",
#     "age": 22,
#     "favourite food": "Pizza",
#     "job": "SRE"
# }
#
# print(about_me)
#
# # to access the value in a dictionary - dictionary name, square brackets, key
# print(about_me["age"])
#
# print(about_me.get("age"))
# # when you use get and return a key that you dont have it returns none, square brackets returns an error
#
# # changing values, can replace and set keys which dont exist
# about_me.update({"age": 60, "favourite food": "Sushi"})
# about_me["eye colour"] = "Brown"
# print(about_me)


# favourite_film = {"Name": "Resevoir Dogs",
#                "Director": "Quentin Tarantino",
#                "Date released": "1992"
#                }
#
# print(favourite_film)
#
# favourite_film.update({"Main Character": "Mr Pink"})
# print(favourite_film)

sre = {
    "course name": "Deloitte SRE",
    "length": 12,
    "trainees": ["zeeshan, will, kieron"],
    "outline": {
        "week 1": "business week",
        "week 2": "Linux",
        "week 3": "Python"
    }
}
print(sre)

# can have a dictionary as a value within a dictionary as well
# e.g. outline dictionary above

# returns a list of keys/values
print(sre.keys())
print(sre.values())

# changes format of dictionary - returns a list of tuples which is the key and then the value
print(sre.items())
