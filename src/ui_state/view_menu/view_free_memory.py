"""
The file to hold the View Free Memory class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewFreeMemory(UIState):
    """
    This is a class for the ViewFreeMemory state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewFreeMemory class
        """
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The loop function for the ViewFreeMemory class
        """
        free_memory = "3519"
        self.titrator.lcd.print("Free Memory:", line=1)
        self.titrator.lcd.print(f"{free_memory} bytes", line=2)

    def handle_key(self, key):
        """
        The handle_key function for the ViewFreeMemory class
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
