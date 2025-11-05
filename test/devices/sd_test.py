"""
The file to test the SD class
"""

from titration.devices.sd import SD


def test_sd_todays_data_file_name():
    """
    The function to test the default google_sheet_interval value
    """
    sd = SD()
    file_name = sd.todays_data_file_name()
    assert file_name.startswith("2025")
    assert file_name.endswith(".csv")
