"""
The file to test the ThermalProbe class
"""

from unittest import mock

from src.devices.eeprom import EEPROM
from src.devices.thermal_probe import ThermalProbe


def test_thermal_probe_reads_values_from_eeprom():
    """
    The function to test the creation of a ThermalProbe
    """
    eeprom = EEPROM()
    eeprom._thermal_correction = 1.1
    with mock.patch("src.devices.eeprom.EEPROM", return_value=eeprom):
        thermal_probe = ThermalProbe(eeprom)

    assert thermal_probe.correction == 1.1


def test_thermal_probe_defaults_from_none():
    """ThermalProbe should read a numeric float from EEPROM."""
    eeprom = EEPROM()
    eeprom._thermal_correction = None

    with mock.patch("src.devices.eeprom.EEPROM", return_value=eeprom):
        thermal_probe = ThermalProbe(eeprom)

    assert thermal_probe.correction == 0.0
