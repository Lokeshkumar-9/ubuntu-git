from ps3 import SCRABBLE_LETTER_VALUES
import random
from test_ps3 import test_is_valid_word
from test_ps3 import test_get_word_score
from test_ps3 import test_update_hand
from test_ps3 import test_wildcard


# Constants
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Function to load words from the words.txt file
def load_words():
    try:
        with open("words.txt", "r") as file:
            return file.read().splitlines()
    except IOError:
        print("Error: Could not load words.txt")
        return []

# Function to deal a new hand
def deal_hand():
    hand = []
    for _ in range(HAND_SIZE):
        letter = random.choice(list(SCRABBLE_LETTER_VALUES.keys()))
        hand.append(letter)
    return hand

# Function to calculate the score of a word
def calculate_word_score(word, hand_size):
    word_length = len(word)
    word_score = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word)
    second_component = 7 * word_length - 3 * (hand_size - word_length)
    if second_component < 1:
        second_component = 1
    return word_score * second_component

# Function to check if a word is valid
def is_valid_word(word, hand, word_list):
    word_freq = {}
    for letter in hand:
        word_freq[letter] = word_freq.get(letter, 0) + 1

    for letter in word:
        if word_freq.get(letter, 0) == 0:
            return False
        word_freq[letter] -= 1

    return word.lower() in word_list

# Function to play the game
def play_game():
    word_list = load_words()
    if not word_list:
        return

    hand = deal_hand()
    print("Current hand:", " ".join(hand))

    total_score = 0
    while True:
        word = input("Enter word or '.' to indicate you're finished: ")
        if word == '.':
            break

        if not is_valid_word(word, hand, word_list):
            print("Invalid word. Try again.")
            continue

        word_score = calculate_word_score(word, len(hand))
        total_score += word_score
        print(f"'{word}' earned {word_score} points. Total score: {total_score}")
        print()

    print("Total score:", total_score)

# Main function to start the game
if __name__ == "__main__":
    print("Loading word list from file...")
    words = load_words()
    print(len(words), "words loaded.")
    play_game()
