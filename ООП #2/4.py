class Card:
    """ Одна игральная карта. """
    RANKS = ["Т", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "В", "Д", "K"]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666'] # ♠ ♣ ♥ ♦
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand:
    """ Рука: набор карт на руках у одного игрока. """
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep
    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nПервые две из моих карт я передал вам.")
print("Теперь у вас на руках:")
print(your_hand)
print("А у меня на руках:")
print(my_hand)
