from collections import defaultdict
import json

from typing import Dict, Iterable, Union

from keycodes import KeyCombo, KeyCode, WinKey

import constants as const


class not_list(list):
    pass


class PToysMapper:
    def __init__(self) -> None:
        self.key_map = defaultdict(dict)
        # key_map looks as follows, where currently everything is keyed under None = global shortcuts
        # {
        #     None: {
        #         K.A: KC(K.B, K.C),
        #         K.L_ALT: K.R_CTRL
        #     }
        # }

        self.shortcut_map = defaultdict(dict)
        # shortcut_map looks as follows, where None = global shortcuts
        # {
        #     None: {
        #         KC(K.A, K.B): KC(K.C, K.D)
        #     },
        #     "app_1": {
        #         KC(K.E, K.F): KC(K.G, K.H)
        #     }
        # }

        self.disabled_shortcuts = defaultdict(list)
        # disabled_shortcuts looks as follows. It is used to disable any shortcuts in
        # an app-specific setting to support not_list
        # {
        #     "app_1": [KC(K.A, K.B), KC(K.C, K.D)],
        #     "app_2": [KC(K.E, K.F), KC(K.G, K.H)],
        #     "app_3": [KC(K.E, K.F), KC(K.G, K.H)],
        # }

    def map_key(self, condition, mapping, name="anon"):
        for old, new in mapping.items():
            if not isinstance(condition, Iterable):
                condition = [condition]
            for c in condition:
                if c is None:
                    if c:
                        c = c.lower()
                    if old in self.key_map[c]:
                        # this means the same key remap has been defined more than once
                        pass
                    else:
                        # the mapping that was defined first takes priority. leaving the code like this because
                        # I'm undecided on what the behavior here should be
                        self.key_map[c][old] = new
                else:
                    raise TypeError(
                        "Unknown type in condition. Single key remaps currently only support None for condition."
                    )

    def map_shortcut(self, condition, mapping, name="anon"):
        for old, new in mapping.items():
            # if _not_list == True, we want to negate the condition so that rather than app-specific, we are adding
            # rules that are global but disabled for the provided app name
            _not_list: bool = False
            if isinstance(condition, not_list):
                _not_list = True

            if not isinstance(condition, Iterable):
                condition = [condition]
            for c in condition:
                if isinstance(c, str) or c is None:
                    if c:
                        # windows process names are case insensitive, and powertoys will force the JSON to lowercase anyways
                        c = c.lower()
                    if _not_list:
                        # in this block, the provided condition was a list of processes that are exceptions.
                        # need to add the rule to globals instead of app-specific and disable them later as app-specific shortcuts
                        globals = None
                        if old not in self.shortcut_map[globals]:
                            self.shortcut_map[globals][old] = new

                        self.disabled_shortcuts[c].append(old)
                    else:
                        if old in self.shortcut_map[c]:
                            # this means the same shortcut has been defined more than once
                            pass
                        else:
                            # the mapping that was defined first takes priority. leaving the code like this because
                            # I'm undecided on what the behavior here should be
                            self.shortcut_map[c][old] = new
                else:
                    raise TypeError("Unknown type in condition")

    # helper to return ptoys config struct
    @staticmethod
    def _remap_dict(old, new, app_name) -> Dict[str, str]:
        d = {
            const.ORIGINAL_KEYS_SETTING_NAME: PToysMapper._code_helper(old),
            const.NEW_REMAP_KEYS_SETTING_NAME: PToysMapper._code_helper(new),
        }
        if app_name:
            d[const.TARGET_APP_SETTING_NAME] = app_name
        return d

    @staticmethod
    def _code_helper(shortcut: Union[KeyCode, KeyCombo]) -> str:
        if isinstance(shortcut, KeyCode):
            shortcut = KeyCombo(shortcut)
        if isinstance(shortcut, KeyCombo):
            return ";".join([str(int(WinKey(key).code)) for key in shortcut])
        else:
            raise TypeError(
                "can't format unknown type with code helper: {}".format(type(shortcut))
            )

    def generate(self):
        # The app_name of "None" = global key remaps
        global_km: Dict[KeyCode, KeyCode] = (
            self.key_map.pop(None) if None in self.key_map else {}
        )
        global_km_json: Iterable[Dict[str, str]] = [
            self._remap_dict(old, new, None) for old, new in global_km.items()
        ]

        # The app_name of "None" = global shortcuts
        global_sc: Dict[KeyCombo, KeyCombo] = (
            self.shortcut_map.pop(None) if None in self.shortcut_map else {}
        )
        global_sc_json: Iterable[Dict[str, str]] = [
            self._remap_dict(old, new, None) for old, new in global_sc.items()
        ]

        
        # We process disabled_shortcuts at the very end to make sure we don't disable any shortcuts that have app-specific overrides
        for app_name, disabled_shortcuts in self.disabled_shortcuts.items():
            for disabled_sc in disabled_shortcuts:
                # if the disabled_sc is already inside of the shortcut map, that means the same shortcut already has an override, so don't disable the shortcut in that case
                # otherwise, we set the key to disabled
                if disabled_sc not in self.shortcut_map[app_name]:
                    self.shortcut_map[app_name][disabled_sc] = WinKey.DISABLED

        app_sc_json: Iterable[Dict[str, str]] = []
        for app_name, app_sc in self.shortcut_map.items():
            app_sc_json.extend(
                [self._remap_dict(old, new, app_name) for old, new in app_sc.items()]
            )

        ptoys_config = {
            const.REMAP_KEYS_SETTING_NAME: {
                const.IN_PROCESS_REMAP_KEYS_SETTING_NAME: global_km_json
            },
            const.REMAP_SHORTCUTS_SETTING_NAME: {
                const.GLOBAL_REMAP_SHORTCUTS_SETTING_NAME: global_sc_json,
                const.APP_SPECIFIC_REMAP_SHORTCUTS_SETTING_NAME: app_sc_json,
            },
        }
        with open("default.json", "w") as f:
            json.dump(ptoys_config, f, indent=2)
