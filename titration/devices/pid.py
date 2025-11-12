"""Host-side PID controller wrapper translated from the firmware header."""

import math

from titration.devices.eeprom import EEPROM


class PID:
    """Host-side PID controller wrapper translated from the firmware header."""

    def __init__(self):
        """The constructor for the mock PID class."""
        eeprom = EEPROM()

        try:
            self.kp_value = float(eeprom.get_kp())
        except Exception:
            self.kp_value = None
        try:
            self.ki_value = float(eeprom.get_ki())
        except Exception:
            self.ki_value = None
        try:
            self.kd_value = float(eeprom.get_kd())
        except Exception:
            self.kd_value = None
        if self.kp_value is None or (
            isinstance(self.kp_value, float) and math.isnan(self.kp_value)
        ):
            self.kp_value = 100000.0
        if self.ki_value is None or (
            isinstance(self.ki_value, float) and math.isnan(self.ki_value)
        ):
            self.ki_value = 0.0
        if self.kd_value is None or (
            isinstance(self.kd_value, float) and math.isnan(self.kd_value)
        ):
            self.kd_value = 0.0
