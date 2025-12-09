"""
The file to hold the View Time class
"""

from datetime import datetime

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewTime(UIState):
    """
    This is a class for the ViewTime state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewPIDConstants class
        """
        super().__init__(titrator)
        self.previous_state = previous_state
        self._start_time = datetime.now()

    def loop(self):
        """
        Loop to update the time display.
        """
        now = datetime.now()
        line1 = (
            f"{now.year:04d}-{now.month:02d}-{now.day:02d} "
            f"{now.hour:02d}:{now.minute:02d}"
        )
        self.titrator.lcd.print(line1, line=1)

        elapsed = datetime.now() - self._start_time
        days = elapsed.days
        hours, rem = divmod(elapsed.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        uptime_str = f"Up d:{days:02d} {hours:02d}:{minutes:02d}:{seconds:02d}"
        self.titrator.lcd.print(uptime_str, line=2)

    def handle_key(self, key):
        """
        Handle key presses to return to the previous state.
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
