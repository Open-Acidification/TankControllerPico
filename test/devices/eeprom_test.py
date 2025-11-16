"""
The file to test the EEPROM class
"""

from titration.devices.eeprom import EEPROM


def test_default_google_sheet_interval_value():
    """
    The function to test the default google_sheet_interval value
    """
    eeprom = EEPROM()
    assert eeprom.google_sheet_interval == 20


def test_set_google_sheet_interval_value():
    """
    The function to test setting the google_sheet_interval value
    """
    eeprom = EEPROM()
    eeprom.google_sheet_interval = 45
    assert eeprom.google_sheet_interval == 45


def test_default_thermal_correction_value():
    """
    The function to test the default thermal_correction_address value
    """
    eeprom = EEPROM()
    assert eeprom.thermal_correction == 12


def test_set_thermal_correction_value():
    """
    The function to test setting the thermal_correction_address value
    """
    eeprom = EEPROM()
    eeprom.thermal_correction = 2.5
    assert eeprom.thermal_correction == 2.5
