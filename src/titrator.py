"""
The file for the Titrator class
"""

# pylint: disable = too-many-instance-attributes

from src.devices.date_time import DateTime
from src.devices.eeprom import EEPROM
from src.devices.library import (
    Heater,
    Keypad,
    LiquidCrystal,
    StirControl,
    SyringePump,
    TemperatureControl,
    TemperatureProbe,
)
from src.devices.ph_control import PHControl
from src.devices.ph_probe_mock import PHProbe
from src.devices.pid import PID
from src.devices.sd import SD
from src.devices.thermal_probe import ThermalProbe
from src.ui_state.main_menu import MainMenu
from src.version import VERSION


class Titrator:
    """
    The Titrator class is the model for the state machine in order
    to move through the different titration states

    Attributes:
        state (UIState object): is used to represent the current state in the state machine
        next_state (UIState object): is used to move to the next state in the state machine
        keypad (Keypad object): is used to identify what keypad value was entered
    """

    def __init__(self):
        """
        The constructor for the Titrator class
        """
        # Initialize EEPROM
        self.eeprom = EEPROM()

        # Initialize DateTime
        self.date_time = DateTime()

        # Initialize PID Controller
        self.pid = PID(self.eeprom)

        # Initialize PH Control
        self.ph_control = PHControl(self)

        # Initialize Thermal Probe
        self.thermal_probe = ThermalProbe(self.eeprom)

        # Initialize SD Card
        self.sd_device = SD()

        # Initialize LCD
        self.lcd = LiquidCrystal()

        # Initialize Keypad
        self.keypad = Keypad()

        # Initialize pH Probe
        self.ph_probe = PHProbe(self.eeprom)

        # Initialize Syringe Pump
        self.pump = SyringePump()

        # Initialize Stir Controller
        self.stir_controller = StirControl()

        # Initialize Temperature Probes
        self.temperature_probe_control = TemperatureProbe(1)
        self.temperature_probe_logging = TemperatureProbe(2)

        # Initialize Heater to PIN 12
        self.heater = Heater(12)

        # Initialize Temperature Controller
        self.temp_controller = TemperatureControl(
            self.temperature_probe_control, self.heater
        )

        # Initialize State
        self.state = MainMenu(self)
        self.next_state = None

        # Initialize Titrator Values
        self.solution_weight = "0"
        self.solution_salinity = "0"

        # Stir Control Values
        self.degas_time = 0

        # pH Calibration Values
        self.buffer_measured_volts = 0
        self.buffer_nominal_ph = 0

        # Pump Volume Values
        self.pump_volume = 0
        self.volume_to_move = 0

        # Temperature Calibration Values
        self.reference_temperature = 0

        self.tank_controller_version = VERSION

    def loop(self):
        """
        The function used to loop through in each state
        """
        self.temp_controller.update()
        self.update_state()
        self.handle_ui()

    def set_next_state(self, new_state, update):
        """
        The function used to set the next state the state machine will enter
        """
        self.next_state = new_state
        if update:
            self.update_state()

    def update_state(self):
        """
        The function used to move to the next state
        """
        if self.next_state:
            print(
                "Titrator::updateState() from",
                self.state.name(),
                "to",
                self.next_state.name(),
            )
            self.state = self.next_state
            self.next_state = None
            self.state.start()

    def handle_ui(self):
        """
        The function used to receive the keypad input and process the appropriate response
        """
        key = self.keypad.get_key()
        if key is not None:
            print("Titrator::handle_ui() key pressed:", key)
            self.state.handle_key(key)
        self.state.loop()

    def get_version(self):
        """
        The function used to get the software version
        """
        return self.tank_controller_version
