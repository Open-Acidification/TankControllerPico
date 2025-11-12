"""
The file to hold the View PID Constants class
"""

import time

from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewPIDConstants(UIState):
    """
    Show PID constants, rotating every 3 seconds between Kp/Ki and Kd/PID state.

    This mirrors the firmware SeePIDConstants behavior:
    - for 3 seconds show Kp (line1) and Ki (line2)
    - next 3 seconds show Kd (line1) and PID: ON/OFF (line2)
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewPIDConstants class
        """
        super().__init__(titrator)
        self.previous_state = previous_state
        self._start_time = time.monotonic()

    def loop(self):
        """
        Rotate display between Kp/Ki and Kd/PID every 3 seconds.
        """
        elapsed = int(((time.monotonic() - self._start_time) / 3.0)) % 2
        if elapsed == 0:
            self.load_kp()
            self.load_ki()
        else:
            self.load_kd()
            self.load_pid()

    def load_kp(self):
        """
        Load the proportional gain (Kp) and display it on the specified line.
        """
        value = self.titrator.pid.kp_value
        self.titrator.lcd.print(f"Kp: {value}", line=1)

    def load_ki(self):
        """
        Load the integral gain (Ki) and display it on the specified line.
        """
        value = self.titrator.pid.ki_value
        self.titrator.lcd.print(f"Ki: {value}", line=2)

    def load_kd(self):
        """
        Load the derivative gain (Kd) and display it on the specified line.
        """
        value = self.titrator.pid.kd_value
        self.titrator.lcd.print(f"Kd: {value}", line=1)

    def load_pid(self):
        """
        Load the PID enabled state and display it on the specified line.
        """
        if self.titrator.ph_control.use_pid:
            self.titrator.lcd.print("PID: ON", line=2)
        else:
            self.titrator.lcd.print("PID: OFF", line=2)

    def handle_key(self, key):
        """
        Handle key presses to return to the previous state.
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
