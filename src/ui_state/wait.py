"""
The file for the Wait class
"""

import time

from src.ui_state.main_menu import MainMenu
from src.ui_state.ui_state import UIState


class Wait(UIState):
    """
    A UI state that waits for a specified delay, then transitions to the next state.
    Replaces repetitive _return_at / time.monotonic() patterns.
    """

    def __init__(self, titrator, ms_delay=1000, next_state=None, previous_state=None):
        """
        Initialize the Wait state.

        Parameters:
            titrator: the Titrator instance
            ms_delay (int): delay in milliseconds before transitioning
            next_state (UIState): state to transition to after delay (defaults to MainMenu)
            previous_state (UIState): state to return to (unused but kept for consistency)
        """
        super().__init__(titrator, previous_state)
        self.ms_delay = ms_delay
        self.end_time = time.monotonic() + (ms_delay / 1000.0)  # convert ms to seconds

        if next_state is None:
            next_state = MainMenu(titrator)
        self.next_state = next_state

    def loop(self):
        """Check if delay elapsed and transition."""
        if time.monotonic() >= self.end_time:
            self._set_next_state(self.next_state, True)

    def handle_key(self, key):
        """Allow user to skip wait by pressing a key."""
        # optionally allow early exit (e.g. any key)
        self._set_next_state(self.next_state, True)
