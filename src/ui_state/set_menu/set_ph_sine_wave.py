"""
The file to hold the Set PH Sine Wave class
"""

from src.ui_state.user_value import UserValue


class SetPHSineWave(UserValue):
    """
    This is a class for the SetPHSineWave state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        """
        Constructor for the SetPHSineWave class
        """
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.prompts = [
            "Set pH Mean:",
            "Set Amplitude:",
            "Set Period hrs:",
        ]
        self.values = [0.0] * 3
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
            self.titrator.ph_control.set_base_target_ph(self.values[0])
            self.titrator.ph_control.set_sine_amplitude_and_hours(
                self.values[1], self.values[2]
            )

            ph_mean = f"New pH={self.values[0]:.3f}"
            amplitude_and_period = f"A={self.values[1]:.3f} P={self.values[2]:.3f}"
            self.titrator.lcd.print(ph_mean, line=1)
            self.titrator.lcd.print(amplitude_and_period, line=2)

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
