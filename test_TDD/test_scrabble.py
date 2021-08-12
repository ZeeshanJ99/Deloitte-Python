from scrabble import word_calc
import pytest
w = word_calc()

@pytest.mark.parametrize("test_word, expected_score",
[
    ("HAPPY", 15),
    ("FOG", 7),
    ("FROG", 8),
    ("SPARTA", 8),
    ("GLOBAL", 9),
])
def test_word_calc(test_word, expected_score):
    assert word_score(test_word) == expected_score
    # assert word_calc("dog") == 5


# parameterize the @ iterates through the list




