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

    def __init__(self):
        """The constructor for the mock SD class."""
        self.most_recent_data_log_header = ""
        self.most_recent_data_log_line = ""

    def todays_data_file_name(self) -> str:
        """Return today's data filename as YYYYMMDD.csv"""
        now = datetime.now()
        return f"{now.year:04d}{now.month:02d}{now.day:02d}.csv"

    def write_to_data_log(self, header: str, line: str) -> None:
        """Create today's data file (or append) and write header + line.
        """
        self.most_recent_data_log_header = str(header)[:128]
        self.most_recent_data_log_line = str(line)[:128]
        fname = self.todays_data_file_name()
        p = self.data_logs / fname

        if not p.exists():
            with p.open("w", encoding="utf-8") as f:
                if header:
                    f.write(header + "\n")
        with p.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
