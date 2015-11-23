import threading
import time
import sys
import os
from Log import Log
from Game import Game
from GameHandler import GameHandler

class UI:
    def __init__(self, log_path):
        self.lock = threading.Lock()
        self.last_info = ""
        self.exit = False
        self.handler = GameHandler(Log(log_path))

    # Clears the output
    def _clear_output(self):
        os.system("clear")

    # Used for printing cards
    def _pretty_list(self, a):
        count = 0
        a = sorted(a)
        result = ""
        for index in range(1,len(a)+1):
            count += 1;
            if (str(a[index-1]) == "The Coin"):
                count = 0
                break;
            if ((index == len(a)) or (str(a[index]) != str(a[index-1]))):
                if (count == 1):
                    result += str(a[index-1]) + "\n"
                else:
                    result += str(count) + "x " + str(a[index-1]) + "\n"
                count = 0
        return result

    # Creates a pretty output string
    def _info(self):
        # if :
        #     pretty_coin = "Coin played." + "\n" * 2
        # else:
        #     pretty_coin = "Coin not played." + "\n" * 2
        cards = self.handler.info()
        pretty_played_self = "### Self ###\n" + self._pretty_list(cards[0]) + "\n"
        pretty_played_oppo = "### Opponent ###\n" + self._pretty_list(cards[1]) + "\n"
        return pretty_played_self + pretty_played_oppo

    # Input
    def input_thread(self):
        while(not (self.exit)):
            keypress = ord(sys.stdin.read(1))
            if keypress==10:
                self.lock.acquire()

                self._clear_output()
                input_command = input('Enter command: ')
                self._clear_output()

                self.handler.update()
                if input_command.startswith("search"):
                    search = input_command[7:]
                    print("You played: ")
                    print([x.lower() for x in self.game.played_self].count(search))
                    print("Opponent played: ")
                    print([x.lower() for x in self.game.played_oppo].count(search))

                elif input_command == "oppo":
                    self._clear_output()
                    print("Opponent played:")
                    print(self._pretty_list(self.game.played_oppo))

                elif input_command == "self":
                    self._clear_output()
                    print("You played:")
                    print(self._pretty_list(self.game.played_self))
                elif input_command == "exit":
                    exit = True
                    break
                else:
                    print("Not a valid command")

                input("\nPress any key to return")

                self._clear_output()
                self.last_info = self._info(self.game)
                print(self.last_info)
                self.lock.release()

    # Output
    def output_thread(self):
        print(self._info())
        while(not self.exit):
            self.handler.update()

            current_info = self._info()
            if (self.last_info != current_info):
                self.lock.acquire()
                self._clear_output()
                print(current_info)
                self.lock.release()
                self.last_info = current_info
            else:
                time.sleep(0.5)
