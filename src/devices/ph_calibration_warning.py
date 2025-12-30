"""
The file to hold the PH Calibration Warning class
"""

import time

from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_ph_calibration import ViewPHCalibration


class PHCalibrationWarning(UIState):
    """
    Constructor for the PHCalibrationWarning class.
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.start_time = time.monotonic()
        self.previous_state = previous_state

    def loop(self):
        """
        Handle the blinking warning message and user response prompts.
        """
        elapsed_time = (time.monotonic() - self.start_time) * 1000

        if elapsed_time % 8000 < 5000:
            if elapsed_time % 1000 < 700:
                self.titrator.lcd.print("BAD CALIBRATION?", line=1)
            else:
                self.titrator.lcd.print("", line=1)

            slope_response = self.titrator.ph_probe.get_slope()
            self.titrator.lcd.print(slope_response, line=2)
        else:
            self.titrator.lcd.print("A: Accept/ignore", line=1)
            self.titrator.lcd.print("C: Clear calibra", line=2)

    def handle_key(self, key):
        """
        Docstring for handle_key A and C
        """
        if key == "A":
            print("Setting ignore_bad_ph_slope to True")
            self.titrator.ph_probe.eeprom.set_ignore_bad_ph_slope(True)
            print("Ignore flag set. Returning to previous state.")
            self._set_next_state(self.previous_state, True)
        elif key == "C":
            self.titrator.ph_probe.clear_calibration()
            self._set_next_state(ViewPHCalibration(self.titrator, self), True)
