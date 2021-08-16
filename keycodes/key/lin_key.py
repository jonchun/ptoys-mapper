from .key import _Key
from . import codes


class _LinKey(_Key):
    _codes = codes.linux

    @classmethod
    def translate(cls, key_name: str) -> str:
        key_name = _lin_key_map.get(key_name, key_name)
        return "VK_{}".format(key_name)


_lin_key_map = {
    "ESCAPE": "ESC",
    "BACKTICK": "GRAVE",
    "ONE": "1",
    "TWO": "2",
    "THREE": "3",
    "FOUR": "4",
    "FIVE": "5",
    "SIX": "6",
    "SEVEN": "7",
    "EIGHT": "8",
    "NINE": "9",
    "ZERO": "0",
    "HYPHEN": "MINUS",
    "BACKSLASH": "",
    "L_BRACE": "LEFTBRACE",
    "R_BRACE": "RIGHTBRACE",
    "CAPS_LOCK": "CAPSLOCK",
    "QUOTE": "APOSTROPHE",
    "L_SHIFT": "LEFTSHIFT",
    "PERIOD": "DOT",
    "R_SHIFT": "RIGHTSHIFT",
    "L_CTRL": "LEFTCTRL",
    "L_SUPER": "LEFTMETA",
    "L_ALT": "LEFTALT",
    "R_ALT": "RIGHTALT",
    "R_SUPER": "RIGHTMETA",
    "R_CTRL": "RIGHTCTRL",
    "PRINT_SCREEN": "",
    "SCROLL_LOCK": "",
    "PAUSE": "",
    "INSERT": "",
    "HOME": "",
    "PAGE_UP": "",
    "DELETE": "",
    "END": "",
    "PAGE_DOWN": "",
    "UP": "",
    "LEFT": "",
    "DOWN": "",
    "RIGHT": "",
    "NUM_LOCK": "",
    "NUM_DIVIDE": "",
    "NUM_MULTIPLY": "",
    "NUM_MINUS": "",
    "NUM_PLUS": "",
    "NUM_ENTER": "",
    "NUM_ONE": "",
    "NUM_TWO": "",
    "NUM_THREE": "",
    "NUM_FOUR": "",
    "NUM_FIVE": "",
    "NUM_SIX": "",
    "NUM_SEVEN": "",
    "NUM_EIGHT": "",
    "NUM_NINE": "",
    "NUM_ZERO": "",
    "NUM_DECIMAL": "",
}
