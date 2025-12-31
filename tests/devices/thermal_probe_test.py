"""
The file to test the ThermalProbe class
"""

from unittest.mock import Mock

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
