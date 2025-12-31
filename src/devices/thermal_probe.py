"""
The file for the ThermalProbe class
"""


class ThermalProbe:
    """
    The class for the ThermalProbe
    """

    def __init__(self, eeprom):
        """
        The constructor function for the ThermalProbe class
        """
        self.eeprom = eeprom

        self._correction = 12

    def get_thermal_correction(self):
        """
        Get the thermal correction value from EEPROM
        """
        return float(self._correction)

    def set_thermal_correction(self, value):
        """
        Set the thermal correction value in EEPROM
        """
        self._correction = value
