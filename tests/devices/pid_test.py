"""
The file to test the View PID Constants class
"""

from unittest import mock

from src.devices.eeprom import EEPROM
from src.devices.pid import PID


def test_pid_reads_values_from_eeprom():
    """
    PID should read kp/ki/kd from EEPROM on construction.
    """
    eeprom = EEPROM()
    eeprom._kp_value = 1.1
    eeprom._ki_value = 2.2
    eeprom._kd_value = 3.3

    with mock.patch("src.devices.eeprom.EEPROM", return_value=eeprom):
        pid = PID(eeprom)
        assert pid.kp_value == 1.1
        assert pid.ki_value == 2.2
        assert pid.kd_value == 3.3


def test_pid_defaults_from_none():
    """
    PID should read kp/ki/kd from EEPROM on construction.
    """
    eeprom = EEPROM()
    eeprom._kp_value = None
    eeprom._ki_value = None
    eeprom._kd_value = None

    with mock.patch("src.devices.eeprom.EEPROM", return_value=eeprom):
        pid = PID(eeprom)
        assert pid.kp_value == 100000.0
        assert pid.ki_value == 0.0
        assert pid.kd_value == 0.0


def test_pid_reflects_eeprom_changes():
    """
    PID properties should reflect current EEPROM values on each access.
    """
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.get_kp.return_value = 100000.0
    mock_eeprom.get_ki.return_value = 0.0
    mock_eeprom.get_kd.return_value = 0.0

    pid = PID(mock_eeprom)
    assert pid.kp_value == 100000.0
    assert pid.ki_value == 0.0
    assert pid.kd_value == 0.0

    mock_eeprom.get_kp.return_value = 200000.0
    mock_eeprom.get_ki.return_value = 50.0
    mock_eeprom.get_kd.return_value = 25.0
    assert pid.kp_value == 200000.0
    assert pid.ki_value == 50.0
    assert pid.kd_value == 25.0
