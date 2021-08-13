from scrabble import ScrabbleHand

class ScrabbleGame:
    def __init__(self):
        self.total_score = 0

    def single_round(self):
        self.hand = ScrabbleHand()
        print(self.hand.get_tiles())
        self.guess = self.get_word_guess()
        score = self.hand.get_score(self.guess)
        self.total_score += score

    def get_word_guess(self):
        #as the user to input a guess
    # use self.hand.is_valid_word to check its valid
    # loop until valid
    # return the guess
        pass

    def main(self):
        while True:
            self.single_round()
            new_round = self.ask_to_play_again()
            if not new_round:
                break
            print(self.exit_message())
