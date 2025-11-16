"""
The file to test the ThermalProbe class
"""

from unittest import mock

from titration.devices.eeprom import EEPROM
from titration.devices.thermal_probe import ThermalProbe


def test_create_thermal_probe():
    """
    The function to test the creation of a ThermalProbe
    """
    thermal_probe = ThermalProbe()

    assert thermal_probe.correction == 12.0


def test_create_thermal_probe_reads_numeric_float():
    """ThermalProbe should read a numeric float from EEPROM."""
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.thermal_correction = 1.1

    with mock.patch("titration.devices.thermal_probe.EEPROM", return_value=mock_eeprom):
        thermal_probe = ThermalProbe()

    assert thermal_probe.correction == 1.1


def test_create_thermal_probe_reads_numeric_string():
    """ThermalProbe should convert numeric strings to float."""
    mock_eeprom = mock.Mock(spec=EEPROM)
    mock_eeprom.thermal_correction = "2.2"

    with mock.patch("titration.devices.thermal_probe.EEPROM", return_value=mock_eeprom):
        thermal_probe = ThermalProbe()

    assert thermal_probe.correction == 2.2


def test_create_thermal_probe_handles_invalid_and_none():
    """None, non-numeric strings or NaN from EEPROM -> correction defaults to 0.0"""
    for bad in (None, "not-a-number", float("nan")):
        mock_eeprom = mock.Mock(spec=EEPROM)
        mock_eeprom.thermal_correction = bad

        with mock.patch(
            "titration.devices.thermal_probe.EEPROM", return_value=mock_eeprom
        ):
            thermal_probe = ThermalProbe()

        assert thermal_probe.correction == 0.0
