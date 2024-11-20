import pygsheets
from config import hotkeys


client = pygsheets.authorize(service_file='key-counter-3030a4d9855d.json')
ssht = client.open('Key Counter')
wsht = ssht.worksheet('title', 'Sheet1')


def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        return
    if key_char in hotkeys.keys():
        key_change(hotkeys[key_char][0], hotkeys[key_char][1])


def key_change(cell_string: str, decrease: bool):
    current_value = int(wsht.cell(cell_string).value)
    if current_value == 0 and decrease: return
    new_value = current_value - 1 if decrease else current_value + 1
    wsht.cell(cell_string).value = new_value
