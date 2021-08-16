from typing import Union

from .keycodes import KeyCode


class _Key:
    _codes = None

    def __init__(self):
        pass

    # fallback if key code is not found.
    def _default_code(self, key_name: str) -> None:
        return None

    def get_code(self, key_name: str) -> KeyCode:
        code = None
        if self._codes:
            try:
                code = self._codes[self.translate(key_name)]
            except KeyError:
                code = self._default_code(key_name)

        return KeyCode(key_name, code)

    def translate(self, key_name: str) -> str:
        return key_name

    # when Key(KeyCode) is called, it should convert it into a KeyCode from itself
    #
    # This allows "casting" between different keys as follows:
    # key = Key.SEMICOLON
    # win_key = WinKey(key)
    # print(repr(key))
    # print(repr(win_key))
    # print(repr(Key(key)))
    #
    # Output:
    # <KeyCode: key='SEMICOLON', code=None>
    # <KeyCode: key='SEMICOLON', code=<WinCodes.VK_OEM_1: 186>>
    # <KeyCode: key='SEMICOLON', code=None>

    def __call__(self, key_code: Union[KeyCode, str]) -> KeyCode:
        if isinstance(key_code, KeyCode):
            key_name = key_code.key
        elif isinstance(key_code, str):
            key_name = key_code
        else:
            raise TypeError("Can only create a KeyCode from another KeyCode or string")
        return getattr(self, key_name)

    # ===== START SPECIAL =====
    # These keys don't actually exist
    @property
    def _DISABLED(self) -> KeyCode:
        return self.get_code("DISABLED")

    DISABLED = _DISABLED

    @property
    def _SUPER(self) -> KeyCode:
        return self.get_code("SUPER")

    SUPER = _SUPER
    WIN = _SUPER
    META = _SUPER

    @property
    def _CTRL(self) -> KeyCode:
        return self.get_code("CTRL")

    CTRL = _CTRL

    @property
    def _SHIFT(self) -> KeyCode:
        return self.get_code("SHIFT")

    SHIFT = _SHIFT

    @property
    def _ALT(self) -> KeyCode:
        return self.get_code("ALT")

    ALT = _ALT

    # ===== END SPECIAL =====

    @property
    def _ESCAPE(self) -> KeyCode:
        return self.get_code("ESCAPE")

    ESCAPE = _ESCAPE
    ESC = _ESCAPE

    @property
    def _F1(self) -> KeyCode:
        return self.get_code("F1")

    F1 = _F1

    @property
    def _F2(self) -> KeyCode:
        return self.get_code("F2")

    F2 = _F2

    @property
    def _F3(self) -> KeyCode:
        return self.get_code("F3")

    F3 = _F3

    @property
    def _F4(self) -> KeyCode:
        return self.get_code("F4")

    F4 = _F4

    @property
    def _F5(self) -> KeyCode:
        return self.get_code("F5")

    F5 = _F5

    @property
    def _F6(self) -> KeyCode:
        return self.get_code("F6")

    F6 = _F6

    @property
    def _F7(self) -> KeyCode:
        return self.get_code("F7")

    F7 = _F7

    @property
    def _F8(self) -> KeyCode:
        return self.get_code("F8")

    F8 = _F8

    @property
    def _F9(self) -> KeyCode:
        return self.get_code("F9")

    F9 = _F9

    @property
    def _F10(self) -> KeyCode:
        return self.get_code("F10")

    F10 = _F10

    @property
    def _F11(self) -> KeyCode:
        return self.get_code("F11")

    F11 = _F11

    @property
    def _F12(self) -> KeyCode:
        return self.get_code("F12")

    F12 = _F12

    @property
    def _F13(self) -> KeyCode:
        return self.get_code("F13")

    F13 = _F13

    @property
    def _F14(self) -> KeyCode:
        return self.get_code("F14")

    F14 = _F14

    @property
    def _F15(self) -> KeyCode:
        return self.get_code("F15")

    F15 = _F15

    @property
    def _F16(self) -> KeyCode:
        return self.get_code("F16")

    F16 = _F16

    @property
    def _F17(self) -> KeyCode:
        return self.get_code("F17")

    F17 = _F17

    @property
    def _F18(self) -> KeyCode:
        return self.get_code("F18")

    F18 = _F18

    @property
    def _F19(self) -> KeyCode:
        return self.get_code("F19")

    F19 = _F19

    @property
    def _F20(self) -> KeyCode:
        return self.get_code("F20")

    F20 = _F20

    @property
    def _F21(self) -> KeyCode:
        return self.get_code("F21")

    F21 = _F21

    @property
    def _F22(self) -> KeyCode:
        return self.get_code("F22")

    F22 = _F22

    @property
    def _F23(self) -> KeyCode:
        return self.get_code("F23")

    F23 = _F23

    @property
    def _F24(self) -> KeyCode:
        return self.get_code("F24")

    F24 = _F24

    @property
    def _BACKTICK(self) -> KeyCode:
        return self.get_code("BACKTICK")

    BACKTICK = _BACKTICK
    TILDE = _BACKTICK
    GRAVE = _BACKTICK

    @property
    def _ONE(self) -> KeyCode:
        return self.get_code("ONE")

    ONE = _ONE
    KEY_1 = _ONE

    @property
    def _TWO(self) -> KeyCode:
        return self.get_code("TWO")

    TWO = _TWO
    KEY_2 = _TWO

    @property
    def _THREE(self) -> KeyCode:
        return self.get_code("THREE")

    THREE = _THREE
    KEY_3 = _THREE

    @property
    def _FOUR(self) -> KeyCode:
        return self.get_code("FOUR")

    FOUR = _FOUR
    KEY_4 = _FOUR

    @property
    def _FIVE(self) -> KeyCode:
        return self.get_code("FIVE")

    FIVE = _FIVE
    KEY_5 = _FIVE

    @property
    def _SIX(self) -> KeyCode:
        return self.get_code("SIX")

    SIX = _SIX
    KEY_6 = _SIX

    @property
    def _SEVEN(self) -> KeyCode:
        return self.get_code("SEVEN")

    SEVEN = _SEVEN
    KEY_7 = _SEVEN

    @property
    def _EIGHT(self) -> KeyCode:
        return self.get_code("EIGHT")

    EIGHT = _EIGHT
    KEY_8 = _EIGHT

    @property
    def _NINE(self) -> KeyCode:
        return self.get_code("NINE")

    NINE = _NINE
    KEY_9 = _NINE

    @property
    def _ZERO(self) -> KeyCode:
        return self.get_code("ZERO")

    ZERO = _ZERO
    KEY_0 = _ZERO

    @property
    def _HYPHEN(self) -> KeyCode:
        return self.get_code("HYPHEN")

    HYPHEN = _HYPHEN
    MINUS = _HYPHEN

    @property
    def _EQUAL(self) -> KeyCode:
        return self.get_code("EQUAL")

    EQUAL = _EQUAL

    @property
    def _BACKSLASH(self) -> KeyCode:
        return self.get_code("BACKSLASH")

    BACKSLASH = _BACKSLASH

    @property
    def _BACKSPACE(self) -> KeyCode:
        return self.get_code("BACKSPACE")

    BACKSPACE = _BACKSPACE

    @property
    def _TAB(self) -> KeyCode:
        return self.get_code("TAB")

    TAB = _TAB

    @property
    def _Q(self) -> KeyCode:
        return self.get_code("Q")

    Q = _Q

    @property
    def _W(self) -> KeyCode:
        return self.get_code("W")

    W = _W

    @property
    def _E(self) -> KeyCode:
        return self.get_code("E")

    E = _E

    @property
    def _R(self) -> KeyCode:
        return self.get_code("R")

    R = _R

    @property
    def _T(self) -> KeyCode:
        return self.get_code("T")

    T = _T

    @property
    def _Y(self) -> KeyCode:
        return self.get_code("Y")

    Y = _Y

    @property
    def _U(self) -> KeyCode:
        return self.get_code("U")

    U = _U

    @property
    def _I(self) -> KeyCode:
        return self.get_code("I")

    I = _I

    @property
    def _O(self) -> KeyCode:
        return self.get_code("O")

    O = _O

    @property
    def _P(self) -> KeyCode:
        return self.get_code("P")

    P = _P

    @property
    def _L_BRACE(self) -> KeyCode:
        return self.get_code("L_BRACE")

    L_BRACE = _L_BRACE
    LEFT_BRACE = _L_BRACE

    @property
    def _R_BRACE(self) -> KeyCode:
        return self.get_code("R_BRACE")

    R_BRACE = _R_BRACE
    RIGHT_BRACE = _R_BRACE

    @property
    def _CAPS_LOCK(self) -> KeyCode:
        return self.get_code("CAPS_LOCK")

    CAPS_LOCK = _CAPS_LOCK

    @property
    def _A(self) -> KeyCode:
        return self.get_code("A")

    A = _A

    @property
    def _S(self) -> KeyCode:
        return self.get_code("S")

    S = _S

    @property
    def _D(self) -> KeyCode:
        return self.get_code("D")

    D = _D

    @property
    def _F(self) -> KeyCode:
        return self.get_code("F")

    F = _F

    @property
    def _G(self) -> KeyCode:
        return self.get_code("G")

    G = _G

    @property
    def _H(self) -> KeyCode:
        return self.get_code("H")

    H = _H

    @property
    def _J(self) -> KeyCode:
        return self.get_code("J")

    J = _J

    @property
    def _K(self) -> KeyCode:
        return self.get_code("K")

    K = _K

    @property
    def _L(self) -> KeyCode:
        return self.get_code("L")

    L = _L

    @property
    def _SEMICOLON(self) -> KeyCode:
        return self.get_code("SEMICOLON")

    SEMICOLON = _SEMICOLON

    @property
    def _QUOTE(self) -> KeyCode:
        return self.get_code("QUOTE")

    QUOTE = _QUOTE
    APOSTROPHE = _QUOTE

    @property
    def _ENTER(self) -> KeyCode:
        return self.get_code("ENTER")

    ENTER = _ENTER

    @property
    def _L_SHIFT(self) -> KeyCode:
        return self.get_code("L_SHIFT")

    L_SHIFT = _L_SHIFT
    LEFT_SHIFT = _L_SHIFT

    @property
    def _Z(self) -> KeyCode:
        return self.get_code("Z")

    Z = _Z

    @property
    def _X(self) -> KeyCode:
        return self.get_code("X")

    X = _X

    @property
    def _C(self) -> KeyCode:
        return self.get_code("C")

    C = _C

    @property
    def _V(self) -> KeyCode:
        return self.get_code("V")

    V = _V

    @property
    def _B(self) -> KeyCode:
        return self.get_code("B")

    B = _B

    @property
    def _N(self) -> KeyCode:
        return self.get_code("N")

    N = _N

    @property
    def _M(self) -> KeyCode:
        return self.get_code("M")

    M = _M

    @property
    def _COMMA(self) -> KeyCode:
        return self.get_code("COMMA")

    COMMA = _COMMA

    @property
    def _PERIOD(self) -> KeyCode:
        return self.get_code("PERIOD")

    PERIOD = _PERIOD

    @property
    def _SLASH(self) -> KeyCode:
        return self.get_code("SLASH")

    SLASH = _SLASH

    @property
    def _R_SHIFT(self) -> KeyCode:
        return self.get_code("R_SHIFT")

    R_SHIFT = _R_SHIFT
    RIGHT_SHIFT = _R_SHIFT

    @property
    def _L_CTRL(self) -> KeyCode:
        return self.get_code("L_CTRL")

    L_CTRL = _L_CTRL
    LEFT_CTRL = _L_CTRL

    @property
    def _L_SUPER(self) -> KeyCode:
        return self.get_code("L_SUPER")

    L_SUPER = _L_SUPER
    LEFT_SUPER = _L_SUPER
    L_WIN = _L_SUPER
    LEFT_WIN = _L_SUPER
    L_META = _L_SUPER
    LEFT_META = _L_SUPER

    @property
    def _L_ALT(self) -> KeyCode:
        return self.get_code("L_ALT")

    L_ALT = _L_ALT
    LEFT_ALT = _L_ALT

    @property
    def _SPACE(self) -> KeyCode:
        return self.get_code("SPACE")

    SPACE = _SPACE

    @property
    def _R_ALT(self) -> KeyCode:
        return self.get_code("R_ALT")

    R_ALT = _R_ALT
    RIGHT_ALT = _R_ALT

    @property
    def _R_SUPER(self) -> KeyCode:
        return self.get_code("R_SUPER")

    R_SUPER = _R_SUPER
    RIGHT_SUPER = _R_SUPER
    R_WIN = _R_SUPER
    RIGHT_WIN = _R_SUPER
    R_META = _R_SUPER
    RIGHT_META = _R_SUPER

    @property
    def _R_CTRL(self) -> KeyCode:
        return self.get_code("R_CTRL")

    R_CTRL = _R_CTRL
    RIGHT_CTRL = _R_CTRL

    @property
    def _PRINT_SCREEN(self) -> KeyCode:
        return self.get_code("PRINT_SCREEN")

    PRINT_SCREEN = _PRINT_SCREEN

    @property
    def _SCROLL_LOCK(self) -> KeyCode:
        return self.get_code("SCROLL_LOCK")

    SCROLL_LOCK = _SCROLL_LOCK

    @property
    def _PAUSE(self) -> KeyCode:
        return self.get_code("PAUSE")

    PAUSE = _PAUSE

    @property
    def _INSERT(self) -> KeyCode:
        return self.get_code("INSERT")

    INSERT = _INSERT

    @property
    def _HOME(self) -> KeyCode:
        return self.get_code("HOME")

    HOME = _HOME

    @property
    def _PAGE_UP(self) -> KeyCode:
        return self.get_code("PAGE_UP")

    PAGE_UP = _PAGE_UP

    @property
    def _DELETE(self) -> KeyCode:
        return self.get_code("DELETE")

    DELETE = _DELETE

    @property
    def _END(self) -> KeyCode:
        return self.get_code("END")

    END = _END

    @property
    def _PAGE_DOWN(self) -> KeyCode:
        return self.get_code("PAGE_DOWN")

    PAGE_DOWN = _PAGE_DOWN

    @property
    def _UP(self) -> KeyCode:
        return self.get_code("UP")

    UP = _UP

    @property
    def _LEFT(self) -> KeyCode:
        return self.get_code("LEFT")

    LEFT = _LEFT

    @property
    def _DOWN(self) -> KeyCode:
        return self.get_code("DOWN")

    DOWN = _DOWN

    @property
    def _RIGHT(self) -> KeyCode:
        return self.get_code("RIGHT")

    RIGHT = _RIGHT

    @property
    def _NUM_LOCK(self) -> KeyCode:
        return self.get_code("NUM_LOCK")

    NUM_LOCK = _NUM_LOCK

    @property
    def _NUM_DIVIDE(self) -> KeyCode:
        return self.get_code("NUM_DIVIDE")

    NUM_DIVIDE = _NUM_DIVIDE

    @property
    def _NUM_MULTIPLY(self) -> KeyCode:
        return self.get_code("NUM_MULTIPLY")

    NUM_MULTIPLY = _NUM_MULTIPLY

    @property
    def _NUM_MINUS(self) -> KeyCode:
        return self.get_code("NUM_MINUS")

    NUM_MINUS = _NUM_MINUS

    @property
    def _NUM_PLUS(self) -> KeyCode:
        return self.get_code("NUM_PLUS")

    NUM_PLUS = _NUM_PLUS

    @property
    def _NUM_ENTER(self) -> KeyCode:
        return self.get_code("NUM_ENTER")

    NUM_ENTER = _NUM_ENTER

    @property
    def _NUM_ONE(self) -> KeyCode:
        return self.get_code("NUM_ONE")

    NUM_ONE = _NUM_ONE
    NUM_1 = _NUM_ONE

    @property
    def _NUM_TWO(self) -> KeyCode:
        return self.get_code("NUM_TWO")

    NUM_TWO = _NUM_TWO
    NUM_2 = _NUM_TWO

    @property
    def _NUM_THREE(self) -> KeyCode:
        return self.get_code("NUM_THREE")

    NUM_THREE = _NUM_THREE
    NUM_3 = _NUM_THREE

    @property
    def _NUM_FOUR(self) -> KeyCode:
        return self.get_code("NUM_FOUR")

    NUM_FOUR = _NUM_FOUR
    NUM_4 = _NUM_FOUR

    @property
    def _NUM_FIVE(self) -> KeyCode:
        return self.get_code("NUM_FIVE")

    NUM_FIVE = _NUM_FIVE
    NUM_5 = _NUM_FIVE

    @property
    def _NUM_SIX(self) -> KeyCode:
        return self.get_code("NUM_SIX")

    NUM_SIX = _NUM_SIX
    NUM_6 = _NUM_SIX

    @property
    def _NUM_SEVEN(self) -> KeyCode:
        return self.get_code("NUM_SEVEN")

    NUM_SEVEN = _NUM_SEVEN
    NUM_7 = _NUM_SEVEN

    @property
    def _NUM_EIGHT(self) -> KeyCode:
        return self.get_code("NUM_EIGHT")

    NUM_EIGHT = _NUM_EIGHT
    NUM_8 = _NUM_EIGHT

    @property
    def _NUM_NINE(self) -> KeyCode:
        return self.get_code("NUM_NINE")

    NUM_NINE = _NUM_NINE
    NUM_9 = _NUM_NINE

    @property
    def _NUM_ZERO(self) -> KeyCode:
        return self.get_code("NUM_ZERO")

    NUM_ZERO = _NUM_ZERO
    NUM_0 = _NUM_ZERO

    @property
    def _NUM_DECIMAL(self) -> KeyCode:
        return self.get_code("NUM_DECIMAL")

    NUM_DECIMAL = _NUM_DECIMAL


# The below can be used as a starting point when defining a map of translations.
#
# "DISABLED": "",
# "SUPER": "",
# "CTRL": "",
# "SHIFT": "",
# "ALT": "",

# "ESCAPE": "",
# "F1": "",
# "F2": "",
# "F3": "",
# "F4": "",
# "F5": "",
# "F6": "",
# "F7": "",
# "F8": "",
# "F9": "",
# "F10": "",
# "F11": "",
# "F12": "",
# "F13": "",
# "F14": "",
# "F15": "",
# "F16": "",
# "F17": "",
# "F18": "",
# "F19": "",
# "F20": "",
# "F21": "",
# "F22": "",
# "F23": "",
# "F24": "",
# "BACKTICK": "",
# "ONE": "",
# "TWO": "",
# "THREE": "",
# "FOUR": "",
# "FIVE": "",
# "SIX": "",
# "SEVEN": "",
# "EIGHT": "",
# "NINE": "",
# "ZERO": "",
# "HYPHEN": "",
# "EQUAL": "",
# "BACKSLASH": "",
# "BACKSPACE": "",
# "TAB": "",
# "Q": "",
# "W": "",
# "E": "",
# "R": "",
# "T": "",
# "Y": "",
# "U": "",
# "I": "",
# "O": "",
# "P": "",
# "L_BRACE": "",
# "R_BRACE": "",
# "CAPS_LOCK": "",
# "A": "",
# "S": "",
# "D": "",
# "F": "",
# "G": "",
# "H": "",
# "J": "",
# "K": "",
# "L": "",
# "SEMICOLON": "",
# "QUOTE": "",
# "ENTER": "",
# "L_SHIFT": "",
# "Z": "",
# "X": "",
# "C": "",
# "V": "",
# "B": "",
# "N": "",
# "M": "",
# "COMMA": "",
# "PERIOD": "",
# "SLASH": "",
# "R_SHIFT": "",
# "L_CTRL": "",
# "L_SUPER": "",
# "L_ALT": "",
# "SPACE": "",
# "R_ALT": "",
# "R_SUPER": "",
# "R_CTRL": "",

# "PRINT_SCREEN": "",
# "SCROLL_LOCK": "",
# "PAUSE": "",

# "INSERT": "",
# "HOME": "",
# "PAGE_UP": "",
# "DELETE": "",
# "END": "",
# "PAGE_DOWN": "",

# "UP": "",
# "LEFT": "",
# "DOWN": "",
# "RIGHT": "",

# "NUM_LOCK": "",
# "NUM_DIVIDE": "",
# "NUM_MULTIPLY": "",
# "NUM_MINUS": "",
# "NUM_PLUS": "",
# "NUM_ENTER": "",
# "NUM_ONE": "",
# "NUM_TWO": "",
# "NUM_THREE": "",
# "NUM_FOUR": "",
# "NUM_FIVE": "",
# "NUM_SIX": "",
# "NUM_SEVEN": "",
# "NUM_EIGHT": "",
# "NUM_NINE": "",
# "NUM_ZERO": "",
# "NUM_DECIMAL": "",
