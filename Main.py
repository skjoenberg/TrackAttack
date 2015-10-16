import json
import threading
from Log import Log
from Game import Game
from UI import UI

# Global random stuff
log_path = '/home/sebastian/.PlayOnLinux/wineprefix/hearthstone/drive_c/Program Files/Hearthstone/Hearthstone_Data/output_log.txt'

last_info = ""
exit = False

# Creates a pretty output string
def info(game):
    if game.coin_used:
        pretty_coin = "Coin played." + "\n" * 2
    else :
        pretty_coin = "Coin not played." + "\n" * 2

    pretty_played_self = "played self:\n" + pretty_list(game.played_self[-7:]) + "\n"
    pretty_played_oppo = "played op:\n" + pretty_list(game.played_oppo[-7:]) + "\n"
    return pretty_coin + pretty_played_self + pretty_played_oppo

# Used for printing cards
def pretty_list(a):
    result = ""
    for elem in a:
        result += elem + "\n"
    return result

cur_ui = UI(log_path)

# Starting a thread for output
output_thread = threading.Thread(target=cur_ui.output_thread)
output_thread.start()

# Get inputs in current thread
cur_ui.input_thread()
