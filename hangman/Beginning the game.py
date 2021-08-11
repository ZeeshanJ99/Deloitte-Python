import random
from hangman_words import word_list


def word():
    return random.choice(word_list)


allowed_errors = 8
guesses = []
done = False

while not done:
    for letter in word():
        if letter.upper() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors left {allowed_errors}, Next Guess: ")
    guesses.append(guess.upper())
    if guess.upper() not in word():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word():
        if letter.upper() not in guesses:
            done = False

    if done:
        print(f"You found the word, Congratulations!!!")
    elif():
        print(f"Game Over, you failed the word was {word()}")


