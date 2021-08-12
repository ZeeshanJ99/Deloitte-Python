one_point_values = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
two_point_values = ['d', 'g']
three_point_values = ['b', 'c', 'm', 'p']
four_point_values = ['f', 'h', 'v', 'w', 'y']
five_point_values = ['k']
eight_point_values = ['j', 'x']
ten_point_values = ['q', 'z']



class Scrabble:
    def __init__(self):
        self.point = 0

    def word_calc(self, word):
        for letter in word:
            for one_point in one_point_values:
                if letter == one_point:
                    self.point = self.point+1
            for two_point in two_point_values:
                if letter == two_point:
                    self.point = self.point+2




            for three self.point in three_point_values:
                if (letter == three_point):
                    point = point + 3
            for four point in four_point_values:
                if (letter == four_point):
                    point = point + 4
            for five point in five_point_values:
                if (letter == five_point):
                    point = point + 5
            for eight point in eight_point_values:
                if (letter == eight_point):
                    point = point + 8
            for ten point in ten_point_values:
                if (letter == ten_point):
                    point = point + 10
            return point

        return self.point

    # def valid_word(self, letter):
    #     if letter in self.word:
    #         return self.point

#
# w = word()
# w.word_calc()
# print(w.get_points())