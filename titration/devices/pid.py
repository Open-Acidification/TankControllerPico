"""Host-side PID controller wrapper translated from the firmware header.
"""


class PID:
    """Host-side PID controller wrapper translated from the firmware header."""
    def __init__(self):
        """The constructor for the mock PID class."""
        self.kp = 1.1
        self.ki = 2.2
        self.kd = 3.3
        self.use_pid = True

        # self.input = 0.0
        # self.output = 0.0
        # self.setpoint = 0.0

    def get_kd(self):
        """Return the derivative gain."""
        return self.kd

    def get_ki(self):
        """Return the integral gain."""
        return self.ki

    def get_kp(self):
        """Return the proportional gain."""
        return self.kp

    def get_mode(self) -> bool:
        """Return the current mode."""
        return self.use_pid

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
