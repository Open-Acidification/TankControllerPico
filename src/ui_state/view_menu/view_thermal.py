"""
The file to hold the View Thermal class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewThermal(UIState):
    """
    This is a class for the ViewThermal state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewThermal class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The loop function for the ViewThermal class
        """
        self.titrator.lcd.print("Avg    Raw", line=1)
        average = self.titrator.thermal_probe.get_running_average()
        raw = self.titrator.thermal_probe.get_raw_temperature()
        self.titrator.lcd.print(f"{average}   {raw}", line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewThermal class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
