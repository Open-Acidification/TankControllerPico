"""
The file for mocking the LiquidCrystal class for testing purposes
"""

# pylint: disable = unused-argument

LCD_WIDTH = 20
LCD_HEIGHT = 4


class LiquidCrystal:
    """
    Generalized mock class for character LCD displays of any width and height.
    """

    def __init__(self):
        """
        Initialize the mock LCD with configurable width and height.
        """
        self.cols = LCD_WIDTH
        self.rows = LCD_HEIGHT

        self.lcd_lines = [None] * self.rows
        self.lcd_line_styles = [None] * self.rows

    def print(self, message, line, style="left"):
        """
        Send a string to the mock LCD at the given line (1-based) and style.
        """
        if style == "left":
            style = "w"
        elif style == "right":
            style = "e"

        idx = line - 1
        if 0 <= idx < self.rows:
            self.lcd_lines[idx] = message
            self.lcd_line_styles[idx] = style

    def get_line(self, line):
        """
        Get the message for the given line (1-based).
        """
        idx = line - 1
        if 0 <= idx < self.rows:
            return self.lcd_lines[idx]
        return "ERROR"

    def get_style(self, line):
        """
        The function to get the lcd line message
        """
        idx = line - 1
        if 0 <= idx < self.rows:
            return self.lcd_line_styles[idx]
        return "ERROR"
