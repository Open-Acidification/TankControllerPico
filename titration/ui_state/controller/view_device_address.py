"""
The file to hold the View Device Address class
"""
import time
import socket
import uuid
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

        ip_str = "0.0.0.0"
        mac_str = "00:00:00:00:00:00"

        # Preferred: titrator.network interface (if provided by the runtime)
        net = getattr(self.titrator, "network", None)
        if net is not None:
            # try common method names used by network wrappers
            try:
                if hasattr(net, "get_ip"):
                    ip_val = net.get_ip()
                    ip_str = str(ip_val)
                elif hasattr(net, "ip"):
                    ip_str = str(net.ip)
            except Exception:
                ip_str = "0.0.0.0"

            try:
                if hasattr(net, "get_mac"):
                    mac = net.get_mac()
                    mac_str = ":".join([f"{b:02X}" for b in mac])
                elif hasattr(net, "mac"):
                    mac_val = net.mac
                    # if mac_val is bytes-like
                    try:
                        mac_str = ":".join([f"{b:02X}" for b in mac_val])
                    except Exception:
                        mac_str = str(mac_val)
            except Exception:
                mac_str = "00:00:00:00:00:00"
        else:
            # Fallback: try to get IP via socket and MAC via uuid
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # doesn't actually send data, just used to pick a good interface
                s.connect(("8.8.8.8", 80))
                ip_str = s.getsockname()[0]
                s.close()
            except Exception:
                ip_str = "0.0.0.0"

            try:
                node = uuid.getnode()
                mac_str = ":".join([f"{(node >> ele) & 0xFF:02X}" for ele in range(40, -1, -8)])
            except Exception:
                mac_str = "00:00:00:00:00:00"

        # Print to LCD (tests/mocks use lcd.print(message, line=1|2))
        self.titrator.lcd.print(ip_str, line=1)
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
            # Reset MAC. readMac(true);
            self.loop()

        if key == Keypad.KEY_D:
            # TODO Return to main menu
            self._set_next_state(self.previous_state, True)

        if key == Keypad.KEY_4:  # Left key
            self._set_next_state(self.previous_state, True)
