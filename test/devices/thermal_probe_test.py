"""
The file to test the ThermalProbe class
"""

from types import SimpleNamespace
from unittest import mock

from titration.devices.thermal_probe import ThermalProbe


def test_create_thermal_probe():
    """
    The function to test the creation of a ThermalProbe
    """
    thermal_probe = ThermalProbe()

    assert thermal_probe.correction == 12.0


def test_create_thermal_probe_with_nan_correction():
    """The function to test ThermalProbe defaults to 0.0 when EEPROM value is invalid."""
    with mock.patch(
        "titration.devices.thermal_probe.EEPROM",
        return_value=SimpleNamespace(thermal_correction_address="invalid"),
    ):
        thermal_probe = ThermalProbe()
        assert thermal_probe.correction == 0.0


def test_create_thermal_probe_with_none_correction():
    """The function to test ThermalProbe defaults to 0.0 when EEPROM value is None."""
    with mock.patch(
        "titration.devices.thermal_probe.EEPROM",
        return_value=SimpleNamespace(thermal_correction_address=None),
    ):
        thermal_probe = ThermalProbe()
        assert thermal_probe.correction == 0.0
