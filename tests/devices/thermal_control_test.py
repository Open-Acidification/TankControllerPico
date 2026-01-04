"""
The file to test the PH Control class
"""

from unittest.mock import Mock

from src.devices.thermal_control import ThermalControl


def test_default_heat_value():
    """
    The function to test the default heat value
    """
    mock_titrator = Mock()
    thermal_control = ThermalControl(mock_titrator)
    assert thermal_control.get_heat(False) is True


def test_save_heat_value():
    """
    The function to test setting the heat value
    """
    mock_titrator = Mock()
    thermal_control = ThermalControl(mock_titrator)
    thermal_control._heat = False
    assert thermal_control.get_heat(True) is False


def test_set_heat():
    """
    The function to test setting the heat via setter
    """
    mock_titrator = Mock()
    thermal_control = ThermalControl(mock_titrator)
    thermal_control.set_heat(False)
    assert thermal_control.get_heat(True) is False


def test_get_and_set_base_thermal_target():
    """
    Test getting and setting the base thermal target value.
    """
    mock_titrator = Mock()
    thermal_control = ThermalControl(mock_titrator)
    thermal_control.set_base_thermal_target(75.0)
    assert thermal_control.get_base_thermal_target() == 75.0


def test_get_and_set_current_thermal_target():
    """
    Test getting and setting the current thermal target value.
    """
    mock_titrator = Mock()
    thermal_control = ThermalControl(mock_titrator)
    thermal_control.set_current_thermal_target(68.5)
    assert thermal_control.get_current_thermal_target() == 68.5


def test_get_and_set_thermal_function_type():
    """
    Test getting and setting the thermal function type.
    """
    mock_titrator = Mock()
    thermal_control = ThermalControl(mock_titrator)

    assert thermal_control.get_thermal_function_type() == ThermalControl.FLAT_TYPE

    thermal_control.set_thermal_function_type(ThermalControl.RAMP_TYPE)
    assert thermal_control.get_thermal_function_type() == ThermalControl.RAMP_TYPE

    try:
        thermal_control.set_thermal_function_type(99)
    except ValueError as err:
        assert str(err) == "Invalid thermal function type"


def test_set_ramp_duration_hours():
    """
    Test setting the ramp duration in hours.
    """
    mock_titrator = Mock()
    mock_titrator.thermal_probe.get_running_average = Mock(return_value=70.0)
    thermal_control = ThermalControl(mock_titrator)

    thermal_control.set_ramp_duration_hours(3.0)
    assert thermal_control.get_ramp_time_start() > 0
    assert thermal_control.get_ramp_time_end() > thermal_control.get_ramp_time_start()
    assert thermal_control.get_thermal_function_type() == ThermalControl.RAMP_TYPE

    thermal_control.set_ramp_duration_hours(0)
    assert thermal_control.get_ramp_time_end() == 0
    assert thermal_control.get_thermal_function_type() == ThermalControl.FLAT_TYPE
