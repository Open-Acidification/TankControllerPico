"""
The file to test the PHProbe mock class
"""

from unittest.mock import Mock

from src.devices.ph_probe_mock import PHProbe


def test_get_and_set_ph_value():
    """
    Test getting and setting the pH value.
    """
    mock_eeprom = Mock()
    ph_probe = PHProbe(mock_eeprom)
    ph_probe._value = 3.125
    assert ph_probe.get_ph_value() == 3.125

    ph_probe.set_ph_value(7.5)
    assert ph_probe.get_ph_value() == 7.5


def test_get_calibration():
    """
    Test getting the calibration response string.
    """
    mock_eeprom = Mock()
    ph_probe = PHProbe(mock_eeprom)
    ph_probe._calibration_response = "?CAL,3"

    assert ph_probe.get_calibration() == "?CAL,3"


def test_clear_calibration():
    """
    Test clearing the calibration response string.
    """
    mock_eeprom = Mock()
    ph_probe = PHProbe(mock_eeprom)

    ph_probe.slope_is_out_of_range = True
    mock_eeprom.set_ignore_bad_ph_slope = Mock()

    ph_probe.clear_calibration()

    assert ph_probe.slope_is_out_of_range is False
    mock_eeprom.set_ignore_bad_ph_slope.assert_called_once_with(False)
    assert ph_probe.get_calibration() == ""


def test_get_slope():
    """
    Test getting the slope response string.
    """
    mock_eeprom = Mock()
    ph_probe = PHProbe(mock_eeprom)
    ph_probe._slope_response = "99.7,100.3, -0.89"

    assert ph_probe.get_slope() == "99.7,100.3, -0.89"


def test_should_warn_about_calibration():
    """
    Test determining if a calibration warning should be shown.
    """
    mock_eeprom = Mock()
    ph_probe = PHProbe(mock_eeprom)

    ph_probe.slope_is_out_of_range = False
    assert ph_probe.should_warn_about_calibration() is False

    ph_probe.slope_is_out_of_range = True
    mock_eeprom.get_ignore_bad_ph_slope = Mock(return_value=False)
    assert ph_probe.should_warn_about_calibration() is True

    mock_eeprom.get_ignore_bad_ph_slope = Mock(return_value=True)
    assert ph_probe.should_warn_about_calibration() is False
