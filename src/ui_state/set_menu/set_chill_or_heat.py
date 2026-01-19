"""
The file to hold the Set Chill or Heat class
"""

from src.devices.library import Keypad
from src.ui_state.ui_state import UIState


class SetChillOrHeat(UIState):
    """
    This is a class for the SetChillOrHeat state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state

    def loop(self):
        """
        The main loop for the SetChillOrHeat state
        """
        self.titrator.lcd.print("1:Chill; 9:Heat", line=1)

        if self.titrator.thermal_control.get_heat(True):
            self.titrator.lcd.print("Currently: Heat", line=2)
        else:
            self.titrator.lcd.print("Currently: Chill", line=2)

    def handle_key(self, key):
        """
        Handle key presses to return to the previous state.
        """
        if key == Keypad.KEY_1:
            self.titrator.thermal_control.set_heat(False)
            self.titrator.lcd.print("Use chiller", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_9:
            self.titrator.thermal_control.set_heat(True)
            self.titrator.lcd.print("Use heater", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_A:
            if self.titrator.thermal_control.get_heat(True):
                self.titrator.lcd.print("Use heater", line=2)
            else:
                self.titrator.lcd.print("Use chiller", line=2)
            self.return_to_main_menu(ms_delay=3000)

        if key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)
