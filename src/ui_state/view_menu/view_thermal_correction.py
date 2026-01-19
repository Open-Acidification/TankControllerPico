"""
The file to hold the View Thermal Correction class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewThermalCorrection(UIState):
    """
    This is a class for the ViewThermalCorrection state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewThermalCorrection class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The loop function for the ViewThermalCorrection class
        """
        self.titrator.lcd.print("Temp Cal Offset:", line=1)
        self.titrator.lcd.print(
            f"{self.titrator.thermal_probe.get_thermal_correction()}", line=2
        )

    def handle_key(self, key):
        """
        The handle_key function for the ViewThermalCorrection class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
