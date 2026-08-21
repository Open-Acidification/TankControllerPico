"""
The file to test the Mock LED class.
"""

from src.devices.led_mock import LED


def test_led_starts_off():
    """
    LED should be off when initialized.
    """
    led = LED()

    assert led.is_on is False


def test_led_turns_on():
    """
    LED should turn on when on() is called.
    """
    led = LED()

    led.on()

    assert led.is_on is True


def test_led_turns_off():
    """
    LED should turn off when off() is called.
    """
    led = LED()
    led.on()

    led.off()

    assert led.is_on is False


def test_led_toggle():
    """
    LED should switch between on and off when toggle() is called.
    """
    led = LED()

    led.toggle()
    assert led.is_on is True

    led.toggle()
    assert led.is_on is False
