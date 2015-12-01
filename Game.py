import math
from Turn import Turn
from time import gmtime, strftime

class Game:
    def __init__(self):
        self.coin_used = False
        self.turn = 0
        self.turns_self = []
        self.turns_oppo = []

    # Creates a new turn for the current player
    def _new_turn(self, player):
            if (player == 1):
                self.turns_self.append(Turn(math.floor(self.turn/2)))
            else:
                self.turns_oppo.append(Turn(math.floor(self.turn/2)))

    # Plays a card for a current player on a given turn
    def play(self, player, card, turn):
        if (turn > self.turn):
            self.turn = turn
            self._new_turn(player)
        if (turn == self.turn):
            if player == 1:
                self.turns_self[-1].add_card(card)
            else:
                self.turns_oppo[-1].add_card(card)

    # Returns all cards played during the game.
    # Returns a tuple (your cards, opponents cards)
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

    # Exports the game in turns to a log file
    def export(self):
        time = strftime("%d-%m-%Y-%H:%M:%S", gmtime())
        path = "log/" + "hearthstone" + time + ".txt"
        yolo = ""
        f = open(path, "w")
        for turn in self.turns_self:
            yolo += "You played [turn " + str(turn.num) + "]:\n"
            for card in turn.cards_played():
                yolo += str(card) + "\n"

        turn_num = 1
        for turn in self.turns_oppo:
            yolo += "Your opponent played [turn " + str(turn.num) + "]:\n"
            for card in turn.cards_played():
                yolo += str(card) + "\n"
        f.write(yolo)
        f.close
