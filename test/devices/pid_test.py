"""
The file to test the View PID Constants class
"""
from types import SimpleNamespace
from unittest import mock

from titration.devices.pid import PID


def test_pid_reads_values_from_eeprom():
    """PID should read kp/ki/kd from EEPROM on construction."""
    mock_eeprom = SimpleNamespace(kp_address=1.1, ki_address=2.2, kd_address=3.3)

    with mock.patch("titration.devices.pid.EEPROM", return_value=mock_eeprom):
        pid = PID()
        assert pid.kp == 1.1
        assert pid.ki == 2.2
        assert pid.kd == 3.3
