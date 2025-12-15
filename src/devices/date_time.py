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

    def offset(self, new_time=None):
        """
        Returns the current offset from UTC.
        """
        if new_time is not None:
            self._offset = datetime.now() - new_time
        return self._offset

    def uptime(self):
        """
        Returns the uptime as a timedelta since the system was started.
        """
        return datetime.now() - self._uptime_start
