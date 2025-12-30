"""
The file to hold the View PH Calibration class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewPHCalibration(UIState):
    """
    This is a class for the ViewPHCalibration state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewPHCalibration class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        self.titrator.lcd.print(f"{self.titrator.ph_probe.get_calibration()}", line=1)
        self.titrator.lcd.print(f"{self.titrator.ph_probe.get_slope()}", line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewGoogleSheetInterval class
        """
        if key == Keypad.KEY_4:
            self._set_next_state(self.previous_state, True)

        if key == Keypad.KEY_D:
            self.return_to_main_menu()
