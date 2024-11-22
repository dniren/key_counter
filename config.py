from pynput import keyboard
import main

hotkeys = {
    # DECREASE LOSING KEYS
    'q': ['b2', True],
    # INCREASE LOSING KEYS
    'w': ['b2', False],
    # DECREASE WINNING KEYS
    'e': ['a2', True],
    # INCREASE WINNING KEYS
    'r': ['a2', False]
}

if __name__ == '__main__':
    print('starting...')
    with keyboard.Listener(on_press=main.on_press) as listener:
        listener.join()
