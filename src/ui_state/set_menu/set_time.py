"""
The file to hold the Set Time class
"""

from datetime import datetime

from src.ui_state.user_value import UserValue


class SetTime(UserValue):
    """
    This is a class for the SetTime state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.prompts = [
            "Set Year (YYYY):",
            "Month (1-12):",
            "Day (1-31):",
            "Hour (0-23):",
            "Minute (0-59):",
        ]
        self.values = [0] * 5
        self.sub_state = 0

    def get_label(self):
        """
        Returns the label for the user value input.
        """
        return self.prompts[self.sub_state]

    def save_value(self):
        """
        Saves the entered value for the current sub-state and advances to the next sub-state.
        """
        self.values[self.sub_state] = self.value
        self.sub_state += 1

        if self.sub_state == len(self.values):
            try:
                new_time = datetime(
                    int(self.values[0]),
                    int(self.values[1]),
                    int(self.values[2]),
                    int(self.values[3]),
                    int(self.values[4]),
                )
                self.titrator.date_time.offset(new_time)
                self.titrator.lcd.print("New Date/Time:", line=1)
                self.titrator.lcd.print(new_time.strftime("%Y-%m-%d %H:%M"), line=2)
                self.return_to_main_menu(ms_delay=3000)

            except ValueError as errormsg:
                self.titrator.lcd.print("Invalid Date/Time", line=1)
                self.titrator.lcd.print(str(errormsg), line=2)
                self.return_to_main_menu(ms_delay=3000)

    def handle_key(self, key):
        """
        Handles key presses and updates the display accordingly.
        """
        if key == "A" and self.value not in ("", "."):
            self.save_value()
            self.value = ""
        else:
            super().handle_key(key)
