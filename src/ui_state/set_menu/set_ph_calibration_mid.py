"""
The file to hold the Set pH Calibration Midpoint class
"""

from src.ui_state.set_menu.set_ph_calibration_high import PHCalibrationHigh
from src.ui_state.set_menu.set_ph_calibration_low import PHCalibrationLower
from src.ui_state.user_value import UserValue


class PHCalibrationOnly(UserValue):
    """
    UI state to set the pH Calibration Midpoint.
    Uses UserValue's keypad flow: implement get_label and save_value.
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.ph_probe._midpoint_calibration or "")

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "Buffer pH"

    def save_value(self):
        """
        Saves the entered pH Calibration Midpoint to the pH probe.
        """
        self.titrator.ph_probe._midpoint_calibration = float(self.value)

        self.titrator.lcd.print(
            f"Buffer = {self.titrator.ph_probe._midpoint_calibration}", line=2
        )
        self.return_to_main_menu(ms_delay=3000)


class PHCalibrationHigher(UserValue):
    """
    Docstring for PHCalibrationHigher
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.ph_probe._midpoint_calibration or "")

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "Higher buffer pH"

    def save_value(self):
        """
        Saves the entered pH Calibration Midpoint to the pH probe.
        """
        self.titrator.ph_probe._midpoint_calibration = float(self.value)

        self.titrator.lcd.print(
            f"Mid = {self.titrator.ph_probe._midpoint_calibration}", line=2
        )
        self._set_next_state(PHCalibrationLower(self.titrator, self), True)


class PHCalibrationMid(UserValue):
    """
    UI state to set the pH Calibration Midpoint.
    Uses UserValue's keypad flow: implement get_label and save_value.
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.ph_probe._midpoint_calibration or "")

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "Mid buffer pH"

    def save_value(self):
        """
        Saves the entered pH Calibration Midpoint to the pH probe.
        """
        self.titrator.ph_probe._midpoint_calibration = float(self.value)

        self.titrator.lcd.print(
            f"Mid = {self.titrator.ph_probe._midpoint_calibration}", line=2
        )
        self._set_next_state(PHCalibrationHigh(self.titrator, self), True)
