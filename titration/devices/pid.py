"""Host-side PID controller wrapper translated from the firmware header.
"""
from titration.devices.eeprom import EEPROM


class PID:
    """Host-side PID controller wrapper translated from the firmware header."""
    def __init__(self):
        """The constructor for the mock PID class."""
        eeprom = EEPROM()

        self.kp = eeprom.kp_address
        self.ki = eeprom.ki_address
        self.kd = eeprom.kd_address

        # self.input = 0.0
        # self.output = 0.0
        # self.setpoint = 0.0

    # def get_mode(self) -> bool:
    #     """Return the current mode."""
    #     return self.use_pid

    # def setKd(self, kd) -> None:
    #     self.kd = (kd)

    # def setKi(self, ki: float) -> None:
    #     self.ki = float(ki)

    # def setKp(self, kp: float) -> None:
    #     self.kp = float(kp)

    # def setTunings(self, kp: float, ki: float, kd: float) -> None:
    #     self.kp = float(kp)
    #     self.ki = float(ki)
    #     self.kd = float(kd)
