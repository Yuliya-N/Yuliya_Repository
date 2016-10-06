""" We create BlackJack game using Card and Deck classes as modules.
class PlayDeck(Deck) - is used to check that when 1/3 of deck is left, 
new deck.
card_value(rank) - returns the BlackJack value for each card
get_hand_value(cards) - returns the value the player has
new_game - variable that defines if to start new game or not
Changes:
class PlayDeck(Deck) >> line 26, 27 >> moved shuffle out 
line 96, 97 >> removed break
line 99, 114 >> dealer part starts only if player not lost

"""
from OOP_Card_Deck import Card, Deck
from random import shuffle


class PlayDeck(Deck):
    def __init__(self, decks_number=1):
        self._list = [
            Card(r, s) for s in self._suits for r in self._ranks
        ] * decks_number
        self._list_full = [
            Card(r, s) for s in self._suits for r in self._ranks
        ] * decks_number

    def draw(self):
        if len(self._list) <= len(self._list_full) / 3:
            self._list = self._list_full
            shuffle(self._list)
        return self._list.pop()


# def get_card_value(rank):
#     if rank in ('10', 'J', 'Q', 'K'):
#         return 10
#     elif rank in ('2', '3', '4', '5', '6', '7', '8', '9'):
#         return int(rank)
#     elif rank == 'A':
#         return 11
#     else:
#         print(rank)
#         raise ValueError('Unknown rank')


def get_hand_value(cards):
    value = 0
    aces = 0
    for card in cards:
        if card.rank in ('10', 'J', 'Q', 'K'):
            value += 10
        elif card.rank in ('2', '3', '4', '5', '6', '7', '8', '9'):
            value += int(card.rank)
        elif card.rank == 'A':
            value += 1
            aces += 1
        else:
            raise ValueError('Unknown rank')
    # changing ace rank if not enough value
    while value <= 11 and aces:
        aces -= 1
        value += 10
    # for k in range(aces):
    #     if value > 21:
    #         value -= 10
    return value 

if __name__ == '__main__':
    deck = PlayDeck(6) # need a test for PlayDeck 1/3 left
    # test: print(deck)
    shuffle(deck)
    new_game = 'y'

    while new_game == 'y':
        #cards giving
        player = []
        dealer = []
        player.append(deck.draw())
        dealer.append(deck.draw())
        player.append(deck.draw())
        # test player.append(Card('A', 'hearts'))
        dealer.append(deck.draw())
        
        #player part
        player_value = get_hand_value(player)
        print('You have:', player, 'it is: ', player_value)
        print('Casino has: ', dealer[1:])
        while player_value < 21:
            decision = input('Card? (y/n): ')
            if decision in ('y', 'yes'):
                player.append(deck.draw())
                player_value = get_hand_value(player)
                print('You have: ', player, 'it is: ', player_value)
            elif decision in ('n', 'no'):
                break
            else:
                print('Please, state y/n, yes/no')
        else:
            if player_value > 21:
                print('You lost!')
            else:
                print('You have 21')   
        
        # dealer part
        if player_value <=21:
            dealer_value = get_hand_value(dealer)
            print('Casino has: ', dealer, 'it is: ', dealer_value)
            if dealer_value < 21 and dealer_value < player_value: 
                while dealer_value < 21 and dealer_value < player_value:
                    dealer.append(deck.draw())
                    dealer_value = get_hand_value(dealer)
                    print('Casino has: ', dealer, 'it is: ', dealer_value)
                else:
                    if dealer_value > 21:
                        print ('You win!')
                    elif dealer_value > player_value:
                        print('You lost!')               
                    else:
                        print('Standoff')
        else:        
            new_game = input('Another game y/n: ')
    else:
        print('Thanks for the game! Come play again :)')


