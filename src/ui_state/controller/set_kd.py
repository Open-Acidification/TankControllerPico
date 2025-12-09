"""
The file to hold the Set KD class
"""

from src.ui_state.user_value.user_value import UserValue


class SetKD(UserValue):
    """
    This is a class for the SetKD state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.eeprom.get_kd(36.0))

    def get_label(self):
        return "Set KD"

    def save_value(self):
        self.titrator.eeprom.set_kd(self.value)
        self.titrator.lcd.print(f"New KD={self.titrator.eeprom.get_kd(36.0)}", line=2)
        self.return_to_main_menu(ms_delay=3000)
