"""
This module provides a Python implementation of the SD card helper used in
the embedded firmware.
"""

from datetime import datetime


class SD:
    """Simple SD-card-like helper for host tests and emulation.

    It stores files under a storage directory next to this module by
    default (./sd_storage). This keeps test artifacts isolated and easy to
    inspect or remove.
    """

    def todays_data_file_name(self) -> str:
        """Return today's data filename as YYYYMMDD.csv"""
        now = datetime.now()
        return f"{now.year:04d}{now.month:02d}{now.day:02d}.csv"
