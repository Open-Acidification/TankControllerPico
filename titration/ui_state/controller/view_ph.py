"""
The file for the ViewPh class, which displays the buffer nominal pH value on the LCD.
"""

from titration.devices.keypad import Keypad
from titration.ui_state.ui_state import UIState


class ViewPh(UIState):
    """
    UI state to display the buffer nominal pH value
    """

    def loop(self):
        """
        Main loop for the ViewPh state
        """
        value = getattr(self.titrator, "buffer_nominal_ph", None)
        if value is not None:
            self.titrator.lcd.print("Buffer Nominal pH:", line=1)
            self.titrator.lcd.print(f"{value}", line=2)
        else:
            self.titrator.lcd.print("Buffer Nominal pH:", line=1)
            self.titrator.lcd.print("Not set", line=2)
        self.titrator.lcd.print("", line=3)
        self.titrator.lcd.print("Any key to return", line=4)

    def handle_key(self, key):
        """
        Handle key input for the ViewPh state
        """
        if key == Keypad.KEY_4:  # Left key
            self._set_next_state(self.previous_state, True)
