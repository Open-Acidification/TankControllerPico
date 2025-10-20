"""
The file for the ManualTitration class
"""

from tank_controller.devices.library import Keypad
from tank_controller.ui_state import main_menu
from tank_controller.ui_state.ui_state import UIState
from tank_controller.ui_state.user_value.degas_time import DegasTime
from tank_controller.ui_state.user_value.volume_to_move import VolumeToMove


class ManualTitration(UIState):
    """
    This is a class for the ManualTitration state of the titrator

    Attributes:
        titrator (Titrator object): the titrator is used to move through the state machine
        previous_state (UIState object): the previous_state is used to return the last visited state
        substate (int): the substate is used to keep track of substate of the UIState
        values (dict): values is a dictionary to hold the volume, direction, degas time, and current pH
    """

    def __init__(self, titrator):
        """
        The constructor for the ManualTitration class

        Parameters:
            titrator (Titrator object): the titrator is used to move through the state machine
        """
        super().__init__(titrator)
        self.values = {
            "p_direction": 0,
            "current_pH": 5,
        }

    def handle_key(self, key):
        """
        The function to respond to a keypad input:
            Substate 1:
                Any -> Enter UserValue state to set volume
            Substate 2:
                Any -> Set p_direction
            Substate 3:
                1 -> Add more HCL
                0 -> Do not add more HCL
            Substate 4:
                1 -> Set degas
                0 -> Do not set degas
            Substate 5:
                Any -> Enter UserValue to set the degas value
            Substate 6:
                Any -> Return to main menu

        Parameters:
            key (char): the keypad input is used to move through the substates
        """
        if self.substate == 1:
            self._set_next_state(VolumeToMove(self.tank_controller, self), True)
            self.substate += 1

        elif self.substate == 2:
            self.values["p_direction"] = key
            self.substate += 1

        elif self.substate == 3:
            if key == Keypad.KEY_1:
                self.substate -= 1
            elif key == Keypad.KEY_0:
                self.substate += 1

        elif self.substate == 4:
            if key == Keypad.KEY_0:
                self.substate += 2
            elif key == Keypad.KEY_1:
                self.substate += 1

        elif self.substate == 5:
            self._set_next_state(DegasTime(self.tank_controller, self), True)
            self.substate += 1

        elif self.substate == 6:
            self._set_next_state(main_menu.MainMenu(self.tank_controller), True)

    def loop(self):
        """
        The function to loop through and display to the LCD screen until a new keypad input
        """
        if self.substate == 1:
            self.tank_controller.lcd.print("Enter volume", line=1)
            self.tank_controller.lcd.print("", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("Any key to continue", line=4)

        elif self.substate == 2:
            self.tank_controller.lcd.print("Direction (0/1):", line=1)
            self.tank_controller.lcd.print("", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("", line=4)

        elif self.substate == 3:
            self.tank_controller.lcd.print(
                f"Current pH: {self.values['current_pH']:>4.5f}", line=1
            )
            self.tank_controller.lcd.print("Add more HCl:", line=2)
            self.tank_controller.lcd.print("(0 - No, 1 - Yes)", line=3)
            self.tank_controller.lcd.print("", line=4)

        elif self.substate == 4:
            self.tank_controller.lcd.print(
                f"Current pH: {self.values['current_pH']:>4.5f}", line=1
            )
            self.tank_controller.lcd.print("Degas:", line=2)
            self.tank_controller.lcd.print("(0 - No, 1 - Yes)", line=3)
            self.tank_controller.lcd.print("", line=4)

        elif self.substate == 5:
            self.tank_controller.lcd.print("Enter degas time", line=1)
            self.tank_controller.lcd.print("", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("Any key to continue", line=4)

        elif self.substate == 6:
            self.tank_controller.lcd.print("Return to", line=1)
            self.tank_controller.lcd.print("main menu", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("Any key to continue", line=4)

    def start(self):
        """
        The function to display MANUAL SELECTED upon entering the ManualTitration state
        """
        self.tank_controller.lcd.print("MANUAL SELECTED", style="center", line=4)
