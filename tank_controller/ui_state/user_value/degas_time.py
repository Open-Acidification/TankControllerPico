"""
The file for the DegasTime class
"""

from tank_controller.ui_state.user_value.user_value import UserValue


class DegasTime(UserValue):
    """
    This is a class for the DegasTime state of the titrator
    """

    def save_value(self):
        """
        The function to save the titrator's degas time
        """
        self.tank_controller.degas_time = self.value

    def get_label(self):
        """
        The function to return the label printed on the LCD Screen
        """
        return "Degas time (s):"
