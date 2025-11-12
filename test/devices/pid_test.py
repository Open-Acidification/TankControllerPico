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


def test_pid_uses_defaults_when_eeprom_has_nan():
    """
    If EEPROM returns NaN for tunings, PID should replace with defaults.
    """
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.get_kp.return_value = float("nan")
    mock_eeprom.get_ki.return_value = float("nan")
    mock_eeprom.get_kd.return_value = float("nan")

    with mock.patch("titration.devices.pid.EEPROM", return_value=mock_eeprom):
        pid = PID()
        assert pid.kp_value == 100000.0
        assert pid.ki_value == 0.0
        assert pid.kd_value == 0.0


def test_pid_uses_defaults_when_eeprom_is_none():
    """If EEPROM returns None for tunings, PID should replace with defaults."""
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.get_kp.return_value = None
    mock_eeprom.get_ki.return_value = None
    mock_eeprom.get_kd.return_value = None

    with mock.patch("titration.devices.pid.EEPROM", return_value=mock_eeprom):
        pid = PID()
        assert pid.kp_value == 100000.0
        assert pid.ki_value == 0.0
        assert pid.kd_value == 0.0
