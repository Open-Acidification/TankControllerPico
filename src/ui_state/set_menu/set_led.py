"""
The file to hold the Set LED class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class SetLED(UIState):
    """
    This is a class for the SetLED state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The main loop for the SetLED state
        """
        self.titrator.lcd.print("LED 1:on; 9:off", line=1)

        if self.titrator.led.is_on:
            self.titrator.lcd.print("Currently on", line=2)
        else:
            self.titrator.lcd.print("Currently off", line=2)

    def handle_key(self, key):
        """
        Handle key presses to control the LED.
        """
        if key == Keypad.KEY_1:
            self.titrator.led.on()
            self.titrator.lcd.print("LED on", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_9:
            self.titrator.led.off()
            self.titrator.lcd.print("LED off", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_A:
            if self.titrator.led.is_on:
                self.titrator.lcd.print("LED on", line=2)
            else:
                self.titrator.lcd.print("LED off", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)
            