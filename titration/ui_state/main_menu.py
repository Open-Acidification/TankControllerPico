"""
The file for the MainMenu class
"""
from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState
from titration.ui_state.controller.set_ph_target import SetPHTarget
from titration.ui_state.controller.set_pid_on_off import EnablePID
from titration.ui_state.controller.set_ph_calibration import PHCalibration
from titration.ui_state.controller.set_ph_calibration_clear import ResetPHCalibration
from titration.ui_state.controller.set_thermal_calibration_clear import ResetThermalCalibration
from titration.ui_state.controller.set_chill_or_heat import SetChillOrHeat
from titration.ui_state.controller.set_google_mins import SetGoogleSheetInterval
from titration.ui_state.controller.set_kd import SetKD
from titration.ui_state.controller.set_ki import SetKI
from titration.ui_state.controller.set_kp import SetKP
from titration.ui_state.controller.set_ph_sine_wave import SetPHSineWave
from titration.ui_state.controller.set_thermal_sine_wave import SetThermalSineWave
from titration.ui_state.controller.set_tank_id import SetTankID
from titration.ui_state.controller.set_thermal_calibration import SetThermalCalibration
from titration.ui_state.controller.set_thermal_target import SetThermalTarget
from titration.ui_state.controller.set_time import SetTime
from titration.ui_state.controller.view_device_address import ViewDeviceAddress
from titration.ui_state.controller.view_free_memory import ViewFreeMemory
from titration.ui_state.controller.view_google_mins import ViewGoogleMins
from titration.ui_state.controller.view_log_file import ViewLogFile
from titration.ui_state.controller.view_ph_calibration import ViewPHCalibration
from titration.ui_state.controller.view_pid_constants import ViewPIDConstants
from titration.ui_state.controller.view_tank_id import ViewTankID
from titration.ui_state.controller.view_thermal_correction import ViewThermalCorrection
from titration.ui_state.controller.view_time import ViewTime
from titration.ui_state.controller.view_version import ViewVersion


class MainMenu(UIState):
    """
    This is a class for the MainMenu state of the Tank Controller
    """

    def __init__(self, titrator):
        super().__init__(titrator)
        # level1: 0 = idle, 1 = View, 2 = Set
        self.level1 = 0
        # level2: -1 = top of menu, 0+ = specific menu item
        self.level2 = -1

        # Display menu lists
        self.view_menus = [
            "View IP and MAC",
            "View free memory",
            "View Google mins",
            "View log file",
            "View pH slope",
            "View PID",
            "View tank ID",
            "View temp cal",
            "View time",
            "View version",
        ]
        self.set_menus = [
            "pH calibration",
            "Clear pH calibra",
            "Clear Temp calib",
            "Set chill/heat",
            "Set Google mins",
            "Set KD",
            "Set KI",
            "Set KP",
            "Set pH target",
            "Set pH w sine",
            "Set Temp w sine",
            "PID on/off",
            "Set Tank ID",
            "Temp calibration",
            "Set temperature",
            "Set date/time",
        ]
        self.view_command_count = len(self.view_menus)
        self.set_command_count = len(self.set_menus)

        # Transition/navigation menu list
        self.view_menu_actions = [
            ViewDeviceAddress,  # View IP and MAC
            ViewFreeMemory,  # View Free Memory
            ViewGoogleMins,  # View Google mins
            ViewLogFile,  # View Log File
            ViewPHCalibration,  # View pH slope
            ViewPIDConstants,  # View PID constants
            ViewTankID,  # View Tank ID
            ViewThermalCorrection,  # View Thermal Correction
            ViewTime,  # View Time
            ViewVersion,  # View Version
        ]

        self.set_menu_actions = [
            PHCalibration,  # pH calibration
            ResetPHCalibration,  # Clear pH calibra
            ResetThermalCalibration,  # Clear Temp calib
            SetChillOrHeat,  # Set chill/heat
            SetGoogleSheetInterval,  # Set Google mins
            SetKD,  # Set KD
            SetKI,  # Set KI
            SetKP,  # Set KP
            SetPHTarget,  # Set pH target
            SetPHSineWave,  # Set pH with sine wave
            SetThermalSineWave,  # Set Temperature with sine wave
            EnablePID,  # Set PID on/off
            SetTankID,  # Set Tank ID,
            SetThermalCalibration,  # Set Temp Calibration,
            SetThermalTarget,  # Set Temperature,
            SetTime,  # Set Time,
        ]

    def handle_key(self, key):
        """
        Handles key presses and updates the menu state accordingly.
        """
        # Example placeholder logic, replace with your actual key handling logic
        if key == Keypad.KEY_A:  # Set pH set_point
            self._set_next_state(SetPHTarget(self.titrator, self), True)
        elif key == Keypad.KEY_B:  # Set Temperature set_point
            self._set_next_state(SetThermalTarget(self.titrator, self), True)
        elif key == Keypad.KEY_C:
            pass
        elif key == Keypad.KEY_D:  # Reset
            self.level1 = 0
            self.level2 = -1
        elif key == Keypad.KEY_2:  # up
            self.up()
        elif key == Keypad.KEY_4:  # left
            self.left()
        elif key == Keypad.KEY_6:  # right
            self.right()
        elif key == Keypad.KEY_8:  # down
            self.down()
        else:
            # ignore invalid keys
            pass

    def left(self):
        """
        Handles 'left' key: go up one menu level or return to idle.
        """
        if self.level2 == -1:
            self.level1 = 0
        else:
            self.level2 = -1

    def right(self):
        """
        Handles 'right' key: enter/advance menu or select item.
        """
        if self.level1 == 0:
            self.level1 = 1
            self.level2 = -1
        elif self.level2 == -1:
            self.level2 = 0
        elif self.level1 == 1:
            self.select_view()
        else:
            self.select_set()

    def up(self):
        """
        Handles 'up' key: cycles main menu or moves up in submenu, wrapping around.
        """
        if self.level2 == -1:
            self.level1 = (self.level1 + 2) % 3
        else:
            if self.level1 == 1:
                self.level2 = (
                    self.level2 + self.view_command_count - 1
                ) % self.view_command_count
            else:
                self.level2 = (
                    self.level2 + self.set_command_count - 1
                ) % self.set_command_count

    def down(self):
        """
        Handles 'down' key: cycles main menu or moves down in submenu, wrapping around.
        """
        if self.level2 == -1:
            self.level1 = (self.level1 + 1) % 3
        else:
            if self.level1 == 1:
                self.level2 = (self.level2 + 1) % self.view_command_count
            else:
                self.level2 = (self.level2 + 1) % self.set_command_count

    def select_view(self):
        """
        Transitions to the selected 'View' menu state.
        """
        if 0 <= self.level2 < len(self.view_menu_actions):
            next_state_class = self.view_menu_actions[self.level2]
            self._set_next_state(next_state_class(self.titrator, previous_state=self), True)

    def select_set(self):
        """
        Transitions to the selected 'Set' menu state.
        """
        if 0 <= self.level2 < len(self.set_menu_actions):
            next_state_class = self.set_menu_actions[self.level2]
            self._set_next_state(next_state_class(self.titrator, previous_state=self), True)

    def idle(self):
        """
        Displays the idle screen.
        """
        lcd = (
            self.titrator.lcd
        )  # Assuming your titrator has an lcd attribute with a .print() method
        lcd.print("Idle Line 1", line=1)
        lcd.print("Idle Line 2", line=2)

    def loop(self):
        """
        Updates the LCD display based on the current menu state.
        """
        lcd = (
            self.titrator.lcd
        )  # Assuming your titrator has an lcd attribute with a .print() method

        if self.level1 == 0:
            self.idle()
        else:
            if self.level1 == 1:
                if self.level2 == -1:
                    lcd.print("View settings", line=1)
                else:
                    lcd.print(self.view_menus[self.level2], line=1)
            else:
                if self.level2 == -1:
                    lcd.print("Change settings", line=1)
                else:
                    lcd.print(self.set_menus[self.level2], line=1)
            lcd.print("<4   ^2  8v   6>", line=2)
