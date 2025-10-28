"""
The file to hold the View Device Address class
"""

import time
import uuid

from titration.devices.ethernet import EthernetTC
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

        ethernet = EthernetTC()
        ip_str = ethernet.get_ip()
        raw_mac = ethernet.get_mac()

        if isinstance(raw_mac, (bytes, bytearray, list, tuple)):
            m = [int(x) & 0xFF for x in raw_mac][:6]
            mac_str = f"{m[0]:02X}{m[1]:02X}:{m[2]:02X}{m[3]:02X}:{m[4]:02X}{m[5]:02X}"
        else:
            mac_str = str(raw_mac)

        # new feature: MAC address generation
        try:
            node = uuid.getnode()
            m = [((node >> ele) & 0xFF) for ele in range(40, -1, -8)]
            mac_str = f"{m[0]:02X}{m[1]:02X}:{m[2]:02X}{m[3]:02X}:{m[4]:02X}{m[5]:02X}"
        finally:
            pass

        self.titrator.lcd.print(ip_str, line=1)
        self.titrator.lcd.print(mac_str, line=2)

    def handle_key(self, key):
        if key == Keypad.KEY_HASH:  # '#'
            # disable watchdog. wdt_disable()
            self.titrator.lcd.print("WDT disabled", line=1)
            self._suppress_until = time.monotonic() + self._suppress_duration

        if key == Keypad.KEY_B:
            # Infinite loop to test Watchdog Timer. wdt_disable() -> wdt_enable(WDTO_15MS);
            self.titrator.lcd.print("WDT test", line=1)
            self._suppress_until = time.monotonic() + self._suppress_duration

        if key == Keypad.KEY_C:
            mac_str = EthernetTC().read_mac()
            # self.titrator.lcd.print(f"MAC address is {mac_str}", line=2)
            self.titrator.lcd.print(mac_str, line=2)
            self._suppress_until = time.monotonic() + self._suppress_duration
            self.loop()

        if key == Keypad.KEY_4 or key == Keypad.KEY_D:
            self._set_next_state(self.previous_state, True)
