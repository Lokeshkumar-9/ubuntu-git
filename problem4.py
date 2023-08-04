# Call the deal_hand function to get a hand with a wildcard
from Problem3 import is_valid_word
from ps3 import deal_hand


hand = deal_hand(7)  # You can specify the desired hand size

# Print the dealt hand
print("Dealt Hand:", hand)
# Define a sample word list
word_list = ["cows", "cats", "dogs", "cups"]

# Test the is_valid_word function with a word containing a wildcard
word = "c*wz"
isValid = is_valid_word(word, hand, word_list)
print(f"Is '{word}' valid? {isValid}")
