from .key import _Key
from . import codes


class _WinKey(_Key):
    _codes = codes.win

    def _default_code(self, key_name: str) -> None:
        return codes.win.VK_DISABLED

    @classmethod
    def translate(cls, key_name: str) -> str:
        key_name = _win_key_map.get(key_name, key_name.upper())
        return "VK_{}".format(key_name)


_win_key_map = {
    "SUPER": "WIN",
    "CTRL": "CONTROL",
    "SHIFT": "SHIFT",
    "ALT": "MENU",

    "BACKTICK": "OEM_3",
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
    "HYPHEN": "OEM_MINUS",
    "EQUAL": "OEM_PLUS",
    "BACKSLASH": "OEM_5",
    "BACKSPACE": "BACK",
    "L_BRACE": "OEM_4",
    "R_BRACE": "OEM_6",
    "CAPS_LOCK": "CAPITAL",
    "SEMICOLON": "OEM_1",
    "QUOTE": "OEM_7",
    "ENTER": "RETURN",
    "L_SHIFT": "LSHIFT",
    "COMMA": "OEM_COMMA",
    "PERIOD": "OEM_PERIOD",
    "SLASH": "OEM_2",
    "R_SHIFT": "RSHIFT",
    "L_CTRL": "LCONTROL",
    "L_SUPER": "LWIN",
    "L_ALT": "LMENU",
    "R_ALT": "RMENU",
    "R_SUPER": "RWIN",
    "R_CTRL": "RCONTROL",
    "PRINT_SCREEN": "SNAPSHOT",
    "SCROLL_LOCK": "SCROLL",
    "PAGE_UP": "PRIOR",
    "PAGE_DOWN": "NEXT",
    "NUM_LOCK": "NUMLOCK",
    "NUM_DIVIDE": "DIVIDE",
    "NUM_MINUS": "SUBTRACT",
    "NUM_PLUS": "ADD",
    "NUM_ENTER": "RETURN",
    "NUM_ONE": "NUMPAD1",
    "NUM_TWO": "NUMPAD2",
    "NUM_THREE": "NUMPAD3",
    "NUM_FOUR": "NUMPAD4",
    "NUM_FIVE": "NUMPAD5",
    "NUM_SIX": "NUMPAD6",
    "NUM_SEVEN": "NUMPAD7",
    "NUM_EIGHT": "NUMPAD8",
    "NUM_NINE": "NUMPAD9",
    "NUM_ZERO": "NUMPAD0",
    "NUM_DECIMAL": "DECIMAL",
}
