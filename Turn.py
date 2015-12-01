class Turn:
    def __init__(self, num):
        self.num = num
        self.cards = []

    # Adds card to turn
    def add_card(self, card):
        self.cards.append(card)

    # Returns the cards played in a turn
    def cards_played(self):
        return self.cards
