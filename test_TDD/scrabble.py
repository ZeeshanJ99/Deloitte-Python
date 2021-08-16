# one_point_values = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
# two_point_values = ['d', 'g']
# three_point_values = ['b', 'c', 'm', 'p']
# four_point_values = ['f', 'h', 'v', 'w', 'y']
# five_point_values = ['k']
# eight_point_values = ['j', 'x']
# ten_point_values = ['q', 'z']
#
#
#
# class Scrabble():
#
#     def __init__(self):
#         self.point = 0
#         self.name
#         self.tiles = 7
#         self.tiles = []
#         self.add_tiles
#
#     def get_num_of_tiles(self):
#         print(f"(self.name) has (self.tiles) tiles")
#
#     def word_calc(self, word):
#         for letter in word:
#             for one_point in one_point_values:
#                 if letter == one_point:
#                     self.point = self.point+1
#             for two_point in two_point_values:
#                 if letter == two_point:
#                     self.point = self.point+2
#             for three_point in three_point_values:
#                 if letter == three_point:
#                     self.point = self.point+3
#             for four_point in four_point_values:
#                 if letter == four_point:
#                     self.point = self.point + 4
#             for five_point in five_point_values:
#                 if letter == five_point:
#                     self.point = self.point + 5
#             for eight_point in eight_point_values:
#                 if letter == eight_point:
#                     self.point = self.point + 8
#             for ten_point in ten_point_values:
#                 if letter == ten_point:
#                     self.point = self.point + 10
#             return self.point

# def valid_word(self, letter):
#     if letter in self.word:
#         return self.point

#
# w = word()
# w.word_calc()
# print(w.get_points())


# davids scrabble

import random
import string


class ScrabbleHand:
    def __init__(self):
        self.tiles = ""
        for x in range(7):
            self.tiles += random.choice(string.ascii_uppercase)

    def get_tiles(self):
        return self.tiles

    def is_valid_word(self, word_check):
        word_check_list = list(word_check)
        tile_list = list(self.tiles)
        for char in word_check:
            if char not in self.tiles:
                return False
            else:
                tile_list.remove(char)
            return True

    def get_score(self, word):
        total_score = 0
        score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
        for letter in word:
            total_score += score[letter.lower()]
        return total_score


if __name__ == "--main--":
    s = ScrabbleHand()
    print(s.get_tiles())
