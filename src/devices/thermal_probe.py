"""
The file for the ThermalProbe class
"""

import time


class ThermalProbe:
    """
    The class for the ThermalProbe
    """

    HISTORY_SIZE = 10

    def __init__(self, eeprom):
        """
        The constructor function for the ThermalProbe class
        """
        self.eeprom = eeprom

        self._correction = 12

        self.history = [0.0] * self.HISTORY_SIZE
        self.history_index = 0
        self.first_time = True
        self.last_time = 0

    def get_thermal_correction(self):
        """
        Get the thermal correction value from EEPROM
        """
        return float(self._correction)

    def clear_thermal_correction(self):
        """
        Clear the thermal correction value in EEPROM
        """
        self._correction = 0

    def set_thermal_correction(self, value):
        """
        Set the thermal correction value in EEPROM
        """
        self._correction = value

    def get_uncorrected_running_average(self):
        """
        Calculate the uncorrected running average of temperature readings.
        """
        current_time = time.time()  # Get current time in seconds
        if (
            self.first_time or self.last_time + 1 <= current_time
        ):  # Check if 1 second has passed
            temperature = self.get_raw_temperature()
            if self.first_time:
                # Initialize the history buffer with the first temperature reading
                self.history = [temperature] * self.HISTORY_SIZE
                self.first_time = False

            # Update the history buffer with the new temperature reading
            self.history_index = (self.history_index + 1) % self.HISTORY_SIZE
            self.history[self.history_index] = temperature
            self.last_time = current_time

        # Calculate the average of the history buffer, ignoring unused slots
        valid_readings = self.history[: self.history_index + 1]
        return sum(valid_readings) / len(valid_readings)

    def get_running_average(self):
        """
        Return the corrected running average within the range of 00.00-99.99
        """
        temperature = self.get_uncorrected_running_average() + self._correction
        if temperature < 0.0:
            temperature = 0.0
        elif temperature > 99.99:
            temperature = 99.99
        return temperature

    def get_raw_temperature(self):
        """
        Simulate reading the raw temperature from a sensor.
        In a real implementation, this method would interface with hardware.
        """
        # Placeholder for actual sensor reading logic
        return 25.0  # return thermo.temperature(RTDnominal, refResistor);
