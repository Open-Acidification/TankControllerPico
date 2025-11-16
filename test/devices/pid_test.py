"""
The file to test the View PID Constants class
"""

from unittest import mock

from titration.devices.eeprom import EEPROM
from titration.devices.pid import PID


def test_pid_reads_values_from_eeprom():
    """
    PID should read kp/ki/kd from EEPROM on construction.
    """
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.get_kp.return_value = 1.1
    mock_eeprom.get_ki.return_value = 2.2
    mock_eeprom.get_kd.return_value = 3.3

    with mock.patch("titration.devices.pid.EEPROM", return_value=mock_eeprom):
        pid = PID()
        assert pid.kp_value == 1.1
        assert pid.ki_value == 2.2
        assert pid.kd_value == 3.3


def test_get_float_various_inputs():
    """Exercise PID.get_float with callable and direct values for numeric/invalid cases."""
    pid = object.__new__(PID)  # instantiate without running __init__

    assert pid.get_float(lambda: "1.1", 0.0) == 1.1
    assert pid.get_float("2.2", 0.0) == 2.2
    assert pid.get_float(3.3, 0.0) == 3.3
    assert pid.get_float(True, 4.4) == 4.4
    assert pid.get_float(None, 5.5) == 5.5
    assert pid.get_float("invalid", 6.6) == 6.6
    assert pid.get_float(lambda: float("nan"), 7.7) == 7.7
    assert pid.get_float(lambda: float("inf"), 8.8) == 8.8
