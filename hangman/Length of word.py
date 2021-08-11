import random
from hangman_words import word_list


def select_random_word():
    return random.choice(word_list)


print(select_random_word())

# gives random word




