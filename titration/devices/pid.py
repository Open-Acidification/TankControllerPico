"""Host-side PID controller wrapper translated from the firmware header.
"""
import math
from titration.devices.eeprom import EEPROM


class PID:
    """Host-side PID controller wrapper translated from the firmware header."""
    def __init__(self):
        """The constructor for the mock PID class."""
        eeprom = EEPROM()

        try:
            self.kp = float(eeprom.kp_address)
        except Exception:
            self.kp = None
        try:
            self.ki = float(eeprom.ki_address)
        except Exception:
            self.ki = None
        try:
            self.kd = float(eeprom.kd_address)
        except Exception:
            self.kd = None

        if self.kp is None or (isinstance(self.kp, float) and math.isnan(self.kp)):
            self.kp = 100000.0
        if self.ki is None or (isinstance(self.ki, float) and math.isnan(self.ki)):
            self.ki = 0.0
        if self.kd is None or (isinstance(self.kd, float) and math.isnan(self.kd)):
            self.kd = 0.0

    #     self.reverse = bool(False)
    #     self.input = 0.0
    #     self.output = 0.0
    #     self.set_point = 0.0

    # def set_tunings(self, kp, ki, kd):
    #     """Set the PID tunings."""
    #     self.kp = float(kp)
    #     self.ki = float(ki)
    #     self.kd = float(kd)

    # def set_kd(self, kd):
    #     """Set the derivative gain (Kd)."""
    #     self.kd = float(kd)

    # def set_ki(self, ki):
    #     """Set the integral gain (Ki)."""
    #     self.ki = float(ki)

    # def set_kp(self, kp):
    #     """Set the proportional gain (Kp)."""
    #     self.kp = float(kp)

    # def compute(self):

    # def log_to_serial(self):
