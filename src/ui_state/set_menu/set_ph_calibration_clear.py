"""
The file to hold the PHCalibrationClear class
"""

from src.ui_state.user_value import UserValue
from src.ui_state.view_menu.view_ph_calibration import ViewPHCalibration


class ResetPHCalibration(UserValue):
    """
    This is a class for the ResetPHCalibration state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return "A: Clear pH Cali"

    def handle_key(self, key):
        """
        Handles key presses and updates the display accordingly.
        """
        if key == "A":
            self.titrator.ph_probe.clear_calibration()
            self._set_next_state(ViewPHCalibration(self.titrator, self), True)
        else:
            super().handle_key(key)
