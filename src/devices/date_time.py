"""
Docstring for src.devices.date_time
"""

from datetime import datetime, timedelta


class DateTime:
    """
    Docstring for DateTime
    """

    def __init__(self):
        self._offset = timedelta(0)
        self._uptime_start = datetime.now()

    def current(self):
        """
        Returns the current date and time.
        """
        return datetime.now() - self._offset

    def now(self):
        """
        Equivalent to the C++ DateTime_TC::now() method.

        Returns the current DateTime object.
        """
        return self.current()

    def offset(self, new_time=None):
        """
        Returns the current offset from UTC.
        """
        if new_time is not None:
            self._offset = datetime.now() - new_time
        return self._offset

    def set_as_current(self, new_time):
        """
        Equivalent to the C++ setAsCurrent() method.

        In the mock simulation, we cannot change the computer's
        system clock, so we update the offset instead.

        In the Pico version, this method will write the time to
        the hardware RTC.
        """
        self.offset(new_time)

    def as16_character_string(self):
        """
        Return the current time formatted for the LCD.

        Example:
            2026-07-29 14:35

        Matches the C++ format:
            YYYY-MM-DD hh:mm
        """
        return self.current().strftime("%Y-%m-%d %H:%M")

    def print_to_serial(self):
        """
        Equivalent to the C++ printToSerial() helper.

        Prints the current simulated time including seconds.
        """
        print(self.current().strftime("%Y-%m-%d %H:%M:%S"))

    def year_month_as_path(self):
        """
        Return a folder path based on the current year and month.

        Example:
            /2026/07

        Used by the Tank Controller when organizing log files.
        """
        return self.current().strftime("/%Y/%m")

    def uptime(self):
        """
        Returns the uptime as a timedelta since the system was started.
        """
        return datetime.now() - self._uptime_start
