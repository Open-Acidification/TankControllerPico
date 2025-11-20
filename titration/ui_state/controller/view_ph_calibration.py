"""
The file to hold the View PH Calibration class
"""

from titration.devices.library import Keypad
from titration.devices.ph_probe import PHProbe
from titration.ui_state.ui_state import UIState


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
        """
        The loop function for the ViewPHCalibration class
        """

        ph_device = PHProbe()

        ph_device.send_calibration_request()
        ph_device.send_slope_request()

        points = ph_device.get_calibration(20)
        slope = ph_device.get_slope(20)

        self.titrator.lcd.print(points, line=1)
        self.titrator.lcd.print(slope, line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewPHCalibration class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
