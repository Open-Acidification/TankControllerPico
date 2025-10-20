"""
The file for the PumpVolume class
"""

from tank_controller.ui_state.user_value.user_value import UserValue


class PumpVolume(UserValue):
    """
    This is a class for the PumpVolume state of the titrator
    """

    def save_value(self):
        """
        The function to save the titrator's pump volume
        """
        self.tank_controller.pump_volume = self.value

    def get_label(self):
        """
        The function to return the label printed on the LCD Screen
        """
        return "Volume in pump (ml):"
