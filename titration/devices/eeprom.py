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
        self._google_sheet_interval = 20
        self._kp_value = 20.0
        self._ki_value = 28.0
        self._kd_value = 36.0
        self._thermal_correction = 12
        self.tank_id = 0

    def get_google_sheet_interval(self, default):
        """
        Get the google sheet interval from EEPROM
        """
        if self._google_sheet_interval is None:
            return default
        return self._google_sheet_interval

    def get_kp(self, default):
        """
        Get the Kp value from EEPROM
        """
        if self._kp_value is None:
            return default
        return float(self._kp_value)

    def get_ki(self, default):
        """
        Get the Ki value from EEPROM
        """
        if self._ki_value is None:
            return default
        return float(self._ki_value)

    def get_kd(self, default):
        """
        Get the Kd value from EEPROM
        """
        if self._kd_value is None:
            return default
        return float(self._kd_value)

    def get_thermal_correction(self, default):
        """
        Get the thermal correction value from EEPROM
        """
        if self._thermal_correction is None:
            return default
        return float(self._thermal_correction)
