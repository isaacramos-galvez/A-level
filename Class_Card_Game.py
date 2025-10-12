import random
card_numbers = []
class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self): 
        """ return a string 'C', 'S', 'H', 'D' """
        suits = ['S','H','D','C']
        return suits[self._card_number//13]

    def get_value(self): 
        """ return a string 'A', ... '10', 'J', 'Q', 'K' """
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return value[self._card_number/13]

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return card.get_value() + card.get_suit()
        
    def get_long_name(self, value, suit):
        """ return card name eg 'Ten of Diamonds' """
        new_variables = [
        C = "Clubs"
        S = "Spades"
        D = "Diamonds"
        H = "Hearts"
        A = "Ace"
        1 = "One"
        2 = "two"
        3 = "Three"
        4 = "Four"
        5 = "five"
        6 = "Six"
        7 = "Seven"
        8 = "Eight"
        9 = "Nine"
        10 = "Ten"
        J = "Jack"
        Q = "Queen"
        K = "King"]
        return card.replace(new_variables)

class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        return len(class_list)

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        top_card = self._card_list.pop()
        return top_card

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        add_card = self._card_list.append(new_card)
        return add_card 


card = Card(1)
print(card.get_suit())
print(card.get_value())
print(card.get_short_name())
deck = Deck()
deck.shuffle_deck()
for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_short_name())