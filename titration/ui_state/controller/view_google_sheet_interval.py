"""
The file to hold the View Google Sheet Interval class
"""
from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewGoogleSheetInterval(UIState):
    """
    This is a class for the ViewGoogleSheetInterval state of the Tank Controller
    """
    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        self.titrator.lcd.print("Google Mins:", line=1)
        self.titrator.lcd.print(f"{self.titrator.eeprom.google_sheet_interval}", line=2)

    def handle_key(self, key):
        if key == Keypad.KEY_4 or key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)
