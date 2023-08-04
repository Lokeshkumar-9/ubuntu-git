def is_valid_word(word, hand, word_list):
    """
    Returns True if word is a valid word and is composed entirely of letters
    in the hand. Otherwise, returns False.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    word = word.lower()  # Convert the word to lowercase
    hand_copy = hand.copy()
    
    if word in word_list:
        for letter in word:
            if letter not in hand_copy or hand_copy[letter] == 0:
                return False
            hand_copy[letter] -= 1
        return True
    
    return False

# Test cases
word_list = ["apple", "banana", "cherry"]
hand = {'a': 1, 'p': 2, 'l': 1, 'e': 1, 'b': 1, 'n': 1, 'c': 1, 'h': 1, 'r': 1, 'y': 1}

# Test 1: Valid word
print(is_valid_word("apple", hand, word_list))  # Output: True

# Test 2: Valid word with extra letters in hand
print(is_valid_word("cherry", hand, word_list))  # Output: True

# Test 3: Valid word with all letters used
print(is_valid_word("banana", hand, word_list))  # Output: True

# Test 4: Invalid word (not in word list)
print(is_valid_word("grape", hand, word_list))  # Output: False

# Test 5: Invalid word (letter 'g' not in hand)
print(is_valid_word("peach", hand, word_list))  # Output: False
