"""
The file to hold the PHCalibration class
"""

from src.ui_state.set_menu.set_ph_calibration_mid import (
    PHCalibrationHigher,
    PHCalibrationMid,
    PHCalibrationOnly,
)
from src.ui_state.ui_state import UIState


class PHCalibration(UIState):
    """
    This is a class for the PHCalibration state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state

    def loop(self):
        """
        The main loop for the PHCalibration state
        """
        self.titrator.lcd.print("pH Cali: ", line=1)
        self.titrator.lcd.print("1,2 or 3 point?", line=2)

    def handle_key(self, key):
        """
        Handles key presses and updates the display accordingly.
        """
        if key == "1":
            self.titrator.lcd.print("1-pt pH calib...", line=2)
            self.return_to_main_menu(ms_delay=3000)
            self._set_next_state(PHCalibrationOnly(self.titrator, self), True)

        if key == "2":
            self.titrator.lcd.print("2 Point Cali", line=2)
            self._set_next_state(PHCalibrationHigher(self.titrator, self), True)

        if key == "3":
            self.titrator.lcd.print("3 Point Cali", line=2)
            self._set_next_state(PHCalibrationMid(self.titrator, self), True)

        if key == "4":
            self._set_next_state(self.previous_state, True)

        if key == "D":
            self.return_to_main_menu()
