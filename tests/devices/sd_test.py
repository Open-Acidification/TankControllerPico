"""
The file to test the SD class
"""

from datetime import datetime

from titration.devices.sd import SD


def test_sd_todays_data_file_name():
    """
    The function to test the default google_sheet_interval value
    """
    sd_device = SD()
    file_name = sd_device.todays_data_file_name()

    now = datetime.now()
    expected = f"{now.year:04d}{now.month:02d}{now.day:02d}.csv"
    assert file_name == expected
