class Turn:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def cards_played(self):
        return self.cards
