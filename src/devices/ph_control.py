"""
The file for the PH Control class
"""

import time


class PHControl:
    """
    The class for the PH Control
    """

    FLAT_TYPE = 0
    RAMP_TYPE = 1
    SINE_TYPE = 2

    def __init__(self, titrator):
        """
        The constructor function for the PH Control class
        """
        self.titrator = titrator
        self.use_pid = bool(True)
        self._base_target_ph = 8.125
        self._current_target_ph = 8.5
        self._ph_function_type = PHControl.FLAT_TYPE  # Default to FLAT_TYPE
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

    def get_base_target_ph(self):
        """
        Get the base target pH value
        """
        return self._base_target_ph

    def get_current_target_ph(self):
        """
        Get the current target pH value
        """
        return self._current_target_ph

    def get_period_in_seconds(self):
        """
        Get the period in seconds for the pH function.
        """
        return self._period_in_seconds

    def get_ph_function_type(self):
        """
        Get the current pH function type.
        """
        return self._ph_function_type

    def get_ramp_time_end(self):
        """
        Get the ramp time end in seconds.
        """
        return (
            self._ramp_time_end_seconds
            if self._ph_function_type != PHControl.FLAT_TYPE
            else 0
        )

    def get_ramp_time_start(self):
        """
        Get the ramp time start in seconds.
        """
        return (
            self._ramp_time_start_seconds
            if self._ph_function_type != PHControl.FLAT_TYPE
            else 0
        )

    def set_amplitude(self, amplitude):
        """
        Set the amplitude for the pH function.
        """
        self._amplitude = amplitude

    def set_base_target_ph(self, target_ph):
        """
        Set the base target pH value
        """
        self._base_target_ph = target_ph

    def set_current_target_ph(self, target_ph):
        """
        Set the current target pH value
        """
        self._current_target_ph = target_ph

    def set_ph_function_type(self, function_type):
        """
        Set the current pH function type.
        """
        if function_type in (
            PHControl.FLAT_TYPE,
            PHControl.RAMP_TYPE,
            PHControl.SINE_TYPE,
        ):
            self._ph_function_type = function_type
        else:
            raise ValueError("Invalid pH function type")

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

            self._ramp_initial_value = self.titrator.ph_probe.get_ph_value()
            self._ph_function_type = PHControl.RAMP_TYPE
        else:
            self._ramp_time_end_seconds = 0
            self._ph_function_type = PHControl.FLAT_TYPE
            print("Set ramp time to 0")

    def set_sine_amplitude_and_hours(self, amplitude, period_in_hours):
        """
        Set the amplitude and period (in hours) for the sine wave pH function.
        """
        if amplitude > 0 and period_in_hours > 0:
            self._amplitude = amplitude
            self._period_in_seconds = int(period_in_hours * 3600)
            self._ph_function_type = PHControl.SINE_TYPE
        else:
            raise ValueError("Amp and period !> than 0.")
