import string
from ps3 import SCRABBLE_LETTER_VALUES

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the product of two components:
    - First component: the sum of the points for letters in the word.
    - Second component: either [7 * word_length - 3 * (n - word_length)] or 1,
      whichever value is greater, where:
      - word_length is the number of letters used in the word.
      - n is the number of letters available in the current hand.

    word: string (lowercase letters)
    n: integer (total number of letters in the hand)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    
    second_component = max(1, 7 * len(word) - 3 * (n - len(word)))
    score *= second_component
    
    return score
word = "example"
n = 10
score = get_word_score(word, n)
print("Word score:", score)

