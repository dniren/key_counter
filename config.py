from pynput import keyboard
import main

hotkeys = {
    # DECREASE BAD KEYS
    'q': ['b2', True],
    # INCREASE BAD KEYS
    'w': ['b2', False],
    # DECREASE GOOD KEYS
    'e': ['a2', True],
    # INCREASE GOOD KEYS
    'r': ['a2', False]
}

if __name__ == '__main__':
    print('starting...')
    with keyboard.Listener(on_press=main.on_press) as listener:
        listener.join()