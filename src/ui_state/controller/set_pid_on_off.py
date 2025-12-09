"""
The file to hold the EnablePID class
"""

from src.ui_state.user_value.user_value import UserValue


class EnablePID(UserValue):
    """
    This is a class for the EnablePID state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(int(self.titrator.ph_control.use_pid))

    def get_label(self):
        """
        Returns the label to prompt user value input.
        """
        return "PID 1:on; 9:off"

    def save_value(self):
        """
        Saves the entered PID on/off value.
        """
        val = self.value
        if val not in (1.0, 9.0):
            self.titrator.lcd.print("Invalid entry", line=1)
            retry_state = EnablePID(self.titrator, self.previous_state)
            self.invalid_entry(retry_state, ms_delay=2000)
            return
        if val == 1.0:
            self.titrator.ph_control.use_pid = True
            self.titrator.lcd.print("PID enabled", line=1)
        elif val == 9.0:
            self.titrator.ph_control.use_pid = False
            self.titrator.lcd.print("PID disabled", line=1)
        self.return_to_main_menu(ms_delay=3000)
