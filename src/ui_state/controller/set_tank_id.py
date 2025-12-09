"""
The file to hold the Set Tank ID class
"""

from src.ui_state.user_value.user_value import UserValue


class SetTankID(UserValue):
    """
    This is a class for the SetTankID state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.eeprom.get_tank_id(1))

    def get_label(self):
        """
        Returns the label to prompt user value input.
        """
        return "Set Tank ID#"

    def save_value(self):
        """
        Saves the entered Tank ID value to EEPROM.
        """
        self.titrator.eeprom.set_tank_id(int(self.value))
        self.titrator.lcd.print(
            f"New Tank ID={self.titrator.eeprom.get_tank_id(1)}", line=2
        )
        self.return_to_main_menu(ms_delay=3000)
