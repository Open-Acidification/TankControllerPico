"""
The file to hold the View Version class
"""

from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewVersion(UIState):
    """
    This is a class for the ViewVersion state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewVersion class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The loop function for the ViewVersion class
        """
        self.titrator.lcd.print("Software Version", line=1)
        self.titrator.lcd.print(f"{self.titrator.version()}", line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewVersion class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
