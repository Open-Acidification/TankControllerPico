"""
The file for the PHProbe class

EZO pH Circuit | Atlas Scientific
https://www.atlas-scientific.com/files/pH_EZO_Datasheet.pdf

Issuing the "Cal,mid,n\r" command will
clear the other calibration points.

While the data sheet uses "Slope" the actual string is "SLOPE"
Similarly, "Cal,?" is actually "CAL,?" and responses are "?CAL,2" for example.
"""

from titration.devices.library import ADS, analog_in, board, busio

CALIB_BUFFER = 17
SLOPE_BUFFER = 32
CALIB_USABLE = CALIB_BUFFER - 1  # 16 usable chars
SLOPE_USABLE = SLOPE_BUFFER - 1  # 31 usable chars


class PHProbe:
    """
    The class for the pH Probe device
    """

    def __init__(self, gain=1):
        """
        The constructor for the PHProbe class
        Initializes I2C pins, gain, and voltage

        Parameters:
            gain (float): gain of the PHProbe

        firmware used a 17-byte and 32-byte buffer (16/31 usable chars) — keep parity by truncating
        """
        self.calibration_response = ""
        self.slope_response = ""
        self.slope_is_out_of_range: bool = False

        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.channel = analog_in.AnalogIn(self.ads, ADS.P0, ADS.P1)

        self.ads.gain = gain
        self.gain_options = [2 / 3, 1, 2, 4, 8, 16]

    def send_calibration_request(self) -> None:
        """
        The function to request calibration status from the pH probe.
        In the real device this prints "CAL,?\r" to Serial1 and the device
        responds; here we mock that behavior by storing the expected
        response string in calibration_response.
        """
        self.calibration_response = "PH Calibration"

    def get_calibration(self, size):
        """
        The function to return the pH probe's calibration response
        """
        usable = min(CALIB_USABLE, max(0, int(size) - 1))
        return self.calibration_response[:usable]

    def send_slope_request(self) -> None:
        """
        Simulate sending a slope request to the probe.
        In firmware: Serial1.print(F("SLOPE,?\r"));
        """
        self.slope_response = "Requesting..."

    def get_slope(self, size):
        """
        The function to return the pH probe's slope response
        for example "99.7,100.3, -0.89" or "Requesting..."
        """
        usable = min(SLOPE_USABLE, max(0, int(size) - 1))
        return self.slope_response[:usable]

    def get_voltage(self):
        """
        The function to return the pH probe's voltage
        """
        return self.channel.voltage

    def set_gain(self, gain):
        """
        The function to set the pH probe's gain

        Parameters:
            gain (int): the gain of the PHProbe
        """
        if gain not in self.gain_options:
            raise ValueError(f"Gain must be one of: {self.gain_options}")
        self.ads.gain = gain

    def get_gain(self):
        """
        The function to return the pH probe's gain
        """
        return self.ads.gain
