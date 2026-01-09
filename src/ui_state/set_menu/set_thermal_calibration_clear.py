"""
The file to hold the ThermalCalibrationClear class
"""

from src.ui_state.user_value import UserValue


class ResetThermalCalibration(UserValue):
    """
    This is a class for the ThermalCalibration state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "A: Clear TempCal"

    def handle_key(self, key):
        """
        Handles key presses and updates the display accordingly.
        """
        if key == "A":
            self.titrator.thermal_probe.clear_thermal_correction()
            self.titrator.lcd.print("Cleared TempCali", line=1)
            self.return_to_main_menu(ms_delay=3000)
        else:
            super().handle_key(key)
