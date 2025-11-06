"""
The file for the ThermalProbe class
"""
import math
from titration.devices.eeprom import EEPROM


class ThermalProbe:
    """
    The class for the ThermalProbe
    """

    def __init__(self):
        """
        The constructor function for the ThermalProbe class
        """
        self.correction = 0
        self.eeprom = EEPROM()
        if math.isnan(self.eeprom.thermal_correction_address):
            self.correction = 0
            # self.correction = self.eeprom.set_thermal_correction(value)
        else:
            self.correction = self.eeprom.thermal_correction_address

        # floattostrf(self.correction, 5, 2, buffer, sizeof(buffer));
        # serial(F("Temperature probe with correction of %s"), buffer);
