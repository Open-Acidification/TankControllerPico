"""
The file for the ViewPh class, which displays the buffer nominal pH value on the LCD.
"""

from tank_controller.devices.keypad import Keypad
from tank_controller.ui_state.ui_state import UIState


class ViewPh(UIState):
    """
    UI state to display the buffer nominal pH value
    """

    def loop(self):
        # Display the buffer nominal pH value on the LCD
        value = getattr(self.tank_controller, "buffer_nominal_ph", None)
        if value is not None:
            self.tank_controller.lcd.print("Buffer Nominal pH:", line=1)
            self.tank_controller.lcd.print(f"{value}", line=2)
        else:
            self.tank_controller.lcd.print("Buffer Nominal pH:", line=1)
            self.tank_controller.lcd.print("Not set", line=2)
        self.tank_controller.lcd.print("", line=3)
        self.tank_controller.lcd.print("Any key to return", line=4)

    def handle_key(self, key):
        # Return to previous state on any key press
        if key == Keypad.KEY_4:  # Left key
            self._set_next_state(self.previous_state, True)
