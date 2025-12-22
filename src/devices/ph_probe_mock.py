"""
The file for the Mock pH probe
"""


class PHProbe:
    """
    Docstring for PHProbe
    """

    def __init__(self, eeprom):
        """
        The constructor for the PHProbe class
        """
        self.eeprom = eeprom
        self._value = 3.125
        self._calibration_response = "?CAL,3"
        self._slope_response = "99.7,100.3, -0.89"
        self.slope_is_out_of_range = False

    def get_ph_value(self):
        """
        Get the current pH value from the mock probe
        """
        return self._value

    def set_ph_value(self, ph_value):
        """
        Set the current pH value for the mock probe
        """
        self._value = ph_value

    def get_calibration(self):
        """
        Get the calibration response string
        """
        return self._calibration_response

    def clear_calibration(self):
        """
        Clear the calibration response string
        """
        self.slope_is_out_of_range = False
        self.eeprom.set_ignore_bad_ph_slope(False)
        self._calibration_response = ""

    def get_slope(self):
        """
        Get the slope response string
        """
        return self._slope_response

    def should_warn_about_calibration(self):
        """
        Determine if a calibration warning should be shown based on the slope and ignore settings.
        """
        if not self.slope_is_out_of_range:
            return False
        if self.slope_is_out_of_range and not self.eeprom.get_ignore_bad_ph_slope(
            False
        ):
            return True
        if self.slope_is_out_of_range and self.eeprom.get_ignore_bad_ph_slope(False):
            return False
        return False
