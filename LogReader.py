from LogConstants import state
from Log import SearchError

class LogReader:
    def __init__(self, log):
        self.log = log

    def _refresh(self):
        self.log.refresh()

    def game_beginning(self):
        self._refresh()
        games = self.log.search(0, state('game_begin'))
        if games != []:
            return games[-1][1]
        else:
            return -1

    def length(self):
        self._refresh()
        return self.log.length()

    def played_self(self, line):
         try:
             return (1, self.log.get_entity(state('played_self'), 'name', line))
         except SearchError:
             pass
         else:
             return None

    def played_oppo(self, line):
        try:
            return (2, self.log.get_entity(state('played_oppo'), 'name', line))
        except SearchError:
            pass
        else:
            return None

    def next_turn(self, line):
        try:
            self.log.get_entity(state('turn'), '', line)
            return True
        except SearchError:
            pass
        else:
            return False
