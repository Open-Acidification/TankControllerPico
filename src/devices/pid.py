"""Host-side PID controller wrapper translated from the firmware header."""

from src.devices.eeprom import EEPROM


class PID:
    """
    Host-side PID controller wrapper translated from the firmware header.
    """

    def __init__(self):
        """
        The constructor for the mock PID class.
        """
        eeprom = EEPROM()

        self.kp_value = 100000.0
        self.ki_value = 0.0
        self.kd_value = 0.0

        try:
            self.kp_value = float(eeprom.get_kp())
            self.ki_value = float(eeprom.get_ki())
            self.kd_value = float(eeprom.get_kd())
        except Exception:
            pass
