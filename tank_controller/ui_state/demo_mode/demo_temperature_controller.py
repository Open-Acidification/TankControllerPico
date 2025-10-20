"""
The file to demo the temperature controller device
"""

from tank_controller.devices.library import Keypad
from tank_controller.ui_state.ui_state import UIState


class DemoTemperatureControl(UIState):
    """
    The class to demo the temperature controller device
    """

    def handle_key(self, key):
        """
        The function to respond to a keypad input:
            Substate 1:
                1 -> Turn Heater On
                2 -> Turn Temperature Control On
                4 -> Return to Demo Mode Menu
            Substate 2-3:
                Any -> Substate 1
            D -> Return to Demo Mode Menu

        Parameters:
            key (char): the keypad input to determine which state to go to
        """
        if self.substate == 1:
            if key == Keypad.KEY_1:
                self.tank_controller.heater.on()
                self.substate = 2
            if key == Keypad.KEY_2:
                self.tank_controller.temp_controller.activate()
                self.substate = 3
            elif key == Keypad.KEY_4:
                self._set_next_state(self.previous_state, True)
        else:
            self.tank_controller.temp_controller.deactivate()
            self.tank_controller.heater.off()
            self.substate = 1

        if key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)

    def loop(self):
        """
        The function to loop through and display to the LCD screen until a new keypad input
        """
        if self.substate == 1:
            self.tank_controller.lcd.print("1: Test heater", line=1)
            self.tank_controller.lcd.print("2: Test controller", line=2)
            self.tank_controller.lcd.print("", line=3)
            self.tank_controller.lcd.print("4: Return", line=4)

        elif self.substate == 2:
            self.tank_controller.lcd.print("Test heater", line=1)
            self.tank_controller.lcd.print(
                f"{self.tank_controller.temperature_probe_control.get_temperature():>4.3f} C",
                line=2,
                style="center",
            )
            self.tank_controller.lcd.print(
                "Heater on: " + str(self.tank_controller.heater.value), line=3, style="center"
            )
            self.tank_controller.lcd.print("Any key to turn off", line=4)

            # Safety Check, does not allow the temperature to get above 80 C
            if self.tank_controller.temperature_probe_control.get_temperature() > 80:
                self.tank_controller.temp_controller.heater_off()
                self.substate = 1

        elif self.substate == 3:
            self.tank_controller.lcd.print("Test controller", line=1)
            self.tank_controller.lcd.print(
                f"{self.tank_controller.temperature_probe_control.get_temperature():>4.3f} C",
                line=2,
                style="center",
            )
            self.tank_controller.lcd.print(
                "Heater on: " + str(self.tank_controller.heater.value), line=3, style="center"
            )
            self.tank_controller.lcd.print("Any key to turn off", line=4)
