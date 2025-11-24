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

        self.correction = self.eeprom.get_thermal_correction(0.0)
