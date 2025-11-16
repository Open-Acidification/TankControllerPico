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
        self.google_sheet_interval = 20
        self.kp_value = 20.0
        self.ki_value = 28.0
        self.kd_value = 36.0

    def get_kp(self):
        """
        Get the Kp value from EEPROM
        """
        return self.kp_value

    def get_ki(self):
        """
        Get the Ki value from EEPROM
        """
        return self.ki_value

    def get_kd(self):
        """
        Get the Kd value from EEPROM
        """
        return self.kd_value
