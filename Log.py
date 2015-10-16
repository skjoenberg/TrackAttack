import os
import re

class SearchError(Exception):
    pass

class Log:
    def __init__(self, log_path):
        self.path = log_path
        self.data = open(self.path).read().splitlines()
        self.last_modification = os.stat(self.path)[-2]

    # Refreshes log-data
    def refresh(self):
        self.last_modification = os.stat(self.path)[-2]
        self.data = open(self.path).read().splitlines()

    # Checks wheter the log have been modified
    def modified(self):
        print
        return (self.last_modification != os.stat(self.path)[-2])

    # Returns the length of the log-file
    def length(self):
        return len(self.data)

    # Get the value of an entity
    def get_entity(self, regex_string, entity, line):
        regex = re.compile(regex_string)
        match = regex.match(self.data[line])
        if match:
            if (entity != ""):
                return match.group(entity)
            else:
                return ""
        else:
            raise SearchError("Entity not found")

    # Search the log with regex
    def search(self, start_line, regex):
        result = []
        current_line = start_line
        for line in range(start_line, self.length()):
            try:
                match = self.get_entity(regex, '', line)
                result.append((match, current_line))
            except SearchError:
                continue
            finally:
                current_line += 1
        return result
