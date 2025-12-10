"""
The file to hold the Set KP class
"""

from src.ui_state.user_value import UserValue


class SetKP(UserValue):
    """
    This is a class for the SetKP state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.eeprom.get_kp(20.0))

    def get_label(self):
        """
        Returns the label to prompt user value input.
        """
        return "Set KP"

    def save_value(self):
        """
        Saves the entered KP value to EEPROM.
        """
        self.titrator.eeprom.set_kp(self.value)
        self.titrator.lcd.print(f"New KP={self.titrator.eeprom.get_kp(20.0)}", line=2)
        self.return_to_main_menu(ms_delay=3000)
