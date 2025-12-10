"""Host-side PID controller wrapper translated from the firmware header."""


class PID:
    """
    Host-side PID controller wrapper translated from the firmware header.
    """

    def __init__(self, eeprom):
        """
        The constructor for the mock PID class.
        """
        self.eeprom = eeprom

    @property
    def kp_value(self):
        """Get Kp from EEPROM (always current)."""
        return self.eeprom.get_kp(100000.0)

    @property
    def ki_value(self):
        """Get Ki from EEPROM (always current)."""
        return self.eeprom.get_ki(0.0)

    @property
    def kd_value(self):
        """Get Kd from EEPROM (always current)."""
        return self.eeprom.get_kd(0.0)
