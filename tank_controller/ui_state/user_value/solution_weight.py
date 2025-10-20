"""
The file for the SolutionWeight class
"""

from tank_controller.ui_state.user_value.user_value import UserValue


class SolutionWeight(UserValue):
    """
    This is a class for the SolutionWeight state of the titrator
    """

    def save_value(self):
        """
        The function to save the titrator's solution weight
        """
        self.tank_controller.solution_weight = self.value

    def get_label(self):
        """
        The function to return the label printed on the LCD Screen
        """
        return "Sol. weight (g):"
