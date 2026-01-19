"""
The file to hold the Set pH Calibration Highpoint class
"""

from src.ui_state.set_menu.set_ph_calibration_low import PHCalibrationLow
from src.ui_state.user_value import UserValue


class PHCalibrationHigh(UserValue):
    """
    UI state to set the pH Calibration Highpoint.
    Uses UserValue's keypad flow: implement get_label and save_value.
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.ph_probe._highpoint_calibration or "")

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "High buffer pH"

    def save_value(self):
        """
        Saves the entered pH Calibration Highpoint to the pH probe.
        """
        self.titrator.ph_probe.set_highpoint_calibration(float(self.value))

        self.titrator.lcd.print(
            f"High = {self.titrator.ph_probe._highpoint_calibration}", line=2
        )
        self._set_next_state(PHCalibrationLow(self.titrator, self), True)
