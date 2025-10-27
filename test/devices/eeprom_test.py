"""
The file to test the EEPROM class
"""

from titration.devices.eeprom import EEPROM


def test_default_google_sheet_interval_value():
    """
    The function to test the default google_sheet_interval value
    """
    e = EEPROM()
    assert e.google_sheet_interval == 20

def test_set_google_sheet_interval_value():
    """
    The function to test setting the google_sheet_interval value
    """
    e = EEPROM()
    e.google_sheet_interval = 45
    assert e.google_sheet_interval == 45
