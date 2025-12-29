"""
The file to test the EEPROM class
"""

from src.devices.eeprom import EEPROM


def test_default_google_sheet_interval_value():
    """
    The function to test the default google_sheet_interval value
    """
    eeprom = EEPROM()
    assert eeprom.get_google_sheet_interval(65535) == 20


def test_save_google_sheet_interval_value():
    """
    The function to test setting the google_sheet_interval value
    """
    eeprom = EEPROM()
    eeprom._google_sheet_interval = 45
    assert eeprom.get_google_sheet_interval(65535) == 45


def test_set_google_sheet_interval():
    """
    The function to test setting the google_sheet_interval via setter
    """
    eeprom = EEPROM()
    eeprom.set_google_sheet_interval(60)
    assert eeprom.get_google_sheet_interval(65535) == 60


def test_default_heat_value():
    """
    The function to test the default heat value
    """
    eeprom = EEPROM()
    assert eeprom.get_heat(False) is True


def test_save_heat_value():
    """
    The function to test setting the heat value
    """
    eeprom = EEPROM()
    eeprom._heat = False
    assert eeprom.get_heat(True) is False


def test_set_heat():
    """
    The function to test setting the heat via setter
    """
    eeprom = EEPROM()
    eeprom.set_heat(False)
    assert eeprom.get_heat(True) is False


def test_default_ignore_bad_ph_slope_value():
    """
    The function to test the default ignore_bad_ph_slope value
    """
    eeprom = EEPROM()
    assert eeprom.get_ignore_bad_ph_slope(True) is False


def test_save_ignore_bad_ph_slope_value():
    """
    The function to test setting the ignore_bad_ph_slope value
    """
    eeprom = EEPROM()
    eeprom._ignore_bad_ph_slope = True
    assert eeprom.get_ignore_bad_ph_slope(False) is True


def test_set_ignore_bad_ph_slope():
    """
    The function to test setting the ignore_bad_ph_slope via setter
    """
    eeprom = EEPROM()
    eeprom.set_ignore_bad_ph_slope(True)
    assert eeprom.get_ignore_bad_ph_slope(False) is True


def test_pid_values():
    """
    The function to test the PID values
    """
    eeprom = EEPROM()
    assert eeprom.get_kp(100000.0) == 20.0
    assert eeprom.get_ki(0.0) == 28.0
    assert eeprom.get_kd(0.0) == 36.0


def test_save_pid_values():
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


def test_set_pid_values():
    """
    The function to test setting the PID values via setters
    """
    eeprom = EEPROM()
    eeprom.set_kp(22.0)
    eeprom.set_ki(29.0)
    eeprom.set_kd(35.0)
    assert eeprom.get_kp(100000.0) == 22.0
    assert eeprom.get_ki(0.0) == 29.0
    assert eeprom.get_kd(0.0) == 35.0


def test_tank_id_value():
    """
    The function to test the default tank_id value
    """
    eeprom = EEPROM()
    assert eeprom.get_tank_id(0) == 1


def test_save_tank_id_value():
    """
    The function to test setting the tank_id value
    """
    eeprom = EEPROM()
    eeprom._tank_id = 5
    assert eeprom.get_tank_id(0) == 5


def test_set_tank_id():
    """
    The function to test setting the tank_id via setter
    """
    eeprom = EEPROM()
    eeprom.set_tank_id(10)
    assert eeprom.get_tank_id(0) == 10


def test_thermal_correction_value():
    """
    The function to test the default thermal_correction_address value
    """
    eeprom = EEPROM()
    assert eeprom.get_thermal_correction(0.0) == 12


def test_save_thermal_correction_value():
    """
    The function to test setting the thermal_correction_address value
    """
    eeprom = EEPROM()
    eeprom._thermal_correction = 2.5
    assert eeprom.get_thermal_correction(0.0) == 2.5
