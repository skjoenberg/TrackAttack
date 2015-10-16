from Turn import Turn

class Game:
    def __init__(self):
        self.coin_used = False
        self.turn = 0
        self.turns_self = []
        self.turns_oppo = []

    def _new_turn(self, player):
            if (player == 1):
                self.turns_self.append(Turn())
            else:
                self.turns_oppo.append(Turn())

    def play(self, player, card, turn):
        if (turn > self.turn):
            self.turn = turn
            self._new_turn(player)
        if (turn == self.turn):
            if player == 1:
                self.turns_self[-1].add_card(card)
            else:
                self.turns_oppo[-1].add_card(card)

    def cards_played(self):
        cards_self = []
        cards_oppo = []

        for turn in self.turns_self:
            for card in turn.cards_played():
                cards_self.append(card)
        for turn in self.turns_oppo:
            for card in turn.cards_played():
                cards_oppo.append(card)

        return (cards_self, cards_oppo)


    def export(self):
        f = open('lol', 'w')
        yolo = ""
        turn_num = 1
        for turn in self.turns_self:
            yolo += "You played [turn " + str(turn_num) + "]:\n"
            for card in turn.cards_played():
                yolo += str(card) + "\n"
        for turn in self.turns_oppo:
            yolo += "Your opponent played [turn " + str(turn_num) + "]:\n"
            for card in turn.cards_played():
                yolo += str(card) + "\n"
        f.write(yolo)
        f.close
