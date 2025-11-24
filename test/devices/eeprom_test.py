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


def test_pid_values():
    """
    The function to test the PID values
    """
    eeprom = EEPROM()
    assert eeprom.get_kp(100000.0) == 20.0
    assert eeprom.get_ki(0.0) == 28.0
    assert eeprom.get_kd(0.0) == 36.0


def test_set_pid_values():
    """
    The function to test setting the PID values
    """
    eeprom = EEPROM()
    eeprom._kp_value = 25.0
    eeprom._ki_value = 30.0
    eeprom._kd_value = 40.0
    assert eeprom.get_kp(100000.0) == 25.0
    assert eeprom.get_ki(0.0) == 30.0
    assert eeprom.get_kd(0.0) == 40.0


def test_thermal_correction_value():
    """
    The function to test the default thermal_correction_address value
    """
    eeprom = EEPROM()
    assert eeprom.get_thermal_correction(0.0) == 12


def test_set_thermal_correction_value():
    """
    The function to test setting the thermal_correction_address value
    """
    eeprom = EEPROM()
    eeprom._thermal_correction = 2.5
    assert eeprom.get_thermal_correction(0.0) == 2.5


def test_default_tank_id_value():
    """
    The function to test the default tank_id value
    """
    eeprom = EEPROM()
    assert eeprom.tank_id == 0


def test_set_tank_id_value():
    """
    The function to test setting the tank_id value
    """
    eeprom = EEPROM()
    eeprom.tank_id = 15
    assert eeprom.tank_id == 15
