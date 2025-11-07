"""
The file for the EEPROM class
"""


class EEPROM:
    """
    The class for the EEPROM
    """

    def __init__(self):
        """
        The constructor function for the EEPROM class
        """
        self.google_sheet_interval = 108
        self.kp = 20.0
        self.ki = 28.0
        self.kd = 36.0

    def get_kp(self):
        """
        Get the Kp value from EEPROM
        """
        return self.kp

    def get_ki(self):
        """
        Get the Ki value from EEPROM
        """
        return self.ki

    def get_kd(self):
        """
        Get the Kd value from EEPROM
        """
        return self.kd
