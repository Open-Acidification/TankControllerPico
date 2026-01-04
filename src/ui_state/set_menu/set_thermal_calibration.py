"""
The file to hold the Set Thermal Calibration class
"""

from src.ui_state.user_value import UserValue


class SetThermalCalibration(UserValue):
    """
    This is a class for the SetThermalCalibration state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.thermal_probe.get_thermal_correction())

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "Real Temperature"

    def save_value(self):
        """
        Saves the thermal calibration value to the thermal probe.
        """
        self.titrator.thermal_probe.set_thermal_correction(self.value)
        self.titrator.lcd.print(
            f"New correction={self.titrator.thermal_probe.get_thermal_correction()}",
            line=2,
        )
        self.return_to_main_menu(ms_delay=3000)
