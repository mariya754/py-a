import cards

class BJ_Card(cards.Positionable_Card):

    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v

class BJ_Deck(cards.Deck):

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card_RANKS:
                self.cards.append(BJ_Cards(rank, suit))

class BJ_Hand(cards.Hand):

    def __init__(self, name):
        super(BJ_Hand, self).___init__()
        self.name = name

    def __str__(self):
        rep = self.name +".\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):

        for card in self.cards:
            if not card.value:
                return None

        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if cards.value == BJ_Card.ACE_VALUE:
                contains_ace = True


        if contains_ace and t <=11:
            t += 10

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """ Игрок в Блэк Джек. """
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name +
            ", будете брать ещё карты?")
        return response == "y"

    def bust(self):
        print(self.name, "перебрал(а.")
        self.lose()

    def lose(self):
        print(self.name, "проиграл(а).")

    def win(self):
        print(self.name, "выиграл(а).")

    def push(self):
        print(self.name, "сыграл(а) с диллером вничью.")

class BJ_Dealer(BJ_Hand):
    """ Диллер в Блэк Джек. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал(а).")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
        