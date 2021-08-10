# % = modulo =the remainder - 15 % 3 == 0, 17 % 3 == 2


#fizzbuzz game
# FizzbuzzPrint every number from 1 to 100
# If divisible by 3,  print Fizz instead
# If divisible by 5, print Buzz instead
# If both?  FizzBuzz!

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

