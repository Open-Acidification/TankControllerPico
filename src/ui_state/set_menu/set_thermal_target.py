"""
The file to hold the Set Thermal Target class
"""

from src.ui_state.user_value import UserValue


class SetThermalTarget(UserValue):
    """
    This is a class for the SetThermalTarget state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        Constructor for the SetThermalTarget class
        """
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.prompts = ["Set Temperature", "Set ramp hours:"]
        self.values = [0.0] * 2
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
        self.values[self.sub_state] = float(self.value)
        self.sub_state += 1

        if self.sub_state < len(self.values):
            self.value = ""
        else:
            self.titrator.thermal_control.set_base_thermal_target(self.values[0])
            self.titrator.thermal_control.set_ramp_duration_hours(self.values[1])

            self.titrator.lcd.print(f"New Temp={self.values[0]:.2f}", line=1)
            self.titrator.lcd.print(f"New Ramp={self.values[1]:.2f}", line=2)

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
