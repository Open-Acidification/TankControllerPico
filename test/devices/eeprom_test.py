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


def test_default_tank_id_value():
    """
    The function to test the default tank_id value
    """
    eeprom = EEPROM()
    assert eeprom.tank_id_address == 8


def test_set_tank_id_value():
    """
    The function to test setting the tank_id value
    """
    eeprom = EEPROM()
    eeprom.tank_id_address = 15
    assert eeprom.tank_id_address == 15
