"""
The file to hold the View Version class
"""

from tank_controller.devices.library import Keypad
from tank_controller.ui_state.ui_state import UIState


class ViewVersion(UIState):
    """
    This is a class for the ViewVersion state of the Tank Controller
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
