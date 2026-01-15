"""
The file for the ViewPh class, which displays the buffer nominal pH value on the LCD.
"""

import time

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class ViewPH(UIState):
    """
    Show pH-related information, rotating every 3 seconds between two sets of displays.

    This mirrors the firmware SeePh behavior:
    - for 3 seconds, show header and values.
    - next 3 seconds, show pH function type and type variables.
    """

    def __init__(self, titrator, previous_state=None):
        """
        The constructor for the ViewPH class
        """
        super().__init__(titrator)
        self.previous_state = previous_state
        self._start_time = time.monotonic()

    def loop(self):
        """
        Rotate display between header/values and pH function/type variables every 3 seconds.
        """
        elapsed = int(((time.monotonic() - self._start_time) / 3.0)) % 2
        if elapsed == 0:
            self.load_header(line=1)
            self.load_values(line=2)
        else:
            self.load_ph_function_type(line=1)
            self.load_type_variables(line=2)

    def load_header(self, line):
        """
        Write the header "Now  Next  Goal" to the specified line on the LCD.
        """
        header = "Now  Next  Goal"
        self.titrator.lcd.print(header, line)

    def load_values(self, line):
        """
        Write the current pH, current target pH, and overall target pH values to the specified line on the LCD.
        """
        current_ph = self.titrator.ph_probe.get_ph_value()
        current_target_ph = self.titrator.ph_control.get_current_target_ph()
        overall_target_ph = self.titrator.ph_control.get_base_target_ph()

        values = f"{current_ph:.2f} {current_target_ph:.3f} {overall_target_ph:.3f}"
        self.titrator.lcd.print(values, line)

    def load_ph_function_type(self, line):
        """
        Display the current pH function type on the LCD.
        """
        ph_type = self.titrator.ph_control.get_ph_function_type()
        type_mapping = {
            self.titrator.ph_control.FLAT_TYPE: "flat",
            self.titrator.ph_control.RAMP_TYPE: "ramp",
            self.titrator.ph_control.SINE_TYPE: "sine",
        }
        type_str = type_mapping.get(ph_type, "????")
        message = f"type: {type_str}"
        self.titrator.lcd.print(message, line)

    def load_type_variables(self, line):
        """
        Display the variables related to the current pH function type on the LCD.
        """
        ph_type = self.titrator.ph_control.get_ph_function_type()

        if ph_type == self.titrator.ph_control.FLAT_TYPE:
            message = ""

        elif ph_type == self.titrator.ph_control.RAMP_TYPE:
            end_time = self.titrator.ph_control.get_ramp_time_end()
            current_time = int(time.monotonic())
            time_left = max(0, end_time - current_time)
            time_left_hours = time_left // 3600
            time_left_minutes = (time_left % 3600) // 60
            time_left_seconds = time_left % 60
            message = f"left: {time_left_hours}:{time_left_minutes}:{time_left_seconds}"

        elif ph_type == self.titrator.ph_control.SINE_TYPE:
            period_in_seconds = self.titrator.ph_control.get_period_in_seconds()
            period_hours = period_in_seconds / 3600.0
            amplitude = self.titrator.ph_control.get_amplitude()
            message = f"p={period_hours:.3f} a={amplitude:.3f}"

        else:
            # Default case
            message = "Invalid type"

        # Display the message on the specified line
        self.titrator.lcd.print(message, line)

    def handle_key(self, key):
        """
        Handle key presses to return to the previous state.
        """
        if key in [Keypad.KEY_4, Keypad.KEY_D]:
            self._set_next_state(self.previous_state, True)
