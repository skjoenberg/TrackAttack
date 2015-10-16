from LogConstants import state
from Log import SearchError

class LogReader:
    def __init__(self, log):
        self.log = log

    # Refreshes the log
    def _refresh(self):
        self.log.refresh()

    # Returns the beginning line of the latest game
    def game_beginning(self):
        self._refresh()
        games = self.log.search(0, state('game_begin'))
        if games != []:
            return games[-1][1]
        else:
            return -1

    # Returns the length of the log-file
    def length(self):
        self._refresh()
        return self.log.length()

    # Checks whether the line have information about cards you have played
    def played_self(self, line):
         try:
             return (1, self.log.get_entity(state('played_self'), 'name', line))
         except SearchError:
             pass
         else:
             return None

    # Checks whether the line have information about cards opponent have played
    def played_oppo(self, line):
        try:
            return (2, self.log.get_entity(state('played_oppo'), 'name', line))
        except SearchError:
            pass
        else:
            return None

    # Checks whether the line have information about a turn switch
    def next_turn(self, line):
        try:
            self.log.get_entity(state('turn'), '', line)
            return True
        except SearchError:
            pass
        else:
            return False
