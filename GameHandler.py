from Game import Game
from LogReader import LogReader

class GameHandler:
    def __init__(self, log):
        self.game  = Game()
        self.reader = LogReader(log)
        self.begin  = -1
        self.line   = -1
        self._first_game = True

    # Checks whether a game has begun
    def _new_game(self):
        return (self.reader.game_beginning() != self.begin)

    # Creates a new game objects
    def _create_new_game(self):
        self.game  = Game()
        self.begin = self.reader.game_beginning()
        self.line  = self.reader.game_beginning()
        self.turn  = 1
        self._first_game = False

    # Handles each new line in the log
    def _handle_news(self, line):
        if (self.reader.played_self(line) != None):
            cur_play = self.reader.played_self(line)
            self.game.play(cur_play[0], cur_play[1], self.turn)
        elif (self.reader.played_oppo(line) != None):
            cur_play = self.reader.played_oppo(line)
            self.game.play(cur_play[0], cur_play[1], self.turn)
        elif (self.reader.next_turn(line)):
            self.turn += 1

    # Updates game information
    def update(self):
        if (self._new_game()):
            if (not self._first_game):
                self.game.export()
            self._create_new_game()

        elif (self.line != self.reader.length()):
            for line in range(self.line, self.reader.length()):
                self._handle_news(line)
                self.line += 1

    # Returns all the cards played (used for UI)
    def info(self):
        if (self.line != -1):
            return self.game.cards_played()
        else:
            return ([],[])
