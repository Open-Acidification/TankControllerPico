"""
The file to hold the PHCalibration class
"""

from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class PHCalibration(UIState):
    """
    This is a class for the PHCalibration state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state
        # Add any initialization logic here

    def loop(self):
        # Add main logic for this state
        pass

    def handle_key(self, key):
        # Handle key input for this state
        if key == Keypad.KEY_4:  # Left key
            self._set_next_state(self.previous_state, True)
