import random
from hangman_words import word_list


def select_random_word():
    return random.choice(word_list)
    return word_list[0]


print(select_random_word())


# a function where letters appear in a word
# Length of the word
# take input ask a player to pick a letter
# check if a letter has already been guessed
# after 1 game loop through - keeps score
# have a main function that plays the game
