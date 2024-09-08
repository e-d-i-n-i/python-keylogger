from pynput.mouse import Listener

def writeToConsole(x, y):
    print('Position of current mouse: {}'.format((x, y)))

with Listener(on_move=writeToConsole) as l:
    l.join()
