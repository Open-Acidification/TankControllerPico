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
        self.thermal_correction_address = "test"

    def set_thermal_correction(self, value):
        """
        Set the thermal correction value from EEPROM
        """
        self.thermal_correction_address = value
