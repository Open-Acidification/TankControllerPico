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
        self._ignore_bad_ph_slope = False
        self._kd_value = 36.0
        self._ki_value = 28.0
        self._kp_value = 20.0
        self._tank_id = 1

    def get_google_sheet_interval(self, default):
        """
        Get the google sheet interval from EEPROM
        """
        if self._google_sheet_interval is None:
            return default
        return self._google_sheet_interval

    def get_ignore_bad_ph_slope(self, default):
        """
        Get the ignore bad pH slope setting from EEPROM
        """
        if self._ignore_bad_ph_slope is None:
            return default
        return self._ignore_bad_ph_slope

    def get_kd(self, default):
        """
        Get the Kd value from EEPROM
        """
        if self._kd_value is None:
            return default
        return float(self._kd_value)

    def get_ki(self, default):
        """
        Get the Ki value from EEPROM
        """
        if self._ki_value is None:
            return default
        return self._ki_value

    def get_kp(self, default):
        """
        Get the Kp value from EEPROM
        """
        if self._kp_value is None:
            return default
        return float(self._kp_value)

    def get_tank_id(self, default):
        """
        Get the tank ID from EEPROM
        """
        if self._tank_id is None:
            return default
        return self._tank_id

    def set_google_sheet_interval(self, value):
        """
        Set the google sheet interval in EEPROM
        """
        self._google_sheet_interval = value

    def set_ignore_bad_ph_slope(self, value):
        """
        Set the ignore bad pH slope setting in EEPROM
        """
        self._ignore_bad_ph_slope = value

    def set_kd(self, value):
        """
        Set the Kd value in EEPROM
        """
        self._kd_value = value

    def set_ki(self, value):
        """
        Set the Ki value in EEPROM
        """
        self._ki_value = value

    def set_kp(self, value):
        """
        Set the Kp value in EEPROM
        """
        self._kp_value = value

    def set_tank_id(self, value):
        """
        Set the tank ID in EEPROM
        """
        self._tank_id = value
