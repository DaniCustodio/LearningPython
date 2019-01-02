from random import randint
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
        for num in range(0, num_cards):
            if num_cards > len(self.cards):
                raise ValueError('All cards have been dealt')
            deal_cards.append(self.cards.pop())
        return deal_cards
    
    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            for i in range(0, 1000):
                a = randint(0,52)
                b = randint(0,52)
                aux = self.cards[a]
                self.cards[a] = self.cards[b]
                self.cards[b] = aux
        return self.cards
    
    def deal_card(self):
        return self._deal(1)
    
    def deal_hand(self, num_cards):
        self.num_cards = num_cards
        return self._deal(self.num_cards)

"""my_deck = Deck()
card = my_deck.deal_card
print(card)
print(my_deck)"""
        