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
        self.correction = 0.0
        self.eeprom = EEPROM()

        try:
            self.correction = float(self.eeprom.thermal_correction)
        except Exception:
            self.correction = None

        if self.correction is None or (
            isinstance(self.correction, float) and math.isnan(self.correction)
        ):
            self.correction = 0.0

            # self.correction = self.eeprom.set_thermal_correction(value)
            # consider adding get_float() as seen in pid.py
