from typing import Union

from .key import Key, KeyCode, KeyCombo

_transform = {
    "LC": "L_CTRL",
    "LCtrl": "L_CTRL",
    "RC": "R_CTRL",
    "RCtrl": "R_CTRL",
    "LM": "L_ALT",
    "LAlt": "L_ALT",
    "RM": "R_ALT",
    "RAlt": "R_ALT",
    "LShift": "L_SHIFT",
    "RShift": "R_SHIFT",
    "LSuper": "L_SUPER",
    "LWin": "L_SUPER",
    "RSuper": "R_SUPER",
    "RWin": "R_SUPER",
    # TODO: Transform . / = - ; ' []\`
}

# parses a single shortcut separated by -
# does not parse multiple key presses separated by spaces
def kbd_parse(input: str) -> Union[KeyCode, KeyCombo]:
    _keys = []
    for key in input.split("-"):
        key = _transform.get(key, key.upper())
        _keys.append(Key(key))
    
    if len(_keys) == 1:
        return _keys[0]

    sum = KeyCombo()
    for _key in _keys:
        sum = sum + _key
    return sum