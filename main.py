from keycodes import Key as K
from keycodes import KeyCombo as KC

from mapper import PToysMapper

if __name__ == "__main__":
    K_CMD = K.R_CTRL
    K_OPTION = K.L_ALT

    pm = PToysMapper()

    pm.map_key(
        None,
        {
            # L_ALT gets mapped to K_CMD (R_CTRL) to allow for differentiating K_CMD bindings from CTRL bindings.
            K.L_ALT: K_CMD,
            # The L_SUPER key becomes the K_OPTION (L_ALT) key
            K.L_SUPER: K_OPTION,
            # Intentionally leave L_CTRL untouched. It should just act as L_CTRL just like on a mac
        },
        "globals.alt_to_cmd",
    )

    ## 2 #'s means shortcut is unchanged in Mac/Win
    ### 3 #'s means shortcut is not simple and needs to disabled or done via AHK

    # Cut, copy, paste, and other common shortcuts
    # https://support.apple.com/en-us/HT201236
    pm.map_shortcut(
        None,
        {
            ## Command-X: Cut the selected item and copy it to the Clipboard.
            ## Command-C: Copy the selected item to the Clipboard. This also works for files in the Finder.
            ## Command-V: Paste the contents of the Clipboard into the current document or app. This also works for files in the Finder.
            ## Command-Z: Undo the previous command. You can then press Shift-Command-Z to Redo, reversing the undo command. In some apps, you can undo and redo multiple commands.
            ## Command-A: Select All items.
            ## Command-F: Find items in a document or open a Find window.
            ## Command-G: Find Again: Find the next occurrence of the item previously found. To find the previous occurrence, press Shift-Command-G.
            # Option-Command-Esc: Force quit an app.
            KC(K_CMD, K_OPTION, K.ESC): KC(K.R_CTRL, K.L_SHIFT, K.ESC),
            # Command-Tab: Switch to the next most recently used app among your open apps.
            KC(K_CMD, K.TAB): KC(K.L_ALT, K.TAB),
            KC(K_CMD, K.SHIFT, K.TAB): KC(K.L_ALT, K.L_SHIFT, K.TAB),
            # To take a screenshot, press and hold these three keys together: Shift, Command, and 3.
            KC(K_CMD, K.SHIFT, K.KEY_3): K.PRINT_SCREEN,
            # How to capture a portion of the screen. Press and hold these three keys together: Shift, Command, and 4.
            KC(K_CMD, K.SHIFT, K.KEY_4): KC(K.R_WIN, K.L_SHIFT, K.S),
        },
        "globals.common",
    )

    # Undocumented Globals
    pm.map_shortcut(
        None,
        {
            # https://discussions.apple.com/thread/671085
            # Command-Period is the usual keyboard shortcut for Cancel in most Mac dialog boxes.
            KC(K_CMD, K.PERIOD): KC(K.ESC),
            # Can't find any official documentation for Command-Q, but it should exit current app
            KC(K_CMD, K.Q): KC(K.ALT, K.F4),
        },
        "globals.undocumented",
    )

    # Document shortcuts
    # The behavior of these shortcuts may vary with the app you're using.
    pm.map_shortcut(
        None,
        {
            # Control-H: Delete the character to the left of the insertion point. Or use Delete.
            KC(K.L_CTRL, K.H): KC(K.BACKSPACE),
            # Control-D: Delete the character to the right of the insertion point. Or use Fn-Delete.
            KC(K.L_CTRL, K.D): KC(K.DELETE),
            ### Control-K: Delete the text between the insertion point and the end of the line or paragraph.
            # Command–Up Arrow: Move the insertion point to the beginning of the document.
            KC(K_CMD, K.UP): KC(K.R_CTRL, K.HOME),
            # Command–Down Arrow: Move the insertion point to the end of the document.
            KC(K_CMD, K.DOWN): KC(K.R_CTRL, K.END),
            # Command–Left Arrow: Move the insertion point to the beginning of the current line.
            KC(K_CMD, K.LEFT): KC(K.HOME),
            # Command–Right Arrow: Move the insertion point to the end of the current line.
            KC(K_CMD, K.RIGHT): KC(K.END),
            # Option–Left Arrow: Move the insertion point to the beginning of the previous word.
            KC(K_OPTION, K.LEFT): KC(K.R_CTRL, K.LEFT),
            # Option–Right Arrow: Move the insertion point to the end of the next word.
            KC(K_OPTION, K.RIGHT): KC(K.R_CTRL, K.RIGHT),
            # Shift–Command–Up Arrow: Select the text between the insertion point and the beginning of the document.
            KC(K_CMD, K.SHIFT, K.UP): KC(K.R_CTRL, K.L_SHIFT, K.HOME),
            # Shift–Command–Down Arrow: Select the text between the insertion point and the end of the document.
            KC(K_CMD, K.SHIFT, K.DOWN): KC(K.R_CTRL, K.L_SHIFT, K.END),
            # Shift–Command–Left Arrow: Select the text between the insertion point and the beginning of the current line.
            KC(K_CMD, K.SHIFT, K.LEFT): KC(K.R_CTRL, K.L_SHIFT, K.LEFT),
            # Shift–Command–Right Arrow: Select the text between the insertion point and the end of the current line.
            KC(K_CMD, K.SHIFT, K.RIGHT): KC(K.R_CTRL, K.L_SHIFT, K.RIGHT),
            ## Shift–Up Arrow: Extend text selection to the nearest character at the same horizontal location on the line above.
            ## Shift–Down Arrow: Extend text selection to the nearest character at the same horizontal location on the line below.
            ## Shift–Left Arrow: Extend text selection one character to the left.
            ## Shift–Right Arrow: Extend text selection one character to the right.
            # Option–Shift–Up Arrow: Extend text selection to the beginning of the current paragraph, then to the beginning of the following paragraph if pressed again.
            KC(K_OPTION, K.SHIFT, K.UP): KC(K.R_CTRL, K.L_SHIFT, K.UP),
            # Option–Shift–Down Arrow: Extend text selection to the end of the current paragraph, then to the end of the following paragraph if pressed again.
            KC(K_OPTION, K.SHIFT, K.DOWN): KC(K.R_CTRL, K.L_SHIFT, K.DOWN),
            # Option–Shift–Left Arrow: Extend text selection to the beginning of the current word, then to the beginning of the following word if pressed again.
            KC(K_OPTION, K.SHIFT, K.LEFT): KC(K.R_CTRL, K.L_SHIFT, K.LEFT),
            # Option–Shift–Right Arrow: Extend text selection to the end of the current word, then to the end of the following word if pressed again.
            KC(K_OPTION, K.SHIFT, K.RIGHT): KC(K.R_CTRL, K.L_SHIFT, K.RIGHT),
            # Control-A: Move to the beginning of the line or paragraph.
            KC(K.L_CTRL, K.A): KC(K.HOME),
            # Control-E: Move to the end of a line or paragraph.
            KC(K.L_CTRL, K.E): KC(K.END),
            # Control-F: Move one character forward.
            KC(K.L_CTRL, K.F): KC(K.RIGHT),
            # Control-B: Move one character backward.
            KC(K.L_CTRL, K.B): KC(K.LEFT),
            ### Control-L: Center the cursor or selection in the visible area.
            # Control-P: Move up one line.
            KC(K.L_CTRL, K.P): KC(K.UP),
            # Control-N: Move down one line.
            KC(K.L_CTRL, K.N): KC(K.DOWN),
            ### Control-O: Insert a new line after the insertion point.
            ### Control-T: Swap the character behind the insertion point with the character in front of the insertion point.
        },
        "globals.document_shortcuts",
    )

    # The below shortcuts are mapped to custom AHK hotkeys for special behaviors
    # Uses ALT + F13-F24
    pm.map_shortcut(
        None,
        {
            # Command-M: Minimize the front window to the Dock. To minimize all windows of the front app, press Option-Command-M.
            KC(K_CMD, K.M): KC(K.R_ALT, K.F13),
            KC(K_CMD, K_OPTION, K.M): KC(K.R_ALT, K.R_SHIFT, K.F13),
            # Command-H: Hide the windows of the front app. To view the front app but hide all other apps, press Option-Command-H.
            KC(K_CMD, K.H): KC(K.R_ALT, K.F14),
            KC(K_CMD, K_OPTION, K.H): KC(K.R_ALT, K.R_SHIFT, K.F14),
            # Control-K: Delete the text between the insertion point and the end of the line or paragraph.
            KC(K.L_CTRL, K.K): KC(K.R_ALT, K.F15),
        },
        "globals.custom",
    )

    # Inside of terminals, ctrl+hotkey should always mean ctrl+shift+hotkey
    terminals = ["WindowsTerminal"]
    pm.map_shortcut(
        terminals,
        {
            # for some reason, mapping to L_CTRL + SHIFT + KEY doesn't disable the original action
            # e.g. L_CTRL+SHIFT+C shouldn't send a SIGINT, but it does. The R_CTRL + L_SHIFT + C setting seems to correctly not send the SIGINT.
            KC(K_CMD, K.MINUS): KC(K.R_CTRL, K.L_SHIFT, K.MINUS),
            KC(K_CMD, K.EQUAL): KC(K.R_CTRL, K.L_SHIFT, K.EQUAL),
            KC(K_CMD, K.BACKSPACE): KC(K.R_CTRL, K.L_SHIFT, K.BACKSPACE),
            KC(K_CMD, K.W): KC(K.R_CTRL, K.L_SHIFT, K.W),
            KC(K_CMD, K.E): KC(K.R_CTRL, K.L_SHIFT, K.E),
            KC(K_CMD, K.R): KC(K.R_CTRL, K.L_SHIFT, K.R),
            KC(K_CMD, K.T): KC(K.R_CTRL, K.L_SHIFT, K.T),
            KC(K_CMD, K.Y): KC(K.R_CTRL, K.L_SHIFT, K.Y),
            KC(K_CMD, K.U): KC(K.R_CTRL, K.L_SHIFT, K.U),
            KC(K_CMD, K.I): KC(K.R_CTRL, K.L_SHIFT, K.I),
            KC(K_CMD, K.O): KC(K.R_CTRL, K.L_SHIFT, K.O),
            KC(K_CMD, K.P): KC(K.R_CTRL, K.L_SHIFT, K.P),
            KC(K_CMD, K.L_BRACE): KC(K.R_CTRL, K.L_SHIFT, K.L_BRACE),
            KC(K_CMD, K.R_BRACE): KC(K.R_CTRL, K.L_SHIFT, K.R_BRACE),
            KC(K_CMD, K.A): KC(K.R_CTRL, K.L_SHIFT, K.A),
            KC(K_CMD, K.S): KC(K.R_CTRL, K.L_SHIFT, K.S),
            KC(K_CMD, K.D): KC(K.R_CTRL, K.L_SHIFT, K.D),
            KC(K_CMD, K.F): KC(K.R_CTRL, K.L_SHIFT, K.F),
            KC(K_CMD, K.G): KC(K.R_CTRL, K.L_SHIFT, K.G),
            KC(K_CMD, K.H): KC(K.R_CTRL, K.L_SHIFT, K.H),
            KC(K_CMD, K.J): KC(K.R_CTRL, K.L_SHIFT, K.J),
            KC(K_CMD, K.K): KC(K.R_CTRL, K.L_SHIFT, K.K),
            KC(K_CMD, K.L): KC(K.R_CTRL, K.L_SHIFT, K.L),
            KC(K_CMD, K.SEMICOLON): KC(K.R_CTRL, K.L_SHIFT, K.SEMICOLON),
            KC(K_CMD, K.APOSTROPHE): KC(K.R_CTRL, K.L_SHIFT, K.APOSTROPHE),
            KC(K_CMD, K.TILDE): KC(K.R_CTRL, K.L_SHIFT, K.TILDE),
            KC(K_CMD, K.Z): KC(K.R_CTRL, K.L_SHIFT, K.Z),
            KC(K_CMD, K.X): KC(K.R_CTRL, K.L_SHIFT, K.X),
            KC(K_CMD, K.C): KC(K.R_CTRL, K.L_SHIFT, K.C),
            KC(K_CMD, K.V): KC(K.R_CTRL, K.L_SHIFT, K.V),
            KC(K_CMD, K.B): KC(K.R_CTRL, K.L_SHIFT, K.B),
            KC(K_CMD, K.N): KC(K.R_CTRL, K.L_SHIFT, K.N),
            KC(K_CMD, K.M): KC(K.R_CTRL, K.L_SHIFT, K.M),
            KC(K_CMD, K.COMMA): KC(K.R_CTRL, K.L_SHIFT, K.COMMA),
            KC(K_CMD, K.PERIOD): KC(K.L_CTRL, K.C),
            KC(K_CMD, K.SLASH): KC(K.R_CTRL, K.L_SHIFT, K.SLASH),
            # don't know what KPASTERISK is. Just the * key on numpad?
            # KC(K_CMD, K.NUM_MULTIPLY): KC(K.R_CTRL, K.L_SHIFT, K.NUM_MULTIPLY),
        },
        "terminals",
    )

    pm.generate()
