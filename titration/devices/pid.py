"""Host-side PID controller wrapper translated from the firmware header."""

import math

from titration.devices.eeprom import EEPROM


class PID:
    """Host-side PID controller wrapper translated from the firmware header."""

    def __init__(self):
        """The constructor for the mock PID class."""
        eeprom = EEPROM()

        try:
            self.kp = float(eeprom.get_kp())
        except Exception:
            self.kp = None
        try:
            self.ki = float(eeprom.get_ki())
        except Exception:
            self.ki = None
        try:
            self.kd = float(eeprom.get_kd())
        except Exception:
            self.kd = None

        if self.kp is None or (isinstance(self.kp, float) and math.isnan(self.kp)):
            self.kp = 100000.0
        if self.ki is None or (isinstance(self.ki, float) and math.isnan(self.ki)):
            self.ki = 0.0
        if self.kd is None or (isinstance(self.kd, float) and math.isnan(self.kd)):
            self.kd = 0.0
