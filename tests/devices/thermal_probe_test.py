"""
The file to test the ThermalProbe class
"""

from unittest.mock import Mock, patch

from src.devices.thermal_probe import ThermalProbe


def test_get_and_set_thermal_correction():
    """
    The function to test the creation of a ThermalProbe
    """
    mock_eeprom = Mock()
    thermal_probe = ThermalProbe(mock_eeprom)
    thermal_probe._correction = 1.1
    assert thermal_probe.get_thermal_correction() == 1.1

    thermal_probe.set_thermal_correction(2.2)
    assert thermal_probe.get_thermal_correction() == 2.2


def test_clear_thermal_correction():
    """
    Test clearing the thermal correction value.
    """
    mock_eeprom = Mock()
    thermal_probe = ThermalProbe(mock_eeprom)
    thermal_probe.set_thermal_correction(5.0)
    assert thermal_probe.get_thermal_correction() == 5.0

    thermal_probe.clear_thermal_correction()
    assert thermal_probe.get_thermal_correction() == 0.0


@patch("src.devices.thermal_probe.ThermalProbe.get_raw_temperature", return_value=30.0)
def test_get_uncorrected_running_average(_mock_get_raw_temperature):
    """
    Test calculating the uncorrected running average.
    """
    mock_eeprom = Mock()
    thermal_probe = ThermalProbe(mock_eeprom)

    # Simulate multiple readings
    for _ in range(thermal_probe.HISTORY_SIZE):
        thermal_probe.get_uncorrected_running_average()

    # The running average should equal the raw temperature since all values are the same
    assert thermal_probe.get_uncorrected_running_average() == 30.0


@patch("time.time", side_effect=[0, 1, 2, 3, 4])  # Simulate time in seconds
@patch(
    "src.devices.thermal_probe.ThermalProbe.get_raw_temperature",
    side_effect=[25.0, 30.0, 35.0, 35.0, 35.0],
)
def test_get_running_average(_mock_get_raw_temperature, _mock_time):
    """
    Test calculating the corrected running average.
    """
    mock_eeprom = Mock()
    thermal_probe = ThermalProbe(mock_eeprom)
    thermal_probe.set_thermal_correction(5.0)

    # Simulate multiple readings
    thermal_probe.get_uncorrected_running_average()  # First reading: 25.0
    thermal_probe.get_uncorrected_running_average()  # Second reading: 30.0
    thermal_probe.get_uncorrected_running_average()  # Third reading: 35.0

    # The running average should be the average of [25.0, 30.0, 35.0] + correction
    expected_average = (25.0 + 30.0 + 35.0) / 3 + 5.0
    assert thermal_probe.get_running_average() == expected_average
