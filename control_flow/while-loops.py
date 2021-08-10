# a for loop iterates through an iterable
# a while loop will run forever
# as long as a condition is True

# x = 1
# while x < 10:
#     print(f"x is currently {x}")
#     x += 1
#     if x == 4:
#         break
#     print(f"x is now {x}")
#     x += 1

# this will loop forever dont click run, - because x is always less than 10
# with x += 1 it stops it once you get to 9
# break will break out of a while loop (with for)
# if ever do while True make sure to use a break statement

# with a while ______ whatever goes after needs to be something thats true or false
# .isdigit tells us whether every character in the string is a digit

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
