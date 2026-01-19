"""
A file for the ThermalControl class
"""

import time


class ThermalControl:
    """
    The class for the ThermalControl
    """

    FLAT_TYPE = 0
    RAMP_TYPE = 1
    SINE_TYPE = 2

    def __init__(self, titrator):
        """
        The constructor function for the ThermalControl class
        """
        self.titrator = titrator
        self._heat = bool(True)
        self._base_thermal_target = 78
        self._current_thermal_target = 67
        self._thermal_function_type = ThermalControl.FLAT_TYPE
        self._ramp_time_start_seconds = 0
        self._ramp_time_end_seconds = 0
        self._ramp_initial_value = 0.0
        self._amplitude = 0.0
        self._period_in_seconds = 0

    def get_amplitude(self):
        """
        Get the amplitude for the pH function.
        """
        return self._amplitude

    def get_base_thermal_target(self):
        """
        Get the base thermal target
        """
        return self._base_thermal_target

    def get_current_thermal_target(self):
        """
        Get the current thermal target
        """
        return self._current_thermal_target

    def get_heat(self, default):
        """
        Get the heat setting from EEPROM
        """
        if self._heat is None:
            return default
        return self._heat

    def get_period_in_seconds(self):
        """
        Get the period in seconds for the pH function.
        """
        return self._period_in_seconds

    def get_ramp_time_end(self):
        """
        Get the ramp time end in seconds.
        """
        return (
            self._ramp_time_end_seconds
            if self._thermal_function_type != ThermalControl.FLAT_TYPE
            else 0
        )

    def get_ramp_time_start(self):
        """
        Get the ramp time start in seconds.
        """
        return (
            self._ramp_time_start_seconds
            if self._thermal_function_type != ThermalControl.FLAT_TYPE
            else 0
        )

    def get_thermal_function_type(self):
        """
        Get the current thermal function type.
        """
        return self._thermal_function_type

    def set_amplitude(self, amplitude):
        """
        Set the amplitude for the pH function.
        """
        self._amplitude = amplitude

    def set_base_thermal_target(self, value):
        """
        Set the base thermal target
        """
        self._base_thermal_target = value

    def set_current_thermal_target(self, value):
        """
        Set the current thermal target
        """
        self._current_thermal_target = value

    def set_heat(self, value):
        """
        Set the heat setting in EEPROM
        """
        self._heat = value

    def set_ramp_duration_hours(self, new_ph_ramp_duration):
        """
        Set the ramp duration in hours. If the duration is greater than 0, configure ramp parameters;
        otherwise, set the function type to FLAT_TYPE.
        """
        if new_ph_ramp_duration > 0:
            current_ramp_time = (
                self._ramp_time_end_seconds - self._ramp_time_start_seconds
            )
            current_ramp_time_str = f"{current_ramp_time:.3f}"
            new_ramp_duration_str = f"{new_ph_ramp_duration:.3f}"
            print(
                f"Change ramp time from {current_ramp_time_str} to {new_ramp_duration_str}"
            )

            self._ramp_time_start_seconds = int(time.monotonic())
            self._ramp_time_end_seconds = self._ramp_time_start_seconds + int(
                new_ph_ramp_duration * 3600
            )

            self._ramp_initial_value = self.titrator.thermal_probe.get_running_average()
            self._thermal_function_type = ThermalControl.RAMP_TYPE
        else:
            self._ramp_time_end_seconds = 0
            self._thermal_function_type = ThermalControl.FLAT_TYPE
            print("Set ramp time to 0")

    def set_sine_amplitude_and_hours(self, amplitude, period_in_hours):
        """
        Set the amplitude and period (in hours) for the sine wave pH function.
        """
        if amplitude > 0 and period_in_hours > 0:
            self._amplitude = amplitude
            self._period_in_seconds = int(period_in_hours * 3600)
            self._thermal_function_type = ThermalControl.SINE_TYPE
        else:
            raise ValueError("Amp and period !> than 0.")

    def set_thermal_function_type(self, function_type):
        """
        Set the current thermal function type.
        """
        if function_type in (
            ThermalControl.FLAT_TYPE,
            ThermalControl.RAMP_TYPE,
            ThermalControl.SINE_TYPE,
        ):
            self._thermal_function_type = function_type
        else:
            raise ValueError("Invalid thermal function type")
