"""
The file to test the Ethernet class
"""

from unittest import mock

from titration.devices.ethernet import Ethernet


def test_get_ip_uses_socket_and_updates():
    """
    Test that get_ip uses socket and updates the IP address correctly.
    """
    mock_socket = mock.Mock()
    mock_socket.getsockname.return_value = ("123.123.1.12", 12345)
    with mock.patch(
        "titration.devices.ethernet.socket.socket", return_value=mock_socket 
    ):
        ethernet = Ethernet()
        ip_address = ethernet.get_ip()
        assert ip_address == "123.123.1.12"
        assert ethernet.ip_address == "123.123.1.12"
        mock_socket.connect.assert_called_once_with(("8.8.8.8", 80))
        mock_socket.close.assert_called_once()


def test_get_mac_retrieves_local_address_and_formats():
    """
    Test that get_mac retrieves the MAC address of the local machine.
    """
    node_int = 0xAB12CD345678
    with mock.patch("titration.devices.ethernet.uuid.getnode", return_value=node_int):
        ethernet = Ethernet()
        mac_address = ethernet.get_mac()
        assert mac_address == "AB12:CD34:5678"
        assert ethernet.mac_address == "AB12:CD34:5678"


def test_is_connected_to_network_reflects_dhcp_flag():
    """
    Test that is_connected_to_network reflects the DHCP flag correctly.
    """
    eth = Ethernet()
    eth.is_using_dhcp = False
    assert eth.is_connected_to_network() is False
    eth.is_using_dhcp = True
    assert eth.is_connected_to_network() is True
