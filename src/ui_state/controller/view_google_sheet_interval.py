"""
The file to hold the View Google Sheet Interval class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewGoogleSheetInterval(UIState):
    """
    This is a class for the ViewGoogleSheetInterval state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewGoogleSheetInterval class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The loop function for the ViewGoogleSheetInterval class
        """
        self.titrator.lcd.print("Google Mins:", line=1)
        self.titrator.lcd.print(f"{self.titrator.eeprom.google_sheet_interval}", line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewGoogleSheetInterval class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
