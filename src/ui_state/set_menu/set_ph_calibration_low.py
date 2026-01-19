"""
The file to hold the Set pH Calibration Lowpoint class
"""

from src.ui_state.user_value import UserValue


class PHCalibrationLower(UserValue):
    """
    Docstring for PHCalibrationLower
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.ph_probe._lowpoint_calibration or "")

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "Lower buffer pH"

    def save_value(self):
        """
        Saves the entered pH Calibration Lowpoint to the pH probe.
        """
        self.titrator.ph_probe._lowpoint_calibration = float(self.value)

        self.titrator.lcd.print(
            f"Low = {self.titrator.ph_probe._lowpoint_calibration}", line=2
        )
        self.return_to_main_menu(ms_delay=3000)


class PHCalibrationLow(UserValue):
    """
    UI state to set the pH Calibration Lowpoint.
    Uses UserValue's keypad flow: implement get_label and save_value.
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.ph_probe._lowpoint_calibration or "")

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "Low buffer pH"

    def save_value(self):
        """
        Saves the entered pH Calibration Lowpoint to the pH probe.
        """
        self.titrator.ph_probe.set_lowpoint_calibration(float(self.value))

        self.titrator.lcd.print(
            f"Low = {self.titrator.ph_probe._lowpoint_calibration}", line=2
        )
        self.return_to_main_menu(ms_delay=3000)
