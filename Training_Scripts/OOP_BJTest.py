from OOP_BlackJack import get_hand_value
from OOP_Card_Deck import Card

if __name__ == '__main__':
    hand = [Card('9', 'spades'), Card('8', 'spades'), Card('A', 'spades')]
    assert get_hand_value(hand) == 18

    hand = [Card('7', 'spades'), Card('2', 'spades'), Card('A', 'spades')]
    assert get_hand_value(hand) == 20

    hand = [Card('Q', 'spades'), Card('A', 'spades')]
    assert get_hand_value(hand) == 21

    hand = [Card('A', 'spades'), Card('A', 'spades')]
    assert get_hand_value(hand) == 12

    hand = [Card('A', 'spades')]*4
    assert get_hand_value(hand) == 14
