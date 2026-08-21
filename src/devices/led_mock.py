"""
Mock LED device for the Tank Controller.
"""


class LED:
    """Mock LED that tracks an ON/OFF state."""

    def __init__(self):
        """Initialize the LED as off."""
        self.is_on = False

    def on(self):
        """Turn the LED on."""
        self.is_on = True

    def off(self):
        """Turn the LED off."""
        self.is_on = False

    def toggle(self):
        """Toggle the LED between on and off."""
        self.is_on = not self.is_on
        