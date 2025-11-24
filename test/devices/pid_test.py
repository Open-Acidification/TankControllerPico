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
    mock_eeprom = EEPROM()
    mock_eeprom._kp_value = 1.1
    mock_eeprom._ki_value = 2.2
    mock_eeprom._kd_value = 3.3

    with mock.patch("titration.devices.eeprom.EEPROM", return_value=mock_eeprom):
        pid = PID(mock_eeprom)
        assert pid.kp_value == 1.1
        assert pid.ki_value == 2.2
        assert pid.kd_value == 3.3


def test_pid_defaults():
    """
    PID should read kp/ki/kd from EEPROM on construction.
    """
    eeprom = EEPROM()
    eeprom._kp_value = None
    eeprom._ki_value = None
    eeprom._kd_value = None

    with mock.patch("titration.devices.eeprom.EEPROM", return_value=eeprom):
        pid = PID(eeprom)
        assert pid.kp_value == 100000.0
        assert pid.ki_value == 0.0
        assert pid.kd_value == 0.0
