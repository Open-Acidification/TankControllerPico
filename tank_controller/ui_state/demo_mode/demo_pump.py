"""
The file to demo the pump device
"""

from tank_controller.devices.library import Keypad
from tank_controller.ui_state.ui_state import UIState
from tank_controller.ui_state.user_value.pump_volume import PumpVolume
from tank_controller.ui_state.user_value.volume_to_move import VolumeToMove


class DemoPump(UIState):
    """
    The class to demo the pump
    """

    def handle_key(self, key):
        """
        The function to handle keypad input:
            Substate 1:
                1 -> Get Volume
                2 -> Set Volume
                3 -> Pull Volume in to Pump
                4 -> Go to 2nd page of options
            Substate 2:
                1 -> Pump Volume out into Solution
                4 -> Go to 1st page of options
            Substate 3:
                Any -> Substate 1
            Substate 4:
                Any -> Substate 1
            D -> Return to Demo Mode Menu

        Parameters:
            key (char): the keypad input is used to move through the substates
        """
        if self.substate == 1:
            if key == Keypad.KEY_1:
                self.substate = 3

            elif key == Keypad.KEY_2:
                self._set_next_state(PumpVolume(self.tank_controller, self), True)
                self.substate = 3

            elif key == Keypad.KEY_3:
                self._set_next_state(VolumeToMove(self.tank_controller, self), True)
                self.tank_controller.pump.pull_volume_in(
                    self.tank_controller.volume_to_move
                )
                self.tank_controller.volume_to_move = 0
                self.substate = 3

            elif key == Keypad.KEY_4:
                self.substate = 2

        elif self.substate == 2:
            if key == Keypad.KEY_1:
                self._set_next_state(VolumeToMove(self.tank_controller, self), True)
                self.tank_controller.pump.push_volume_out(
                    self.tank_controller.volume_to_move
                )
                self.tank_controller.volume_to_move = 0
                self.substate = 3

            elif key == Keypad.KEY_4:
                self.substate = 1

        elif self.substate == 3:
            self.substate = 1

        if key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)

    def loop(self):
        """
        The function to loop through and display to the LCD screen until a new keypad input
        """
        if self.substate == 1:
            self.tank_controller.lcd.print("1: Get volume", line=1)
            self.tank_controller.lcd.print("2: Set volume", line=2)
            self.tank_controller.lcd.print("3: Pull volume in", line=3)
            self.tank_controller.lcd.print("4: Page 2", line=4)

        elif self.substate == 2:
            self.tank_controller.lcd.print("1: Push volume out", line=1)
            self.tank_controller.lcd.print("", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("4: Page 1", line=4)

        elif self.substate == 3:
            self.tank_controller.lcd.print("Pump volume:", line=1)
            self.tank_controller.lcd.print(
                f"{self.tank_controller.pump.get_volume_in_pump()} ml",
                line=2,
                style="center",
            )
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("Any key to continue", line=4)
