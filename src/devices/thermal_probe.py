"""
The file for the ThermalProbe class
"""

from src.devices.eeprom import EEPROM


class ThermalProbe:
    """
    The class for the ThermalProbe
    """

    def __init__(self):
        """
        The constructor function for the ThermalProbe class
        """
        self.correction = 0.0
        self.eeprom = EEPROM()

        try:
            self.correction = float(self.eeprom.thermal_correction)
        finally:
            pass
