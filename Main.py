import json
import threading
from Log import Log
from Game import Game
from UI import UI

# Global random stuff
log_path = '/home/sebastian/.PlayOnLinux/wineprefix/hearthstone/drive_c/Program Files/Hearthstone/Hearthstone_Data/output_log.txt'

last_info = ""
exit = False

# Create UI-object
cur_ui = UI(log_path)

# Starting a thread for output
output_thread = threading.Thread(target=cur_ui.output_thread)
output_thread.start()

# Get inputs in current thread
cur_ui.input_thread()
