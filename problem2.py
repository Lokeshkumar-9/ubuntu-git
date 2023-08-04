def update_hand(hand, word):
    # Create a copy of the original hand to avoid modifying it directly
    new_hand = hand.copy()

    # Iterate over each letter in the word and update the new_hand accordingly
    for letter in word:
        new_hand[letter] = new_hand.get(letter, 0) - 1

    # Remove letters with zero or negative count from the new_hand
    new_hand = {letter: count for letter, count in new_hand.items() if count > 0}

    return new_hand

def display_hand(hand):
    for letter, count in hand.items():
        for _ in range(count):
            print(letter, end=" ")
    print()

hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
print("Original hand:")
display_hand(hand)

word = 'quail'
new_hand = update_hand(hand, word)
print("\nNew hand after spelling the word 'quail':")
display_hand(new_hand)

word = 'jolly'
hand = {'j': 2, 'o': 1, 'l': 1, 'w': 1, 'n': 2}
print("\nOriginal hand:")
display_hand(hand)

new_hand = update_hand(hand, word)
print("\nNew hand after spelling the word 'jolly':")
display_hand(new_hand)
