"""
The file to configure mock objects
"""

# pylint: disable=unused-import, ungrouped-imports, wrong-import-position
# mypy: ignore-errors

from tank_controller import mock_config

if mock_config.MOCK_ENABLED:
    from tank_controller.devices import ads_mock as ADS
    from tank_controller.devices import analog_mock as analog_in
    from tank_controller.devices import board_mock as board
    from tank_controller.devices import i2c_mock as busio
    from tank_controller.devices import pwm_out_mock as pwmio
    from tank_controller.devices.digital_mock import DigitalInOut
    from tank_controller.devices.heater_mock import Heater
    from tank_controller.devices.keypad_mock import Keypad
    from tank_controller.devices.liquid_crystal_mock import LiquidCrystal
    from tank_controller.devices.max31865_mock import MAX31865
    from tank_controller.devices.serial_mock import Serial
    from tank_controller.devices.spi_mock import SPI
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

    from tank_controller.devices.keypad import Keypad
    from tank_controller.devices.liquid_crystal import LiquidCrystal

from tank_controller.devices.ph_probe import PHProbe
from tank_controller.devices.stir_control import StirControl
from tank_controller.devices.syringe_pump import SyringePump
from tank_controller.devices.temperature_control import TemperatureControl
from tank_controller.devices.temperature_probe import TemperatureProbe
