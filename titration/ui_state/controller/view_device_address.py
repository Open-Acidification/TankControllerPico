"""
The file to hold the View Device Address class
"""

import time
import random
# import socket
# import uuid
from titration.devices.library import Keypad
from titration.ui_state.ui_state import UIState


class ViewDeviceAddress(UIState):
    """
    This is a class for the ViewDeviceAddress state of the Tank Controller
    """

    def __init__(self, titrator, previous_state=None):
        super().__init__(titrator)
        self.previous_state = previous_state
        self._suppress_until = 0.0
        self._suppress_duration = 2

    def loop(self):
        """Display the current IP and MAC address on the LCD.

        This tries to read network information from the titrator if available
        (for example a hardware/network wrapper). If not available it falls
        back to querying the host system (socket/uuid) or uses safe
        placeholders.
        """
        if time.monotonic() < self._suppress_until:
            return

        ip_str = "192.168.1.10"
        mac = b"\x90\xa2\xda\x00\x00\x00"
        mac_str = f"{mac[0]:02X}{mac[1]:02X}:{mac[2]:02X}{mac[3]:02X}:{mac[4]:02X}{mac[5]:02X}"

        # Preferred: titrator.network interface (if provided by the runtime)
        net = getattr(self.titrator, "network", None)
        if net is not None:
            # IP
            if hasattr(net, "localIP"):
                ip_val = net.localIP()
                # join 4 octets like "192.168.0.10"
                ip_str = ".".join(str(o) for o in ip_val)
            elif hasattr(net, "ip"):
                ip_str = str(net.ip)
            elif hasattr(net, "isUsingDHCP"):
                serial_iface = getattr(self.titrator, "serial", None)
                msg = f"DHCP address is {ip_str}"
                serial_iface(msg)
        # else:
        #     # Fallback: try to get IP via socket and MAC via uuid
        #     try:
        #         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #         # doesn't actually send data, just used to pick a good interface
        #         s.connect(("8.8.8.8", 80))
        #         ip_str = s.getsockname()[0]
        #         s.close()
        #     except Exception:
        #         ip_str = "0.0.0.0"

        #     try:
        #         node = uuid.getnode()
        #         m = [((node >> ele) & 0xFF) for ele in range(40, -1, -8)]
        #         mac_str = f"{m[0]:02X}{m[1]:02X}:{m[2]:02X}{m[3]:02X}:{m[4]:02X}{m[5]:02X}"
        #     except Exception:
        #         mac_str = "00:00:00:00:00:00"

        self.titrator.lcd.print(ip_str, line=1)
        self.titrator.lcd.print(mac_str, line=2)

    def readmac(self, force_reset: bool = False):
        """
        Read and possibly reset the MAC address stored in EEPROM.
        """
        # (Replace with real EEPROM read in your integration)
        bytes6 = list(getattr(self, "_eeprom_mac", [0, 0, 0, 0, 0, 0]))
        if force_reset or bytes6[0] != ord("#"):
            try:
                seed = time.time_ns()
            except Exception:
                seed = int(time.time() * 1000)
            random.seed(seed)

            bytes6[0] = ord("#")
            bytes6[3] = random.randrange(256)
            bytes6[4] = random.randrange(256)
            bytes6[5] = random.randrange(256)
        mac_str = (
            f"MAC address is {bytes6[0]:02X}{bytes6[1]:02X}:"
            f"{bytes6[2]:02X}{bytes6[3]:02X}:"
            f"{bytes6[4]:02X}{bytes6[5]:02X}"
        )
        self.titrator.lcd.print(mac_str, line=2)

    def handle_key(self, key):
        if key == Keypad.KEY_HASH:  # '#'
            # TODO disable watchdog. wdt_disable()
            self.titrator.lcd.print("WDT disabled", line=1)
            self._suppress_until = time.monotonic() + self._suppress_duration

        if key == Keypad.KEY_B:
            # TODO Infinite loop to test Watchdog Timer. wdt_disable() -> wdt_enable(WDTO_15MS);
            self.titrator.lcd.print("WDT test", line=1)
            self._suppress_until = time.monotonic() + self._suppress_duration

        if key == Keypad.KEY_C:
            self.readmac()
            self._suppress_until = time.monotonic() + self._suppress_duration
            self.loop()

        if key == Keypad.KEY_4 or key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)
