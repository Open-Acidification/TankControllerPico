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


def test_pid_values():
    """
    The function to test the PID values
    """
    eeprom = EEPROM()
    assert eeprom.get_kp() == 20.0
    assert eeprom.get_ki() == 28.0
    assert eeprom.get_kd() == 36.0


def test_set_pid_values():
    """
    The function to test setting the PID values
    """
    eeprom = EEPROM()
    eeprom.kp_value = 25.0
    eeprom.ki_value = 30.0
    eeprom.kd_value = 40.0
    assert eeprom.get_kp() == 25.0
    assert eeprom.get_ki() == 30.0
    assert eeprom.get_kd() == 40.0
