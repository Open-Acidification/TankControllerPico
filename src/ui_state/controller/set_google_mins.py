"""
The file to hold the Set Google Sheet Interval class
"""

from src.ui_state.user_value.user_value import UserValue


class SetGoogleSheetInterval(UserValue):
    """
    UI state to set the Google Sheets upload interval (minutes).
    Uses UserValue's keypad flow: implement get_label and save_value.
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator, previous_state)
        self.previous_state = previous_state
        self.value = str(self.titrator.eeprom.get_google_sheet_interval(20))

    def get_label(self):
        return "G Sheet Minutes"

    def save_value(self):
        self.titrator.eeprom.set_google_sheet_interval(int(self.value))

        self.titrator.lcd.print(
            f"New interval={self.titrator.eeprom.get_google_sheet_interval(20)}", line=2
        )
        self.return_to_main_menu(ms_delay=3000)
