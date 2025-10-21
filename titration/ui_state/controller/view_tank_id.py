"""
The file to hold the View Tank ID class
"""

from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewTankID(UIState):
    """
    This is a class for the ViewTankID state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        Initialize the ViewTankID state
        :param titrator: The titrator object
        :param previous_state: The previous state to return to
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        Main loop for the ViewTankID state
        """
        pass

    def handle_key(self, key):
        """
        Handle key input for the ViewTankID state
        """
        if key == Keypad.KEY_4:  # Left key
            self._set_next_state(self.previous_state, True)
