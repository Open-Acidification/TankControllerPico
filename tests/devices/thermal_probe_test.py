"""
The file to test the ThermalProbe class
"""

from unittest import mock

from src.devices.eeprom import EEPROM
from src.devices.thermal_probe import ThermalProbe


def test_create_thermal_probe():
    """
    The function to test the creation of a ThermalProbe
    """
    thermal_probe = ThermalProbe()

    assert thermal_probe.correction == 12.0


def test_create_thermal_probe_reads_numeric_float():
    """ThermalProbe should read a numeric float from EEPROM."""
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.thermal_correction = 1

    with mock.patch("src.devices.thermal_probe.EEPROM", return_value=mock_eeprom):
        thermal_probe = ThermalProbe()

    assert thermal_probe.correction == 1.0
