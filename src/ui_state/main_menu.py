"""
The file for the MainMenu class
"""

from src.devices.library import Keypad
from src.ui_state.set_menu.set_chill_or_heat import SetChillOrHeat
from src.ui_state.set_menu.set_google_mins import SetGoogleSheetInterval
from src.ui_state.set_menu.set_kd import SetKD
from src.ui_state.set_menu.set_ki import SetKI
from src.ui_state.set_menu.set_kp import SetKP
from src.ui_state.set_menu.set_ph_calibration import PHCalibration
from src.ui_state.set_menu.set_ph_calibration_clear import ResetPHCalibration
from src.ui_state.set_menu.set_ph_sine_wave import SetPHSineWave
from src.ui_state.set_menu.set_ph_target import SetPHTarget
from src.ui_state.set_menu.set_pid_on_off import EnablePID
from src.ui_state.set_menu.set_tank_id import SetTankID
from src.ui_state.set_menu.set_thermal_calibration import SetThermalCalibration
from src.ui_state.set_menu.set_thermal_calibration_clear import (
    ResetThermalCalibration,
)
from src.ui_state.set_menu.set_thermal_sine_wave import SetThermalSineWave
from src.ui_state.set_menu.set_thermal_target import SetThermalTarget
from src.ui_state.set_menu.set_time import SetTime
from src.ui_state.ui_state import UIState
from src.ui_state.view_menu.view_device_address import ViewDeviceAddress
from src.ui_state.view_menu.view_free_memory import ViewFreeMemory
from src.ui_state.view_menu.view_google_sheet_interval import (
    ViewGoogleSheetInterval,
)
from src.ui_state.view_menu.view_log_file import ViewLogFile
from src.ui_state.view_menu.view_ph_calibration import ViewPHCalibration
from src.ui_state.view_menu.view_pid_constants import ViewPIDConstants
from src.ui_state.view_menu.view_tank_id import ViewTankID
from src.ui_state.view_menu.view_thermal_correction import (
    ViewThermalCorrection,
)
from src.ui_state.view_menu.view_time import ViewTime
from src.ui_state.view_menu.view_version import ViewVersion


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
            ViewGoogleSheetInterval,  # View Google mins
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
            self.move_up()
        elif key == Keypad.KEY_4:  # left
            self.move_left()
        elif key == Keypad.KEY_6:  # right
            self.move_right()
        elif key == Keypad.KEY_8:  # down
            self.move_down()
        else:
            # ignore invalid keys
            pass

    def move_left(self):
        """
        Handles 'left' key: go up one menu level or return to idle.
        """
        if self.level2 == -1:
            self.level1 = 0
        else:
            self.level2 = -1

    def move_right(self):
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

    def move_up(self):
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

    def move_down(self):
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
            self._set_next_state(
                next_state_class(self.titrator, previous_state=self), True
            )

    def select_set(self):
        """
        Transitions to the selected 'Set' menu state.
        """
        if 0 <= self.level2 < len(self.set_menu_actions):
            next_state_class = self.set_menu_actions[self.level2]
            self._set_next_state(
                next_state_class(self.titrator, previous_state=self), True
            )

    def idle(self):
        """
        Displays the idle screen.
        """
        lcd = self.titrator.lcd
        lcd.print("Idle Line 1", line=1)
        lcd.print("Idle Line 2", line=2)

    def loop(self):
        """
        Updates the LCD display based on the current menu state.
        """
        lcd = self.titrator.lcd

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
