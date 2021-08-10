# IF
# if age is below 15 then codes wont run
# else is triggered if the if statement isnt
# elif = else if

# age = 14
#
# if age >= 15:
#     print("you can watch this violent film")
#     print("This is still in the if statement block")
# elif age == 14:
#     print("come back next year")
# else:
#     print("you are too young")
#     print("still part of else-block")
#
# print("this will always run")

# film_rating = "U"

# An if-else block to check the film rating
# and print a corresponding description for who can watch
# U, PG, 12A, 15, 18


# switch age:
# case "U":
#    do something
# | is the same as or


# Get user input for their age and the film certificate
# print an appropriate message
# think about how to handle casting inputs (when you want to go from str to integers)
# try to make the code robust (idiot proof)


prompt_user = True

while prompt_user:
    age = input("What is your age?\n")
    if age.isdigit():
        if int(age) < 120:
            age = int(age)
            prompt_user = False
        else:
            print("don't be silly")
    else:
        print("please provide age in digits")

film_certificate = input("What certificate movie are you watching\n")
if age >= 18:
    print("You can watch all movies")
elif age >= 15 and (film_certificate == "U" or film_certificate == "PG" or film_certificate == "12A" or
                    film_certificate == "15" or film_certificate == "18"):
    print("You can only watch U, PG, 12A and 15 movies!")
elif age >= 12 and (film_certificate == "U" or film_certificate == "PG" or film_certificate == "12A" or
                    film_certificate == "15" or film_certificate == "18"):
    print("You can only watch U, PG and 12A movies")
elif age >= 10 and (film_certificate == "PG" or film_certificate == "12A" or
                    film_certificate == "15" or film_certificate == "18"):
    print("You can only watch U and PG movies")
elif age < 9 and (film_certificate == "PG" or film_certificate == "12A" or
                  film_certificate == "15" or film_certificate == "18"):
    print("You can only watch U movies")
