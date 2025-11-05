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
        self.kp_address = 20
        self.ki_address = 28
        self.kd_address = 36
