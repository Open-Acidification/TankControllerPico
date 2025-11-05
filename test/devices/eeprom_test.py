"""
The file to test the EEPROM class
"""

from titration.devices.eeprom import EEPROM


def test_default_google_sheet_interval_value():
    """
    The function to test the default google_sheet_interval value
    """
    eeprom = EEPROM()
    assert eeprom.google_sheet_interval == 108


def test_set_google_sheet_interval_value():
    """
    The function to test setting the google_sheet_interval value
    """
    eeprom = EEPROM()
    eeprom.google_sheet_interval = 45
    assert eeprom.google_sheet_interval == 45


def test_pid_addresses():
    """
    The function to test the PID address values
    """
    eeprom = EEPROM()
    assert eeprom.kp_address == 20
    assert eeprom.ki_address == 28
    assert eeprom.kd_address == 36


def test_set_pid_addresses():
    """
    The function to test setting the PID address values
    """
    eeprom = EEPROM()
    eeprom.kp_address = 25
    eeprom.ki_address = 30
    eeprom.kd_address = 40
    assert eeprom.kp_address == 25
    assert eeprom.ki_address == 30
    assert eeprom.kd_address == 40
