"""
The file to hold the View Free Memory class
"""

from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewFreeMemory(UIState):
    """
    This is a class for the ViewFreeMemory state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        Initialize the ViewFreeMemory state
        :param titrator: The titrator object
        :param previous_state: The previous state to return to
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        Main loop for the ViewFreeMemory state
        """
        pass

    def handle_key(self, key):
        """
        Handle key input for the ViewFreeMemory state
        """
        if key == Keypad.KEY_4:  # Left key
            self._set_next_state(self.previous_state, True)
