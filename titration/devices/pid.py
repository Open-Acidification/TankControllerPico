"""Host-side PID controller wrapper translated from the firmware header."""

import math

from titration.devices.eeprom import EEPROM


class PID:
    """
    Host-side PID controller wrapper translated from the firmware header.
    """

    def __init__(self):
        """
        The constructor for the mock PID class.
        """
        eeprom = EEPROM()

        self.kp_value = self.get_float(eeprom.get_kp(), 100000.0)
        self.ki_value = self.get_float(eeprom.get_ki(), 0.0)
        self.kd_value = self.get_float(eeprom.get_kd(), 0.0)

    def get_float(self, getter_or_value, default_value):
        """
        Call getter_or_value (if callable) and return a finite float, otherwise default.
        """
        try:
            raw = getter_or_value() if callable(getter_or_value) else getter_or_value
        except Exception:
            return float(default_value)

        if isinstance(raw, bool):  # Reject bool which converts to 1.0/0.0 and is finite
            return float(default_value)

        try:
            val = float(raw)
        except (TypeError, ValueError):
            return float(default_value)

        if not math.isfinite(val):  # Only accept finite floats (reject NaN and +/-inf)
            return float(default_value)

        return val
