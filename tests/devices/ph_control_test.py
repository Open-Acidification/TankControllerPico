"""
The file to test the PH Control class
"""

from unittest.mock import Mock

from src.devices.ph_control import PHControl


def test_uses_pid_kby_default():
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


def test_get_and_set_base_target_ph():
    """
    Test getting and setting the base target pH value.
    """
    mock_titrator = Mock()
    ph_control = PHControl(mock_titrator)
    ph_control._base_target_ph = 1.125

    assert ph_control.get_base_target_ph() == 1.125

    ph_control.set_base_target_ph(7.5)
    assert ph_control.get_base_target_ph() == 7.5


def test_get_and_set_current_target_ph():
    """
    Test getting and setting the current target pH value.
    """
    mock_titrator = Mock()
    ph_control = PHControl(mock_titrator)
    ph_control._current_target_ph = 2.2

    assert ph_control.get_current_target_ph() == 2.2

    ph_control.set_current_target_ph(6.8)
    assert ph_control.get_current_target_ph() == 6.8


def test_get_and_set_ph_function_type():
    """
    Test getting and setting the pH function type.
    """
    mock_titrator = Mock()
    ph_control = PHControl(mock_titrator)

    assert ph_control.get_ph_function_type() == PHControl.FLAT_TYPE

    ph_control.set_ph_function_type(PHControl.RAMP_TYPE)
    assert ph_control.get_ph_function_type() == PHControl.RAMP_TYPE

    ph_control.set_ph_function_type(PHControl.SINE_TYPE)
    assert ph_control.get_ph_function_type() == PHControl.SINE_TYPE

    try:
        ph_control.set_ph_function_type(99)
    except ValueError as e:
        assert str(e) == "Invalid pH function type"


def test_set_ramp_duration_hours():
    """
    Test setting the ramp duration in hours.
    """
    mock_titrator = Mock()
    mock_titrator.ph_probe.get_ph_value = Mock(return_value=7.2)
    ph_control = PHControl(mock_titrator)

    ph_control.set_ramp_duration_hours(2.5)
    assert ph_control.get_ramp_time_start() > 0
    assert ph_control.get_ramp_time_end() > ph_control.get_ramp_time_start()
    assert ph_control.get_ph_function_type() == PHControl.RAMP_TYPE

    ph_control.set_ramp_duration_hours(0)
    assert ph_control.get_ramp_time_end() == 0
    assert ph_control.get_ph_function_type() == PHControl.FLAT_TYPE


def test_set_sine_amplitude_and_hours():
    """
    Test setting the sine amplitude and period in hours.
    """
    mock_titrator = Mock()
    ph_control = PHControl(mock_titrator)

    ph_control.set_sine_amplitude_and_hours(1.5, 4)
    assert ph_control.get_amplitude() == 1.5
    assert ph_control.get_period_in_seconds() == 14400  # 4 hours in seconds
    assert ph_control.get_ph_function_type() == PHControl.SINE_TYPE

    try:
        ph_control.set_sine_amplitude_and_hours(-1, 4)
    except ValueError as e:
        assert str(e) == "Amp and period !> than 0."
