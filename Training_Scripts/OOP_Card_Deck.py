"""
"""
from random import shuffle

class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def __repr__(self):
        return "Card('{}', '{}')".format(self.rank, self.suite)


class Deck:
    _ranks = ('2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K', 'A')
    _suits = ('spades', 'hearts', 'clubs', 'diamonds')
    

    def __init__(self, number):
        self._list = [Card(r, s) for s in self._suits for r in self._ranks] * number

    def __repr__(self):
        return 'Deck({})'.format(len(self._list))

    def draw(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value
    
    # def __mul__(self, multiplicator):
    #     self._list *= multiplicator 
    #     return Deck()


# Tests
# deck = Deck(2)
# deck = deck * 3
# print(deck)
# card = deck.draw()
# print(card)
# print(len(deck))
# shuffle(deck)
# print(deck[10])

