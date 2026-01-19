"""
The file to configure mock objects
"""

# pylint: disable=unused-import, ungrouped-imports, wrong-import-position
# mypy: ignore-errors
# ruff: noqa: F401

from src import mock_config

if mock_config.MOCK_ENABLED:
    from src.devices import ads_mock as ADS
    from src.devices import analog_mock as analog_in
    from src.devices import board_mock as board
    from src.devices import i2c_mock as busio
    from src.devices import pwm_out_mock as pwmio
    from src.devices.digital_mock import DigitalInOut
    from src.devices.heater_mock import Heater
    from src.devices.keypad_mock import Keypad
    from src.devices.liquid_crystal_mock import LiquidCrystal
    from src.devices.max31865_mock import MAX31865
    from src.devices.serial_mock import Serial
    from src.devices.spi_mock import SPI
else:
    import adafruit_ads1x15.ads1115 as ADS
    import board
    import busio
    import pwmio
    from adafruit_ads1x15 import analog_in
    from adafruit_max31865 import MAX31865
    from busio import SPI
    from digitalio import DigitalInOut
    from gpiozero import LED as Heater
    from serial import Serial

    from src.devices.keypad import Keypad
    from src.devices.liquid_crystal import LiquidCrystal

from src.devices.ph_probe import PHProbe
from src.devices.stir_control import StirControl
from src.devices.syringe_pump import SyringePump
from src.devices.temperature_control import TemperatureControl
from src.devices.temperature_probe import TemperatureProbe
