"""
The file to test the SetLED class
"""

from src.devices.library import Keypad
from src.titrator import Titrator
from src.ui_state.set_menu.set_led import SetLED


def test_led_on():
    """Test turning the LED on."""
    titrator = Titrator()
    state = SetLED(titrator)

    state.handle_key(Keypad.KEY_1)

    assert titrator.led.is_on is True


def test_led_off():
    """Test turning the LED off."""
    titrator = Titrator()
    state = SetLED(titrator)

    titrator.led.on()
    state.handle_key(Keypad.KEY_9)

    assert titrator.led.is_on is False
    