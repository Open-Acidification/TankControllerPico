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
        self._highpoint_calibration = None
        self._lowpoint_calibration = None
        self._midpoint_calibration = None

    def clear_calibration(self):
        """
        Clear the calibration response string
        """
        self.slope_is_out_of_range = False
        self.eeprom.set_ignore_bad_ph_slope(False)
        self._calibration_response = ""

    def get_calibration(self):
        """
        Get the calibration response string
        """
        return self._calibration_response

    def get_ph_value(self):
        """
        Get the current pH value from the mock probe
        """
        return self._value

    def get_slope(self):
        """
        Get the slope response string
        """
        return self._slope_response

    def set_ph_value(self, ph_value):
        """
        Set the current pH value for the mock probe
        """
        self._value = ph_value

    def set_highpoint_calibration(self, highpoint):
        """
        Set the highpoint calibration value for the pH probe.
        """
        self.slope_is_out_of_range = False
        self.eeprom.set_ignore_bad_ph_slope(False)
        self._highpoint_calibration = highpoint
        buffer = f"Cal,High,{int(highpoint)}.{int(highpoint * 1000 + 0.5) % 1000}\r"
        print(buffer)  # Simulate sending the string to the Atlas Scientific product
        print(
            f"PHProbe::setHighpointCalibration({int(highpoint)}.{int(highpoint * 1000) % 1000})"
        )

    def set_lowpoint_calibration(self, lowpoint):
        """
        Set the lowpoint calibration value for the pH probe.
        """
        self.slope_is_out_of_range = False
        self.eeprom.set_ignore_bad_ph_slope(False)
        self._lowpoint_calibration = lowpoint
        buffer = f"Cal,low,{int(lowpoint)}.{int(lowpoint * 1000 + 0.5) % 1000}\r"
        print(buffer)  # Simulate sending the string to the Atlas Scientific product
        print(
            f"PHProbe::setLowpointCalibration({int(lowpoint)}.{int(lowpoint * 1000) % 1000})"
        )

    def set_midpoint_calibration(self, midpoint):
        """
        Set the midpoint calibration value for the pH probe.
        """
        self.slope_is_out_of_range = False
        self.eeprom.set_ignore_bad_ph_slope(False)
        self._midpoint_calibration = midpoint
        buffer = f"Cal,mid,{int(midpoint)}.{int(midpoint * 1000 + 0.5) % 1000}\r"
        print(buffer)  # Simulate sending the string to the Atlas Scientific product
        print(
            f"PHProbe::setMidpointCalibration({int(midpoint)}.{int(midpoint * 1000) % 1000})"
        )

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
