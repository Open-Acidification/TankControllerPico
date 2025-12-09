"""
The file to hold the EnablePID class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class EnablePID(UIState):
    """
    This is a class for the EnablePID state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The main loop for the EnablePID state
        """
        self.titrator.lcd.print("PID 1:on; 9:off", line=1)

        if self.titrator.ph_control.use_pid:
            self.titrator.lcd.print("Currently enabled", line=2)
        else:
            self.titrator.lcd.print("Currently disabled", line=2)

    def handle_key(self, key):
        """
        Handle key presses to return to the previous state.
        """
        if key == Keypad.KEY_1:
            self.titrator.ph_control.use_pid = True
            self.titrator.lcd.print("PID enabled", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_9:
            self.titrator.ph_control.use_pid = False
            self.titrator.lcd.print("PID disabled", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_4:
            self._set_next_state(self.previous_state, True)

        if key == Keypad.KEY_D:
            self.return_to_main_menu()
