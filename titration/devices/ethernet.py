"""
Establishes the Ethernet connection and sets class variables
https://docs.arduino.cc/libraries/ethernet/
"""

from __future__ import annotations

import random
import socket
import time
# import uuid
# from typing import Optional, Tuple
from typing import Tuple


class EthernetTC:
    """
    Ethernet controller class for Tank Controller.
    """

    def __init__(self) -> None:
        # default MAC (matches the C++ example)
        self.mac: bytes = b"\x90\xa2\xda\x00\x00\x00"

        # default IP as a 4-tuple (192,168,1,10)
        self.default_ip: Tuple[int, int, int, int] = (192, 168, 1, 10)
        # self.ip = "192.168.1.10"

        # current IP (start with default)
        self.ip: Tuple[int, int, int, int] = tuple(self.default_ip)

        # DHCP flag
        self.is_using_dhcp: bool = False

        # testing / diagnostic
        self.num_attempted_dhcp_releases: int = 0

    def get_ip(self) -> str:
        """
        Get the current IP address as a string.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            addr = s.getsockname()[0]  # e.g. "192.168.1.10"
            parts = addr.split(".")
            if len(parts) == 4:
                self.ip = tuple(int(part) & 0xFF for part in parts)
        finally:
            s.close()
        return ".".join(str(o) for o in self.ip)

    def is_connected_to_network(self) -> bool:
        """
        Check if connected to a network (DHCP enabled)."""
        return bool(self.is_using_dhcp)

    def get_mac(self) -> bytes:
        """
        Get the MAC address as bytes.
        """
        return bytes(self.mac)

    def read_mac(self, force_reset: bool = False) -> str:
        """
        Read and possibly reset the MAC address stored in EEPROM.
        """
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
            # Copy the generated/persisted bytes into the object’s mac[]
            # with setMac(bytes) & EEPROM.update(MAC_ADDRESS...)
        mac_str = (
            f"{bytes6[0]:02X}{bytes6[1]:02X}:"
            f"{bytes6[2]:02X}{bytes6[3]:02X}:"
            f"{bytes6[4]:02X}{bytes6[5]:02X}"
        )
        # Log the MAC with serial(...).

        return mac_str

    def get_num_attempted_dhcp_releases(self) -> int:
        """
        Get the number of attempted DHCP releases.
        """
        return int(self.num_attempted_dhcp_releases)

    def loop(self):
        """Placeholder for periodic Ethernet tasks (DHCP renewals etc.).

        In this host-side translation we don't implement real DHCP. If you
        want to simulate behavior inject a `network` object that exposes a
        `begin(mac)` method and `local_ip()`/`mac()` accessors.
        """
        if self.is_using_dhcp:
            EthernetTC.maintain()
        self.num_attempted_dhcp_releases += 1
