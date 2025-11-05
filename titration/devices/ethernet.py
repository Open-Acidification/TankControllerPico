"""
Establishes the Ethernet connection and sets class variables
https://docs.arduino.cc/libraries/ethernet/
"""

from __future__ import annotations

import socket
import uuid


class Ethernet:
    """
    Ethernet controller class for Tank Controller.
    """

    def __init__(self) -> None:
        self.default_mac = "90A2:DA00:0000"
        self.mac = self.default_mac

        self.default_ip = "192.168.1.10"
        self.ip = self.default_ip

        self.is_using_dhcp: bool = False

        self.num_attempted_dhcp_releases: int = 0

    def get_ip(self) -> str:
        """
        Get the current IP address as a string.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            self.ip = s.getsockname()[0]
        finally:
            s.close()
        return self.ip

    def get_mac(self):
        """
        Retrieves the MAC address of the local machine.
        """
        try:
            mac_num = hex(uuid.getnode()).replace("0x", "").upper()
            mac_num = mac_num.zfill(12)
            self.mac = ":".join(mac_num[i : i + 4] for i in range(0, 12, 4))
        except Exception:
            self.mac = self.default_mac
        return self.mac

    def is_connected_to_network(self) -> bool:
        """
        Check if connected to a network (DHCP enabled)."""
        return bool(self.is_using_dhcp)

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
            Ethernet.maintain()
        self.num_attempted_dhcp_releases += 1
