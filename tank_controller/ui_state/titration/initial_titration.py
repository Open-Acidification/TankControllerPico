"""
The file for the InitialTitration class
"""

from tank_controller.devices.library import Keypad
from tank_controller.ui_state.titration.automatic_titration import AutomaticTitration
from tank_controller.ui_state.titration.manual_titration import ManualTitration
from tank_controller.ui_state.ui_state import UIState


class InitialTitration(UIState):
    """
    This is a class for the InitialTitration state of the titrator

    Attributes:
        titrator (Titrator object): the titrator is used to move through the state machine
        previous_state (UIState object): the previous_state is used to return the last visited state
        substate (int): the substate is used to keep track of substate of the UIState
        choice (int): the choice variable is used to select auto or manual titration
    """

    def __init__(self, titrator):
        """
        The constructor for the InitialTitration class

        Parameters:
            titrator (Titrator object): the titrator is used to move through the state machine
        """
        super().__init__(titrator)
        self.choice = 0

    def handle_key(self, key):
        """
        The function to respond to a keypad input:
            1 -> Manual Titration
            2 -> Automatic Titration

        Parameters:
            key (char): the keypad input to determine manual or automatic titration
        """
        if self.substate == 1:
            self.choice = key
            self.substate += 1

    def loop(self):
        """
        The function to loop through and display to the LCD screen until a new keypad input
        """
        if self.substate == 1:
            self.tank_controller.lcd.print("Bring pH to 3.5:", line=1)
            self.tank_controller.lcd.print("Manual: 1", line=2)
            self.tank_controller.lcd.print("Automatic: 2", line=3)
            self.tank_controller.lcd.print("Stir speed: slow", line=4)

        elif self.substate == 2:
            self.tank_controller.lcd.print("Heating to 30 C...", line=1)
            self.tank_controller.lcd.print("", line=2)
            self.tank_controller.lcd.print("Please wait...", style="center", line=3)
            self.tank_controller.lcd.print("", line=4)

            if self.choice == Keypad.KEY_1:
                self._set_next_state(ManualTitration(self.tank_controller), True)
            else:
                self._set_next_state(AutomaticTitration(self.tank_controller), True)
