"""
The file to test the PH Control class
"""

from src.devices.ph_control import PHControl
from unittest.mock import Mock


def test_uses_pid_by_default():
    """
    The function to test the default google_sheet_interval value
    """
    mock_titrator = Mock()
    phcontrol = PHControl(mock_titrator)
    assert phcontrol.use_pid is True


def test_set_use_pid_value():
    """
    The function to test setting the use_pid value
    """
    mock_titrator = Mock()
    phcontrol = PHControl(mock_titrator)
    phcontrol.use_pid = False
    assert phcontrol.use_pid is False
