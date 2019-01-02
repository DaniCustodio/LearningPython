from random import shuffle
class Card():
    valid_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    valid_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, suit, value):
        if suit not in Card.valid_suits:
            raise ValueError('Invalid suit!')
        elif value not in Card.valid_values:
            raise ValueError('Invalid value!')
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck():
    def __init__(self):
        self.cards = []
        for suit in Card.valid_suits:
            for v in Card.valid_values:
                self.cards.append(Card(suit, v))
    
    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, num_cards):
        deal_cards = []
        if len(self.cards) == 0:
            raise ValueError('All cards have been dealt')
        if num_cards > len(self.cards):
            num_cards = len(self.cards)
        for num in range(0, num_cards):           
            deal_cards.append(self.cards.pop())
        return deal_cards
    
    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError('Only full decks can be shuffled')     
        shuffle(self.cards)
        return self
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, ncards):
        self.ncards = ncards
        return self._deal(self.ncards)

        