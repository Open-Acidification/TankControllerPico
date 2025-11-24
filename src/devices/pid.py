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

        self.kp_value = eeprom.get_kp(100000.0)
        self.ki_value = eeprom.get_ki(0.0)
        self.kd_value = eeprom.get_kd(0.0)
