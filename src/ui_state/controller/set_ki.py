"""
The file to hold the Set KI class
"""

from src.ui_state.user_value.user_value import UserValue


class SetKI(UserValue):
    """
    This is a class for the SetKI state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.eeprom.get_ki(28.0))

    def get_label(self):
        """
        Returns the label to prompt user value input.
        """
        return "Set KI"

    def save_value(self):
        """
        Saves the entered KI value to EEPROM.
        """
        self.titrator.eeprom.set_ki(self.value)
        self.titrator.lcd.print(f"New KI={self.titrator.eeprom.get_ki(28.0)}", line=2)
        self.return_to_main_menu(ms_delay=3000)
