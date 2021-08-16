from typing import Iterable, Union


class KeyCode:
    def __init__(self, key: str, code: int) -> None:
        self.key: str = key
        self.code: int = code

    def __hash__(self) -> int:
        return hash((self.key, self.code))

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __str__(self) -> str:
        return "<{}: {}>".format(self.key, self.code)

    def __repr__(self) -> str:
        return "<{class_name}: key={key}, code={code}>".format(
            class_name=self.__class__.__name__, key=repr(self.key), code=repr(self.code)
        )

    def __add__(self, other: Union["KeyCode", "KeyCombo"]):
        if isinstance(other, KeyCode):
            return KeyCombo(self, other)
        elif isinstance(other, KeyCombo):
            return KeyCombo(self) + other
        else:
            raise TypeError("Can only add togther KeyCode and KeyCombo")


class KeyCombo:
    def __init__(self, *args) -> None:
        # using a list instead of a set to preserve order
        _self_combo = []

        # Flatten args non-recursively just to make KeyCombo(x,y,z) nicer to use.
        for arg in args:
            if isinstance(arg, Iterable):
                for key_code in arg:
                    if isinstance(key_code, KeyCode):
                        if key_code not in _self_combo:
                            _self_combo.append(key_code)
                    else:
                        raise KeyComboTypeError()
            else:
                key_code = arg
                if isinstance(key_code, KeyCode):
                    if key_code not in _self_combo:
                        _self_combo.append(key_code)
                else:
                    raise KeyComboTypeError()
        self._combo = tuple(_self_combo)

    def __hash__(self) -> int:
        return hash(self._combo)

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    def __str__(self) -> str:
        output = "{"
        for key in self._combo:
            output = "{}{}, ".format(output, str(key))
        output = output.rstrip(", ")
        output += "}"
        return output

    def __repr__(self) -> str:
        return repr(self._combo)
        # output = "{KeyCombo: "
        # for key in self._combo:
        #     output = "{}{}, ".format(output, repr(key))
        # output = output.rstrip(", ")
        # output += "}"
        # return output

    def __add__(self, other: Union[KeyCode, "KeyCombo"]):
        if isinstance(other, KeyCode):
            return self + KeyCombo(other)
        elif isinstance(other, KeyCombo):
            # use list instead of set to preserve order
            _self_combo = list(self._combo)
            for _key in other._combo:
                if _key not in _self_combo:
                    _self_combo.append(_key)
            return KeyCombo(_self_combo)
        else:
            raise TypeError("Can only add together KeyCode and KeyCombo")

    def __iter__(self):
        return iter(self._combo)

    def __next__(self):
        pass


class KeyComboTypeError(TypeError):
    def __init__(self, *args: object) -> None:
        if not args:
            msg = "KeyCombo can only consist of KeyCodes"
        else:
            msg = args[0]
            args = args[:-1]
        super().__init__(msg, *args)
