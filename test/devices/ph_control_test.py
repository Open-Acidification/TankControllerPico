"""
The file to test the PH Control class
"""

from titration.devices.ph_control import PHControl


def test_uses_pid_by_default():
    """
    The function to test the default google_sheet_interval value
    """
    phcontrol = PHControl()
    assert phcontrol.use_pid is True


def test_set_use_pid_value():
    """
    The function to test setting the use_pid value
    """
    phcontrol = PHControl()
    phcontrol.use_pid = False
    assert phcontrol.use_pid is False
