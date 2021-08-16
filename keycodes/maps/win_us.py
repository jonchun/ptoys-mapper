
import kbd2code.keycodes as keycodes

replace_map = {
    # Modifiers (L and R prefixes were added)
    # https://www.emacswiki.org/emacs/EmacsKeyNotation
    "C": "CONTROL",
    "LC": "LCONTROL",
    "RC": "RCONTROL",
    "M": "MENU",
    "LM": "LMENU",
    "RM": "RMENU",
    "S": "SHIFT",
    "LS": "LSHIFT",
    "RS": "RSHIFT",
    "DEL": "BACK",
    "RET": "RETURN",
    "SPC": "SPACE",
    "ESC": "ESCAPE",
    "TAB": "TAB",
    # Function Keys
    # https://www.gnu.org/software/emacs/manual/html_node/emacs/Function-Keys.html
    # Cursor arrow keys.
    "left": "LEFT",
    "up": "UP",
    "right": "RIGHT",
    "down": "DOWN",
    # Other cursor repositioning keys
    "begin": "DISABLED",
    "end": "END",
    "home": "HOME",
    "next": "NEXT",
    "prior": "PRIOR",
    # Miscellaneous function keys.
    "select": "LAUNCH_MEDIA_SELECT",
    "print": "PRINT",
    "execute": "EXECUTE",
    "backtab": "DISABLED",
    "insert": "INSERT",
    "undo": "DISABLED",
    "redo": "DISABLED",
    "clearline": "DISABLED",
    "insertline": "DISABLED",
    "deleteline": "DISABLED",
    "insertchar": "DISABLED",
    "deletechar": "DISABLED",
    "clearline": "DISABLED",
    # Numbered function keys (across the top of the keyboard).
    "f25": "DISABLED",
    "f26": "DISABLED",
    "f27": "DISABLED",
    "f28": "DISABLED",
    "f29": "DISABLED",
    "f30": "DISABLED",
    "f31": "DISABLED",
    "f32": "DISABLED",
    "f33": "DISABLED",
    "f34": "DISABLED",
    "f35": "DISABLED",
    # Keypad keys (to the right of the regular keyboard), with names or punctuation.
    "kp-add": "ADD",
    "kp-subtract": "SUBTRACT",
    "kp-multiply": "MULTIPLY",
    "kp-divide": "DIVIDE",
    "kp-backtab": "DISABLED",
    "kp-space": "DISABLED",
    "kp-tab": "DISABLED",
    "kp-enter": "RETURN",
    "kp-separator": "SEPARATOR",
    "kp-decimal": "DECIMAL",
    "kp-equal": "OEM_PLUS",
    "kp-prior": "PRIOR",
    "kp-next": "NEXT",
    "kp-end": "END",
    "kp-home": "HOME",
    "kp-left": "LEFT",
    "kp-up": "UP",
    "kp-right": "RIGHT",
    "kp-down": "DOWN",
    "kp-insert": "INSERT",
    "kp-delete": "DELETE",
    # Keypad keys with digits.
    "kp-0": "NUMPAD0",
    "kp-1": "NUMPAD1",
    "kp-2": "NUMPAD2",
    "kp-3": "NUMPAD3",
    "kp-4": "NUMPAD4",
    "kp-5": "NUMPAD5",
    "kp-6": "NUMPAD6",
    "kp-7": "NUMPAD7",
    "kp-8": "NUMPAD8",
    "kp-9": "NUMPAD9",
    # Keypad PF keys.
    "kp-f1": "DISABLED",
    "kp-f2": "DISABLED",
    "kp-f3": "DISABLED",
    "kp-f4": "DISABLED",
}

def mapped_name(key_name: str) -> str:
    key_name = replace_map.get(key_name, key_name.upper())
    return "VK_{}".format(key_name)

def mapped_key(key_name: str) -> int:
    return getattr(keycodes.win, mapped_name(key_name), keycodes.win.VK_DISABLED)
