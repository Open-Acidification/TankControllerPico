"""
The file to demo the stir controller device
"""

from tank_controller.devices.library import Keypad
from tank_controller.ui_state.ui_state import UIState
from tank_controller.ui_state.user_value.degas_time import DegasTime


class DemoStirControl(UIState):
    """
    The class to demo the stir controller device
    """

    def handle_key(self, key):
        """
        The function to respond to a keypad input:
            Substate 1:
                1 -> Set Motor Speed to Fast
                2 -> Set Motor Speed to Slow
                3 -> Degas
                4 -> Return to Demo Mode Menu
            Substate 2-4:
                Any -> Return to Demo Stir Control Menu
            Substate 5:
                Any -> Display Degas Timer
            D -> Return to Demo Mode Menu

        Parameters:
            key (char): the keypad input to determine which state to go to
        """
        if self.substate == 1:
            if key == Keypad.KEY_1:
                self.tank_controller.stir_controller.set_fast()
                self.substate = 2
            elif key == Keypad.KEY_2:
                self.tank_controller.stir_controller.set_slow()
                self.substate = 3
            elif key == Keypad.KEY_3:
                self._set_next_state(DegasTime(self.tank_controller, self), True)
                self.substate = 5
            elif key == Keypad.KEY_4:
                self.tank_controller.stir_controller.set_stop()
                self._set_next_state(self.previous_state, True)
        elif self.substate == 5:
            self.tank_controller.stir_controller.degas(self.tank_controller.degas_time)
            self.substate = 4

        else:
            self.tank_controller.stir_controller.set_stop()
            self.substate = 1

        if key == Keypad.KEY_D:
            self.tank_controller.stir_controller.set_stop()
            self._set_next_state(self.previous_state, True)

    def loop(self):
        """
        The function to loop through and display to the LCD screen until a new keypad input
        """
        if self.substate == 1:
            self.tank_controller.lcd.print("1: Set fast speed", line=1)
            self.tank_controller.lcd.print("2: Set slow speed", line=2)
            self.tank_controller.lcd.print("3: Degas", line=3)
            self.tank_controller.lcd.print("4: Return", line=4)

        elif self.substate == 2:
            self.tank_controller.lcd.print("Motor speed", line=1)
            self.tank_controller.lcd.print("set to fast", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("Any key to continue", line=4)

        elif self.substate == 3:
            self.tank_controller.lcd.print("Motor speed", line=1)
            self.tank_controller.lcd.print("set to slow", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("Any key to continue", line=4)

        elif self.substate == 4:
            self.tank_controller.lcd.print("Degassing solution", line=1)
            self.tank_controller.lcd.print("Time remaining:", line=2)
            self.tank_controller.lcd.print(
                self.tank_controller.stir_controller.get_timer(), line=3
            )
            self.tank_controller.lcd.print("Any key to continue", line=4)

        elif self.substate == 5:
            self.tank_controller.lcd.print("", line=1)
            self.tank_controller.lcd.print("Any key to begin", line=2)
            self.tank_controller.lcd.print("degassing solution", line=3)
            self.tank_controller.lcd.print("", line=4)
